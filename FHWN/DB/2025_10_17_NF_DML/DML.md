

# DML

## Insertion

### Insert single row
```sql
INSERT INTO athlete_results (Name, NOC, Medal)
VALUES ("Foo", "BAR", "Diamond");
```
### Insert multiple rows

```sql
INSERT INTO athlete_results (Name, NOC, Medal)
VALUES 
    ("Foo", "BAR", "Amethyst"),
    ("Foo", "BAR", "Ruby"),
    ("Foo", "BAR", "Emerald"),
    ("Foo", "BAR", "Sapphire"),
    ("Foo", "BAR", "Topaz"),
    ("Foo", "BAR", "Skull");
```

### Insert results of a query
```sql
INSERT INTO athlete_results (Name, NOC, Year, Event, Medal)
SELECT 'Mate', 'HUN', 2222, t.Event, 'Wood'
FROM (
    SELECT DISTINCT Event FROM athlete_results
) t;
```

## Update

```sql
UPDATE athlete_results
SET Year = 2222
WHERE Name = 'Foo';
```

## Delete
```sql
DELETE FROM athlete_results WHERE Year = 2222;
```

