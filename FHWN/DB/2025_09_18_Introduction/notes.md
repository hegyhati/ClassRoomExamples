# Introduction to DB (Database) / RDBMS (Relational Database Management System)

> [!CAUTION]
> This is only a brief listing of some cornerpoints of the course material, and **cannot** be considered as a full-fledged learning material in itself.
> This only serves as a short recap of the most important concepts. 
> Reading the book and additional resources is still necessary. 


## Motivation for DB

### What do we want/need?

Store (a lot of) data (in a structured way).

![What do we want](./what_do_we_want.jpg)

### Why?

To get asnwers to questions and/or keep state of things.
 - What are the latest news?
 - How many people and who liked my last insta post?
 - Which supermarket is still open nearby? 
 - etc.

### What do we do with that data?

**C** reate it

**R** ead it

**U** pdate it

**D** elete it

## With what tool? 

### General wisdom

> Use the right tool for the job.

Each scenario / requiremenet / use-case is different, chose the tool for storing the data based on your needs, not what allegedly *the best*, *the state-of-the-art* tool is.

> If your only tool is a hammer, every problem looks like a nail.

RDBMS is not the only solution. 
It is a **very** important tool to know, but not suited for everything.
If it *feels* inadequate, look for a more fitting tool, in most of the cases there is something.
Be open to learn, extend your knowledge, avoid becoming a one-trick pony. 

> Don't bring a knife to a gun fight

Excel. is. NOT. a. database!

![Excel](./excel.jpg)

> Don't use a sledgehammer to crack a nut.

The tool for your beer tasting diary does not need a distributed Oracle Cloud Autonomous Database with in-memory processing, multi-region replication, and Kubernetes orchestration.

> If it ain't broke, don't fix it.

If your backend runs fine on a good old local MySQL DB, there's no need to jump on the hype bandwagon and ditch it for a trendy BaaS.

### Rule of thumbs

**Small amount of data, mostly hierarchical and changing structure, single user** 
→  A JSON file should do the trick.

**If it grows a lot, but the structure remains changing**  → Good time to move to a Document based NoSQL solution. (MongoDB, Couchbase, etc.)

**You don't want to manage it yourself, looking for a cloud solution** 
→ Something like Firebase is easy to set up, and can carry you a long way.

**If the structure solidifies and in a relational manner** → Probably a good time to learn about RDBMS. Logical to move for safety and speed, especially if data keeps growing.

**Small amount of mostly tabular data, with unfrequent changes or deletions, single user with manual editing needs**
→ A spreadsheet application will suffice.

**Same, but programmable access is needed** 
→ You can probably still get away with a spredsheet and a dataframe library like pandas.

**Data keeps growing, just a few sheets, just additions, mostly analytical functions, pivot tables**
→ OLAP is the way.

**Or instead: more and more sheets, interconnected by lot of `XLOOKUP`, `INDEX`, etc. and/or need for multiple users**
→ This suggests OLTP direction with RDBMS.

#### RDBMS rule of thumbs

**Small/Medium size, single user, manual edits, reports** 
→ MS Acces / Libreoffice Base is a reasonable choice.

**Still a single user and small/medium size, but need for programmable access**
→ Sqlite is most probably enough for these needs. (VERY prominent for embedded / mobile apps.)

**Larger size and/or need for multiple users possibly over the internet**
→ Open source proper DBMS, like MySQL, PosgreSQL is a good choice.

**Parallelization and performance become crucial due to growing size, query frequency**
→ State-of-the-art proprietary RDBMS, like Oracle, MS SQL is necessary.

**If it is not legally necessary for data to be on-premise, and infrastructure management is better outsourced**
→ Cloud native managed RDBMS (AWS RDS, Azure SQL).

**Same but simpler cases**
→ Supabase will probably ease your workflow (similar to Firebase in the NoSQL realm).

#### Still more

Confused already? We still haven't touched on:
 - Time-series data → InfluxDB, TimescaleDB
 - Special type of data (e.g. geodata) → PostGIS, GeoJSON
 - Graph-like relationships → Neo4j
 - Streaming platforms → Apache Kafka, Pulsar
 - ...

> [!IMPORTANT]  
> You **DON'T** need to learn all these at once. You’ll likely never use more than half — but you don’t know which half.
> The key takeaway: there are tools for many needs. When the need arises, be curious.

> [!NOTE]  
> From now on we will focus on RDBMS if not stated otherwise.
> Some statements, techniques apply for other type of DBMS as well, some don't. 

So, from now on, when referring to a DB, it is implied to be a relational DB, unless stated otherwise.

## Relational DB basics

### 3 levels of design

In the end, all data is stored by 0s and 1s, but - as in many areas in IT - it is standard practice to break up this process into several layers of *abstraction*.
Moreover, in a relational DB, the data is **structured**, i.e., it follows certain rules, thus we can separate:
 - the structure of the DB, called schema or metadata
 - the actual data, that is stored following that structure

When planing/designing a DB, we refer to planing the structure/schema of the DB.

In DB design, there are generally 3 steps / layers considered, that go as far as files and indexing, beyond that, low-level storage is handled by the operating system and hardware.
In the semester we mainly focus on the first 2 layers.

#### Conceptual design
Translates the real world requirements into the conceptual model, that is:
 - high level: mostly focuses on _what_ to store, and how these things are _related_, not on how to store 
 - formal: strict rules and structural notation, not just unregulated sketches
 - typically an ER diagram (detailed next sesstion)

#### Logical design

Converts the conceptual model to the logical model, detailed later.
Mostly automatic process, but human decisions are needed on:
 - data types
 - selection of keys
 - normalization
 - data consistency constraints
 - deletion propagation

These things will be discussed later.

#### Physical design

Determines how the logical model is stored, and (if the DBMS supports it) access control. 
Usually vendor specific, includes performance optimization decisions, etc.

### Logical model of RDBMS

A beauty of the RDBMS logical model is, that it's building blocks are few and simple. 
Complexity arises on _how_ these are used.

#### Basic building blocks

 - The DB is made up of (a finite set of) **table**s .
 - Each table consists of (a finite set of) **column**s.
 - Each column has its unique (for that table) **name** and **type** (can be vendor specific, but most basic ones are standard).
 - **Row**s (sometimes called records) will hold the actual data, and each **field** (cell) must have the type prescribed by the column.
 - No two rows in the same table may have exactly the same **values** across all columns.
 - Each column may have additional constraints on the values.

In relational algebra (covered in later sessions)  - that provides the mathematical basis for this model - tables and columns are referred to as relations and attributes, which names may also be used interchangeably.

#### Keys

While each row is unique (according to the rule above), usually a smaller subset *should* be enough to unambiguously identify them, i.e., no two rows can have identical values across that subset of culomns either.
Note, that such a "rule" is a direct consequence of the values we want to store. It is a planning decision of the database designer, who understands the semantics of the real world requirements.
Consequently, this decision has to be stated explicitely in the logical model.

Such a subset of columns is called a *key*. If it consists of a single column it is called a *simple key* otherwise a *composite key*. 
Naturally, the whole set of columns could be a key, and a real superset of any key could also be a key.
Keys, that are minimal, i.e., no subset of them can be a key are called *candidate key*s. 
If not stated otherwise, keys usually refer to candidate keys.

Usually, one candidate key is selected to be the *default* way of identifying a row, and nominated as the **primary key**. 
Primary key column(s) can not be nullable, i.e., must always contain data.

If columns in a table must match key values from another table, it is called a *foreign key*.

#### Nullability

In most DBMS solutions, the absence of a value is allowed by default (except for  the PK). 
Sometimes this is desired, sometimes not, again the decision of the designer.

## Database (Query) language

Users, programs must somehow interact with the DBMS, and the formal language of that is called the database language, tha can generally have these parts:
 - **DDL** - Data Definition Language - used for defining the schema
 - **DML** - Data Manipulation Language - used to add/update/delete data
 - **DQL** - Data Query Language - used to retreive data (sometimes considered part of DML)
 - **DTL** - Data Transaction Language - used for transaction management (discussed later, again sometimes considered as part of DML)
 - **DCL** - Data Control Language - used for managing access rights of users

Unlike in many fields in IT, luckily, the industry have (mostly) settled for one such language: **SQL** - Structured Query Language. 
Don't let the name mislead you, it is not only a DQL, but the whole package.

*All* RDBMS use SQL, or, to be more precise, a dialect of it. 
Vendors that do not support multiple users, obviously don't have any DCL parts of SQL. 
Moreover, vendors may extend SQL with features specific to them.

Nevertheless, just knowing the "standard" SQL is enough to solve most of the problems with any of the RDBMS vendors.

Finally, there are other (sometimes vendor-specific) languages, like HTSQL, PRQL, LINQ, MDX that play similar roles for specific tasks, but they are almost always defined on top of SQL, transpile to SQL in the background. 
Typically, they don't add capabilities compared to "low level" SQL, just simplify specific tasks for the programmer.

## Recapception (recap of the recap)
![Acronyms](./acronyms.jpg)

Test yourself by explaining the meaning of these acronyms: 
 - TLA
 - DB
 - DBMS
 - RDBMS
 - CRUD
 - BaaS
 - JSON
 - OLAP
 - SQL
 - DDL
 - DML
 - DTL
 - DCL
 - DQL
 - PK
 - ER
 - SQL


