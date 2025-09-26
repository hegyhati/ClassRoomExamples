# Goal

We work for a company that makes and sells costumes of popular fictional characters. 
In order to increase sales, we plan to collect data, that will allow us to have a targeted marketing campaign. 

What we want to do things like:
 - Send an e-mail to people about a costume of their favorite superhero before Carnival & Helloween. 
 - If a purchase is not made, send an e-mail to their good firends with the same offer before Christmas.
 - If a person already likes an actor, who has a new movie coming up, send an e-mail about the costume of his/her role in that movie few weeks before the debut. 

> [!NOTE]
> Don't do this at home. Everything here would be highly unethical, most probably illegal. 

# Data

To be able to do this, we need some data, that we will aquire from multiple sources:

## Webshop

We will launch a webshop on which we will sell these costumes.

 - Users will be able to register with an e-mail address. 
 - Users may specify their size, so that it will automatically be selected for them. 
 - We will log all purchases.

Each offers sent out in e-mails and redirect to unique landing site, thus we can log, if a purchase was successful. 
An offer is valid only for 3 days and may be used only once.

## Meta

To have information about the populations social network, we can buy the following info from Meta:
 - list of users, with their
   - name
   - e-mail address
   - list of friends
   - list of followed pages
 - list of pages, with their
   - name
   - category
   - list of followers

## TMDB

Information about movies, actors, etc. is luckily publickly available on the internet. 
We task our intern to scrape or fetch data about movies (past and upcoming) and the actors playing in them, and their roles.

# Tasks
 - Make the ER model needed for our DB.
 - Prepare the logical model based on the conceptual model.
 - Write the SQL script that initializes the tables.
 