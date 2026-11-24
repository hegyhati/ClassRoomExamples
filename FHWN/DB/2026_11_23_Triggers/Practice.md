# Base story

We want to store students in a dormitory. 
 - For each student, store some attributes like name, age, gender
 - Same for rooms, e.g., floor, room number, street_side.

## Setup

Create the tables, and insert some rooms.

## Trigger exercises

## Simple room capacity

Assume that all of the rooms have 2 beds.
When adding a new student, check if the selected room is full or not. 
If so, raise an exception.

## More complex condition

Modify the schema and the trigger so, that each room has their own capacity.

## Additional constriants

Include additional constraints, like maximal age-gap, only same gender rooms, etc.

## Adaptive allocation

Don't raise an exception when room is full, rather find another suitable empty room and place the new student there.
If nothing is available, then raise an exception. 
    