# Database Management Systems - Written Test 1
2026.11.09

## 1. True or false
Decide whether each statement is true or false. In the latter case, provide a one-sentence explanation.

 - A relational database table can have multiple non-composite primary keys,.
 - In a relation that is in 2NF, every non-key attribute depends only on the primary key.
 - A `WHERE` clause can be used to filter groups after aggregate functions have been applied.

## 2. Short explanation
Briefly explain how a 1-to-many relationship can be implemented in the logical design, and provide a small example.

## 3. DB Design exercise - bicycles and gear sets
We want to do research on the first names used for characters in novels from the 19th century. We need to store all of the first first names that appear. For each novel, we need to record the author, the title, the year it was published, and how many different characters are mentioned with each first name.


### 3.1. Conceptual model
Draw the ER diagram for the data described above.

### 3.2. Logical model
Write the DDL statements for the database.

### 3.3. Query
Write the SQL queries that answer the following questions:
1. How many books did Charles Dickens publish?
2. Which 3 authors published the most books between 1820 and 1850?
3. How many characters are called Natasha or Nikolai in War and Peace?
