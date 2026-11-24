# Database Management Systems - Written Test 1
2026.11.09

## 1. True or false 
Decide whether each statement is true or false. In the latter case, provide a one-sentence explanation.

 - In a relational database, every composite key must be a primary key.
 - If an attribute depends on a subset of a composite key, it violates the rules of the 1st normal form.
 - A `SELECT` SQL query always returns only the first page of the results, and subsequent pages require additional queries.

## 2. Short explanation
Briefly explain how a many-to-many relationship can be implemented in the logical design, and provide a small example.

## 3. DB Design exercise - mobile phones
We want to make a website where we can compare different mobile phones on the market. We want to store the brand and the model of the phone (e.g., Samsung Galaxy S8), the release year, the list price in USD, the amount of RAM it comes with, along with the CPU model including its manufacturer, the clock speed, and the number of cores.

### 3.1. Conceptual model
Draw the ER diagram for data described above.

### 3.2. Logical model
Write the DDL statements for the database.

### 3.3. Query
Write the SQL queries that answer the following question. 
1. What were the 3 most expensive phones from 2026?
2. Which brands have released less than 10 models?
3. Are there any phones from 2016 that have an 8-core CPU?


