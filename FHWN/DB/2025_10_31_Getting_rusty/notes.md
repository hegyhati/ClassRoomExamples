# Movies, finally

# 1. ERD / tables
Plan a database, that can hold plenty of information about movies:
 - basic things, like title, release date, runtime
 - which acters played which roles in the movies
 - in which countries was it produced and what languages are spoken

Then, extend the schema to be able to accept data from the first class:
 - list of friends, their relationships (not friends, friends, close friends) 
 - favorite superheroes, previous halloween party dress ups

Check if your schema satisfy 3NF. 
If not, normalize the tables that don't. 

# 2. Realize the DB
Use [this database](db/movies.sqlite) and extend it with your new tables. 

# 3. Add a few data manually
Insert the data of 3 friends and a few favorite superheroes for all of them by executing `INSERT` statements manually. 

# 4. Create a view
For simpler queries later, create a view, that has 3 columns:
 - friend
 - role that this friend likes
 - whether the friend has ever dressed up as this role

Use the `LIKE` operator to find roles, that match a favorite character.

# 5. Answer some questions
 0. For friend A, what are the movies, where at least one favorite superhero appears?
 1. Can all of our friends have costumes from movies not older than x years?
 2. Is there a movie, to whose screening both A and B can go in the costume of one of their favorite superheroes (who appear in that movie).
 3. Is there an actor who is loved by both A and B but for different characters?

# 6. Make an application
Write a Rust program that provides you a TUI for:
 - logging new data
 - answering the above questions

# 7. Pimp it yourself
Implement / realize your own idea.
