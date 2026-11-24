# Citystrides competition

We would like to provide the "backbone" for a website like [CityStridesVS](https://hegyhati.github.io/citystrides_vs/all/), that tracks a few friends progress (and competition) on [citystrides.com](https://citystrides.com/).


## Base tables

First we need a table to store users. A simple solution:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    nickname TEXT UNIQUE NOT NULL,
    color TEXT NOT NULL 
);
```

Where `id` is the CS id from the website.

This is ok(ish), but color could be anything, we could introduce a check to only accept `rgb(r,g,b)` format:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    nickname TEXT UNIQUE NOT NULL,
    color TEXT NOT NULL CHECK (color ~ '^rgb\([0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\)$')
);
```
If you have nightmares about regexes, you can create your own type like this:


```sql
CREATE DOMAIN color_channel AS SMALLINT CHECK (VALUE BETWEEN 0 AND 255);

CREATE TYPE rgb AS (
    r color_channel,
    g color_channel,
    b color_channel
);

CREATE TABLE users (
    id INT PRIMARY KEY,
    nickname TEXT UNIQUE NOT NULL,
    color rgb NOT NULL
);
```

Let's insert some data into the table: 

```sql
INSERT INTO users (id, nickname, color) VALUES
(666, 'Lucifer', '(6,6,6)'::rgb),
(42, 'Deep Thought', '(42,42,42)'::rgb),
(404, 'Anonymus', '(4,0,4)'::rgb),
(7, 'James Bond', '(0,0,7)'::rgb),
```

Now, we want to store each run, and how many new steets it meant for the runner:

```sql
CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id),
    streets_collected INT NOT NULL,
    collected_at TIMESTAMPTZ NOT NULL
);
```

Not bad, but:
 - if we delete a user, there is no need to keep her/his runing data
 - the number of streets collected by a run cannot be negative
 - if no timestamp is available, we should have a fallback of assigning the current time 

So:

```sql
CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    streets_collected INT NOT NULL CHECK (streets_collected >= 0),
    collected_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

Add some runs

```sql
INSERT INTO runs (user_id, streets_collected) VALUES
(666, 7),
(42, 4),
(404, 4)
(42, 2);
```
## Views

Most often we will want to see a toplist of users based on streets, something like this:

| Nickname | Total streets |
| --- | --- | 
| Lucifer | 7 |
| Deep Thought | 6 | 
| Anonymus | 4 |
| James Bond | 0 | 

We can have all the data for that with a query:

```sql
SELECT 
    users.nickname AS nickname,
    SUM(runs.streets_collected) AS total_streets
FROM users JOIN runs ON users.id = runs.user_id
GROUP BY nickname
ORDER BY total_streets DESC;
```

And if we use that often enough, we can just make a view for that:

```sql
CREATE VIEW v_user_streets_toplist AS
SELECT 
    users.nickname AS nickname,
    SUM(runs.streets_collected) AS total_streets
FROM users JOIN runs ON users.id = runs.user_id
GROUP BY nickname
ORDER BY total_streets DESC;
```

This is a regular/standard/virtual view. If we get a lot of queries for this, and we are happy with "daily standindgs", we can create a materialized view of it:


```sql
CREATE MATERIALIZED VIEW mv_user_streets_toplist AS
SELECT 
    users.nickname AS nickname,
    SUM(runs.streets_collected) AS total_streets
FROM users JOIN runs ON users.id = runs.user_id
GROUP BY nickname
ORDER BY total_streets DESC
WITH DATA;
```

Then, each midnigcht a cron-job can just update it:


```sql
REFRESH MATERIALIZED VIEW mv_user_streets_toplist;
```

## Triggers

Nowadays triggers are useful mostly in these scenarios:
 - Preserving data consistency, where other tools (e.g. ,`CHECK`) lacks capability:
   - when more context than the row is needed
   - when we don't want to just simply refuse incorrect data, but try to correct it if possible
 - logging type of features
 - "making views writable" 


### Simple data correction

We don't want to have names, that have leading/trailing spaces.

We could do that by adding a constraint on `users.nickname`:

```sql
CHECK (nickname !~ '(^[[:space:]]|[[:space:]]$)')
```
or 
```sql
CHECK (nickname NOT LIKE ' %' AND nickname NOT LIKE '% ')
```

If the table is already created we can add it later like this:


```sql
ALTER TABLE users
ADD CONSTRAINT chk_no_leading_trailing_spaces
CHECK (nickname !~ '(^[[:space:]]|[[:space:]]$)')
```

This fails if existing data already has nicknames with leading/trailing spaces. 
Clean them up in advance, or use `NOT VALID` temporarily.


This works, however, imagine what happens, when we want to register a new user, and the name contains trailing spaces:
 - our application sends the `INSERT` statement.
 - the database receives it, the check fails.
 - the database sends back an error to the application.
 - the application receives the error message, and if we handled this situation correctly:
 - the application removes the leading/trailing spaces from the name
 - the application resends the request with the updated name
 - the database receives the new user, checks it, the check passes, and inserts it into the table
 - the database sends an OK to the application, which happily continues doing whatever it is doing

There are two issues with this:
 - there are 2 roundtrips between the application and the database instead of just 1
 - the logic, that trailing and leading spaces should be removed are implemented as a check on the DB side, and as a fixing routine on the application side

In essence this is equivalent to reviewing someones work in a docx file seeing a typo, leaving a comment for that, saving the docx, then sending back in an e-mail. Unless this is part of our KPI, it makes everybodys life easier if we simply fix the typo. 

So, it would be nicer if the DBMS would fix this instead of just raising an error. This is where a simple check falls short, and triggers come to the rescue.

Triggers have essentially two parts:
 1. a function itself that needs to be run
 2. a statement connection this function to events when it should be run

First the function:

```sql
CREATE OR REPLACE FUNCTION normalize_nickname()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.nickname := btrim(NEW.nickname);
    RETURN NEW;
END;
$$;
```
`NEW` will always reference the row to be `INSERT`ed, or the new version of a row to be `UPDATE`d. 
Similarly, `OLD` refers to the row to be `DELETE`d, or the old version of a row to be `UPDATE`d, but we don't need that here.

Next we tell Postgres to run this function **before** inserting or updating a row in the `users` table:

```sql
CREATE TRIGGER trg_normalize_nickname
BEFORE INSERT OR UPDATE OF nickname ON users
FOR EACH ROW
EXECUTE FUNCTION normalize_nickname();
```

That's it.

Several notes:
 - `BEFORE` instructs the DBMS to do this before insertion/update/deletion. Because of that we can still modify the data.
 - In case of `AFTER`, that is not available, we would need to execute a DML query to change the already inserted row if we want to. 
 - `FOR EACH ROW` means, that if we have an update/insert/delet that affects multiple lines, this function will be called for all of them. 
 - `FOR EACH STATEMENT` would only execute the function once (even if 0 rows are affected) and `NEW` or `OLD` arenot available in the called function.
 - The third option would be `INSTEAD OF`.

### Prevent duplicate activities

In an ideal world, we would get notified of each activity once. But nothing is perfect, the runner may connected multiple tracker applications, that report the same run, etc. We would like to have a rudimentary safegourd around that: if a run with the same number of streets is being inserted by the same user in 5 minutes, just ignore it. 


```sql
CREATE OR REPLACE FUNCTION prevent_duplicate_collection()
RETURNS TRIGGER AS $$
DECLARE
    last_streets INT;
    last_time TIMESTAMPTZ;
BEGIN
    SELECT streets_collected, collected_at
    INTO last_streets, last_time
    FROM runs
    WHERE user_id = NEW.user_id
    ORDER BY collected_at DESC, id DESC
    LIMIT 1;

    IF FOUND AND last_streets = NEW.streets_collected AND last_time >= NEW.collected_at - INTERVAL '5 minutes' THEN
        RAISE EXCEPTION 'Duplicate submission: User % already submitted % streets within the last 5 minutes.', NEW.user_id, NEW.streets_collected;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_prevent_duplicate_collection
BEFORE INSERT ON runs
FOR EACH ROW
EXECUTE FUNCTION prevent_duplicate_collection();
```

New things, things to note:
 - we will need two variables to store the timestamp/streetcount of the same users last run, we need to declare them in the beginning.
 - we use `INTO` in the `SELECT` to save the results of the query into the variables
 - `FOUND` will contain whether the `SELECT ... INTO ... ` statement before it was successful, i.e., found at least 1 run
 - `RAISE EXCEPTION` to raise an exception  
 - note, that a simple check would not work here, as we need information from other rows in the table, not just the current row.
 - think about what happens, if the transactions of duplicate activities happen at the same time.


### Log overtakings

There is nothing that motivates someone more, when she/he receives an e-mail, that a friend is beating her/him in a competition. 
We are Machiavellian if it is about healthy lifestlye, so we want to record such events, and rub the users nose in it.

So we create this table:


```sql
CREATE TABLE overtakings (
    id SERIAL PRIMARY KEY,
    overtaker_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    overtaken_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    overtaken_at TIMESTAMPTZ NOT NULL
);
```

So far pretty straight-forward. 

Now we need a trigger that chechs the old total sum of the user, the new one, and everyone who is between that: 


```sql
CREATE OR REPLACE FUNCTION overtakings_manager()
RETURNS TRIGGER AS $$
DECLARE
    user_new_total INT;
BEGIN
    SELECT SUM(streets_collected) INTO user_new_total
    FROM runs
    WHERE user_id = NEW.user_id;

    INSERT INTO overtakings (overtaker_id, overtaken_id, overtaken_at)
    SELECT 
        NEW.user_id,
        user_id,
        NEW.collected_at
    FROM runs
    WHERE user_id <> NEW.user_id
    GROUP BY user_id
    HAVING SUM(streets_collected) > user_new_total - NEW.streets_collected
       AND SUM(streets_collected) <= user_new_total;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_overtakings
AFTER INSERT ON runs
FOR EACH ROW
EXECUTE FUNCTION overtakings_manager();
```

Note, that this logging type of trigger can just run `AFTER` the insert was done.


This is fine, but this trigger function does two things:
 - calculates the old and new number of streets for the user of the inserted run
 - records overtakings in the overtakings table

If there could be several avenues how an overtaking happens (e.g., some old runs get updated, because street data changes), there would be several places where the same recording logic would be implemented redundantly. 

Again, here it is not really the case, but for the sake of illustration, lets separate that logic into a procedure:

```sql
CREATE OR REPLACE PROCEDURE record_overtakings(
    p_user_id INT,
    p_old_total INT,
    p_new_total INT,
    p_collected_at TIMESTAMPTZ
)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO overtakings (overtaker_id, overtaken_id, overtaken_at)
    SELECT 
        p_user_id,
        other.user_id,
        p_collected_at
    FROM (
        SELECT user_id, SUM(streets_collected) AS total_streets
        FROM runs
        WHERE user_id <> p_user_id
        GROUP BY user_id
    ) other
    WHERE other.total_streets > p_old_total 
      AND other.total_streets <= p_new_total;
END;
$$;

CREATE OR REPLACE FUNCTION overtakings_manager()
RETURNS TRIGGER AS $$
DECLARE
    user_new_total INT;
BEGIN
    SELECT SUM(streets_collected) INTO user_new_total
    FROM runs
    WHERE user_id = NEW.user_id;

    CALL record_overtakings(
        NEW.user_id,
        user_new_total - NEW.streets_collected,
        user_new_total,
        NEW.collected_at
    );

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_overtakings
AFTER INSERT ON runs
FOR EACH ROW
EXECUTE FUNCTION overtakings_manager();
```

Note, that we `EXECUTE` functions and `CALL` procedures. 