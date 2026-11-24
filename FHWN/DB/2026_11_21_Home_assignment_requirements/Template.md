> [!Note]
> First the brief title of the application

# FlightTracker

> [!Note]
> A brief description of the topic, not a full specification, just enough to "set the scene". 
> Use it to explain any not commonly known concepts.
> Someone with no special interest / previous knowledge in the field should gain all the necessary knowledge to understand the difficulty of each task below.
> For example: you don't need to explain what countries and flags are, but it is not general knowledge how points are counted in darts competitions.
> Be as brief as possible here, the details will be specified later.

The proposed application aims to track flights of passengers on airplanes, and derive interesting statistics based on that data.

# Features
> [!Note]
> This is the place where each feature is listed and well specified. 
> Don't talk about implementation like "There will be an Airport table, that has columns...". 
> Instead, specify what the user of the application will be able to do. 
> Try to group your features into logical subsections, and in the order how they "depend on each other". E.g., the feature for registering a user flight should come after registering the flight itself, which should come after having the airports and and the carrier registered. 

## Managing infrastructure and flights data (Admin interactions)

### Airports

> [!NOTE]
> For each feature use the following template:
> ---
> **Feature name**
>
> Brief description of the feature
>
> - list of additional constraints, like:
> - what data is needed for the feature
> - when the operation should succeed or not
> - also, what is assumed / will not be taken into consideration
> ---
>
> Use the 3 dashed to provide visual isolation of the features.

---

**Add airports**

The user can register new airports with their name, identifier and country.

- Identifiers must be 3 characters.
- Two airports with the same name or identifier cannot exist. 
- The country must be selected from the existing list of countries.
- Each airport must be either domestic or international.  
- Each airport has a GPS coordinate.

---

**Disable airports**

An airport may stop operation, which should be registered by the admin.

- A disabled airport can not start operation again. 
- An already disabled airport cannot be disabled.

---

**List airports**

The admin can list airports in a country. 
 
- For each listed item, it should be indicated whether an airport is international or domestig and whether it is still active or not.

---

**Search among airports**

The admin can search for airports.

- List all airports whose code or name includes the provided string as a substring. 
- The details defined above and the country name should also be visible for each airport.

---

### Aircraft

---

**Add new Aircraft type**

The admin can add new aircraft type.

- Two aircrafts with the same name cannot exist.
- Each aircraft have a list of seats. 
- Each seat on an aircraft is identified by a row number and a column letter.
- Each seat is either window, middle, or aisle.
- Each seat is assumed to have the same class. 

---

### Flights ###

---

**Add new flight**

The admin can announce a new flight between two airports, specifying the aircraft and the date & time of departure and arrival, and the price of a ticket. 

- The arrival time must be later than the departure time.
- The application will not consider different time zones and local time, everything will be in UTC+1. 
- Similarly the app will not consider daylight saving time.
- The time difference should be at least the distance / 1000 km/h. 
- The connected airports must either be international or domestic and in the same country. 
- The admin should be able to select both airports with searching from the available airports.
- The price is assumed to be the same for each seat on a flight and given always in EUR.

---

**Cancel flight**

The admin can register if a flight is canceled.

---

## Tickets (Passenger interactions)

---

**Search for flights**

A passenger can search for available flights between two airports within the provided dates.

- The passenger should be able to select both airports with searching from the available airports.
- Only flights that are not fully booked should be listed.
- The list should show the departure/arrival date & time, the number of available seats, and the price.
- Canceled flights should also not appear on the list.

---

**Book a flight**

When a passenger finds an offer satisfactory he/she can book it.

- When booking the passenger must also select a seat.
- We will only store anonymous statistical data for market research purposes. The passenger will only need to tell his/her age, gender, and whether he/she is traveling for business or leisure purposes. 

---

## Analysis (Market researcher interactions)

---

**Most/least preferred seats**

For each aircraft type, the analyst can list the top 5 most & least popular seats.

- After selecting the aircraft type from a list, it should be displayed, how many flights (not canceled) are advertised with this aircraft type.
- For each top/bottom seat, list how many times it was booked by someone, and whether it is an aisle/middle/window seat.

---

**Top destinations**

For each airport, the analyst can list the top 5 most popular destinations.

- There are two ordering criteria: either by total number of passengers or the "fullness" of flights (i.e., total tickets booked / available tickets)
- The analyst can restrict the analysis to certain age groups, gender or purpose of travel. 

---

**Connecting flights**

The analyst can list connections where no direct flights are available, but there is a demand.

 - A connection (A to B) should be listed if there are pasengers, who traveled from A to C and in less than 24 hours from C to B. 
 - Since users are not stored explicitly, we assume, that two users are the same if their age/gender/travelpurpose is the same.
 - Only 5 promising candidates for profitable connections are listed.
 - For each such connection, provide a list of transit airports (C in the above example) and how many people traveled though it.






