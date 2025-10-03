# Play along

For testing online, visit [this site](https://datawithdev.com/sql-playground/) and import the data from [the sqlite DB](/athlete_data_after2000.db).

Or use [DB Browsaer for SQLite](https://sqlitebrowser.org/) locally.

Data source: [Kaggle](https://www.kaggle.com/datasets/krishd123/olympics-legacy-1896-2020)

# DQL

## Basic commands

### Get all the data
```sql
SELECT * FROM athlete_results;
```

### Get only specific columnns
Name and team for all of the results:
```sql
SELECT Name,Team FROM athlete_results;
```

> [!NOTE] 
> Keywords can be in any case, `SELECT`, `select` and `sEleCt` does the same.
> But stick to one (of the first 2).

### Filter by condition
Get the name and sport for each Austrian athlete:
```sql
SELECT Name,Sport FROM athlete_results WHERE NOC = 'AUT';
```
> [!IMPORTANT]
> Double qutes are **NOT** used for string literals, they have to be used for table/column names if they contain spaces.

> [!NOTE]
> `=` is the "is equal" operator, not `==`. 
> But it is also accepted by a lot of DBMSs.


### Filter by multiple conditions
Get the name, exact event and medal of Austrian athletes who ended up on the podium:

```sql
SELECT Name, Event, Medal FROM athlete_results WHERE NOC = 'AUT' AND Medal != NULL;
```

> [!Caution]
> 0 results, because `NULL` is special. 
> 
> `anything = NULL` -> `false`
>
> `anything != NULL` -> `false`
> 
> Even:
> 
> `NULL = NULL` -> `false`
> 
> `NULL != NULL` -> `false`

Always use `IS NULL` or `IS NOT NULL`:

```sql
SELECT Name, Event, Medal FROM athlete_results WHERE NOC = 'AUT' AND Medal IS NOT NULL;
```

> [!NOTE]
> SQLite is lenient in many things, `IS` can be left out for example, but not proper SQL.



### Filter comparing columns
List where Country and Team differ:
```sql
SELECT Country,Team FROM athlete_results WHERE Country != Team;
```

### Remove duplicates
Same, but list each only once:
```sql
SELECT DISTINCT Country,Team FROM athlete_results WHERE Country != Team;
```

> [!Important]
> `DISTINCT` applies to the whole `Country,Team` tuple, so the same `Country` could appear twice if it had different `Team`s.

### Get the number of results
How many Gold medals did Austrian athletes won?
```sql
SELECT COUNT(*) FROM athlete_results where NOC = 'AUT' AND Medal = 'Gold';
```
> [!Note]
> `COUNT()` is also often accepted, again, not proper.


How many Austrian athletes won Gold medals?
```sql
SELECT COUNT(DISTINCT Name) FROM athlete_results where NOC = 'AUT' AND Medal = 'Gold';
```

### Order results
Order the countries by name:
```sql
SELECT DISTINCT Country FROM athlete_results ORDER BY Country;
```

## Grouping and nesting



### Group by attribute

Group Austrian athletes by Sport:
```sql
SELECT Name, Sport, Year FROM athlete_results WHERE NOC = 'AUT' GROUP BY Sport;
```
Which values are selected for `Name` and `Year` for each `Sport` group?!

> [!TIP]
> When using `GROUP BY`, it is a code smell if any non-groupping column remains as is without any aggregate function.

Count how many Gold medals each Country had:
```sql
SELECT Country, COUNT(Medal) FROM athlete_results WHERE Medal = 'Gold' GROUP BY Country;
```

Little bit nicer:
```sql
SELECT Country, COUNT(*) AS "Gold Medals" FROM athlete_results WHERE Medal = 'Gold' GROUP BY Country;
```

And sort it then:
```SQL
SELECT Country, COUNT(*) AS "Gold Medals" FROM athlete_results WHERE Medal = 'Gold' GROUP BY Country ORDER BY "Gold Medals";
```

Descending...
```SQL
SELECT Country, COUNT(*) AS "Gold Medals" FROM athlete_results WHERE Medal = 'Gold' GROUP BY Country ORDER BY "Gold Medals" DESC;
```

Only top 20:
```sql
SELECT Country, COUNT(*) AS "Gold Medals" FROM athlete_results WHERE Medal = 'Gold' GROUP BY Country ORDER BY "Gold Medals" DESC LIMIT 20;
```

Probably it is time to break it up to multiple lines for readibility:
```sql
SELECT 
    Country, 
    COUNT(*) AS "Gold Medals" 
FROM athlete_results 
WHERE Medal = 'Gold' 
GROUP BY Country 
ORDER BY "Gold Medals" DESC 
LIMIT 20;
```

### Nesting
Sometimes question cannot (easily) be answered in one go, an intermediate table is needed/useful.

What is the average number of Gold medals won by a Country in each event it participates?

Distinct participation of countries easy:
```sql
SELECT DISTINCT Country, Year, FROM athlete_results;
```

Count the medals:
```sql
SELECT 
    Country, 
    Year, 
    COUNT(Medal) AS Gold
FROM athlete_results
GROUP BY Country, Year;
```

This result as an "intermediate table" can be used for a subsequent query:
```sql
SELECT Country, AVG(Gold) AS "Average gold"
FROM (
    SELECT 
        Country, 
        Year, 
        COUNT(Medal) AS Gold
    FROM athlete_results
    GROUP BY Country, Year;
) t
GROUP BY Country;
ORDER BY "Average gold"
```


## Practice questions:
 - How many countries won a gold medal in the 2020 Olympics? 
 - Who participated at the most olympic games?
 - Who won the most Gold medals in a single event?
 - Was there an athlete who changed citizenship? 
 - Who are the two athletes that shared the podium the most times? 

# DDL

## Views

### Create (virtual) view
```sql
CREATE VIEW most_participations AS
SELECT Name, COUNT(*) AS Participation FROM (
    SELECT DISTINCT Name, Year, Season 
    FROM athlete_results 
) t
GROUP BY Name
ORDER BY Participation DESC
```

> [If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.](https://en.wikipedia.org/wiki/Duck_test)

Views...
 - ✅ look like tables
 - ✅ can be queried like a table
 - ❌ cannot be altered (DML) as tables (usually).
 - ❌ are not stored like tables

Views are not tables.
The results of the "construction query" is not stored, only the "recipe query". 
When querying a view, the recipe query is executed first to get the view.

### Querying View
Just like a table:
```sql
SELECT * from most_participations LIMIT 10;
```

### Create materialized View
Kinda like tables, data is cached also, but needs to be updated (mostly manually).

Not standard!

```sql
CREATE MATERIALIZED VIEW most_participations_materialized AS
SELECT Name, COUNT(*) AS Participation FROM (
    SELECT DISTINCT Name, Year, Season 
    FROM athlete_results 
) t
GROUP BY Name
ORDER BY Participation DESC
```

### Virtual vs. Material views

| | Virtual | Material|
| --- | --- | --- |
| Pro | small memory footrpint, always-up-to-date | faster to query, saves CPU | 
| Con | extra computation for every query | not up-to-date necessarily, additional memory need |

## Dropping

### Drop entire table or view
```sql
DROP VIEW most_participations;
```
![SQL Injection](Injection.PNG)


### Delete column/attribute
```sql
ALTER TABLE athlete_results DROP COLUMN A;
```