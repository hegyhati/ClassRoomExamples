# We want to maximize our profit/wealth over the span of a given number of days by buying and selling different car types.
# Known are:
# - the car types, and the price of each of them for each day
# - the number of days when we can trade
# - our initial budget
# - the number of garage spaces, that we can (and must) use to keep the bought cars safe from one day to another

param startbudget; # HUF 
param garagecapacity; #pieces
param nDays;

set Days := 1..nDays;
set Cars;

param price{Days,Cars}; # HUF

# Variables

## How many do I buy / sell from a car on a scpecific day.
var buysell{Days,Cars}, integer, >=-garagecapacity, <=garagecapacity;
    # positive if buying, negative if selling

## Balance at the end of the day
var balance{0..nDays} >= 0;

## Garage at the end of the day
var garage{0..nDays,Cars} >=0, <=garagecapacity;
    # Note: does not need to be an integer variable.

# Constraints

## I shouldn't spend more money than what I have
## Constraint no more needed, as variable bound expresses it.

## Connect the balance variable with the sellbuy variable and the startbudget
s.t. InitialBalance:
    balance[0]=startbudget;

s.t. ConnectBalanceBuySell{d in Days}:
    balance[d] = balance[d-1] - sum{c in Cars} price[d,c] * buysell[d,c];

## I can not sell a car that I don't have
## Contraint no more needed, as garage bounds expresses that

## Connect the garage variable with the sellbuy and initialize it
s.t. InitialGarage{c in Cars}:
    garage[0,c]=0;

s.t. ConnectGarageBuySell{d in Days, c in Cars}:
    garage[d,c]=garage[d-1,c] + buysell[d,c];
    
## I shouldn't have more cars at the end of the day, then my garage capacity
s.t. MeetGarageCapacity{d in Days}:
    sum {c in Cars} garage[d,c] <= garagecapacity;

## It is not advantageous to buy anything on the last day
s.t. RedundantConstraint1 {c in Cars}:
    buysell[nDays,c] <= 0;

# Objective funtction

## I want to maximize my budget in the end
maximize FinalBudget: balance[nDays];

