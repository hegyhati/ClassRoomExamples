# Description

I have a running club in Sopron, Loholó Duhajok. 
Each monday, some of us go for a grouprun. 
I want to make statistics about the people who have came the most in the last 3 months, half year, all time, etc. 
I also want to see, who has the longest streak.
Something like [this](https://duhajok.hu/singlepage.html#loholoduhajok-sortabla)
There are two more running clubs like this.

# Incremental solution

## 1 

There are runners with names and unique nicknames.

```sql
CREATE TABLE Runners (
    nickname VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30)
);
```

## 1 -> 2

There are running groups, each has a unique name, a city, where it is based. 
Each city has at most one group. 
Runners can belong to one of the groups.

```sql
CREATE TABLE Running_groups (
    name VARCHAR(30) PRIMARY KEY,
    city VARCHAR(30) UNIQUE
);
CREATE TABLE Runners (
    nickname VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30),
    group_name VARCHAR(30) REFERENCES Running_groups(name)
);
```

## 2 -> 3

Runners MUST belong to one of the groups.

```sql
CREATE TABLE Running_groups (
    name VARCHAR(30) PRIMARY KEY,
    city VARCHAR(30) UNIQUE
);
CREATE TABLE Runners (
    nickname VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30),
    group_name VARCHAR(30) NOT NULL REFERENCES Running_groups(name)
);
```
Questions:
 - Can a runner not belong to any group?
 - Can a group be empty?


## 3 -> 3'
If a group is deleted, so should be the runners. 

```sql
CREATE TABLE Running_groups (
    name VARCHAR(30) PRIMARY KEY,
    city VARCHAR(30) UNIQUE
);
CREATE TABLE Runners (
    nickname VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30),
    group_name VARCHAR(30) NOT NULL REFERENCES Running_groups(name) ON DELETE CASCADE
);
```

## 3 -> 3''
If a group is deleted, set the reference to `NULL`.

```sql
CREATE TABLE Running_groups (
    name VARCHAR(30) PRIMARY KEY,
    city VARCHAR(30) UNIQUE
);
CREATE TABLE Runners (
    nickname VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30),
    group_name VARCHAR(30) REFERENCES Running_groups(name) ON DELETE SET NULL
);
```

## 3 -> 4 

Don't let the group to be deleted if there is at least one member.

```sql
CREATE TABLE Running_groups (
    name VARCHAR(30) PRIMARY KEY,
    city VARCHAR(30) UNIQUE
);
CREATE TABLE Runners (
    nickname VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30),
    group_name VARCHAR(30) REFERENCES Running_groups(name) NOT NULL ON DELETE RESTRICT
);
```
Note: `RESTRICT` does not work on sqlite only PosgreSQL

## 4 -> 5
Each group has exactly one leader, and one person may only lead 1 group. 

```sql
CREATE TABLE Running_groups (
    name VARCHAR(30) PRIMARY KEY,
    city VARCHAR(30) UNIQUE,
    leader VARCHAR(30) REFERENCES Runners(nickname) ON DELETE RESTRICT UNIQUE NOT NULL
);
CREATE TABLE Runners (
    nickname VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30),
    group_name VARCHAR(30) REFERENCES Running_groups(name) NOT NULL ON DELETE RESTRICT
);
```
Question: Can someone from another group be the leader of a group?

## 5 -> 6

There are groupruns in each group, at most one a day.
Runners may attend to a grouprun or not. 

```sql
CREATE TABLE Running_groups (
    name VARCHAR(30) PRIMARY KEY,
    city VARCHAR(30) UNIQUE,
    leader VARCHAR(30) REFERENCES Runners(nickname) ON DELETE RESTRICT UNIQUE NOT NULL
);
CREATE TABLE Runners (
    nickname VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30),
    group_name VARCHAR(30) REFERENCES Running_groups(name) NOT NULL ON DELETE RESTRICT
);
CREATE TABLE Groupruns (
    id SERIAL PRIMARY KEY, -- Postgre SQL
    group_name VARCHAR(30) REFERENCES Running_groups(name) NOT NULL ON DELETE RESTRICT,
    day DATE NOT NULL,
    UNIQUE(group_name, day)
);

CREATE TABLE Attendances (
    runner VARCHAR(30) REFERENCES Runners(nickname) ON DELETE CASCADE,
    run_id INTEGER REFERENCES Groupruns(id) ON DELETE CASCADE,
    PRIMARY KEY (runner, run_id)
);
```
Notes:
 - auto increment id was needed because foreign key on Grouprun would be also 2 columns, and grouprun would have no "meaning"
 - auto increment is not standard, `SERIAL` works only on PostgreSQL




