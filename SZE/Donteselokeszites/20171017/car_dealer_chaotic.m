# We want to maximize our profit/wealth over the span of a given number of days by buying and selling different car types.
# Known are:
# - the car types, and the price of each of them for each day
# - the number of days when we can trade
# - our initial budget
# - the number of garage spaces, that we can (and must) use to keep the bought cars safe from one day to another



param startbudget; # HUF 
param garagecapacity; #pieces
param nDays;

param M := 10000000;

set Days := 1..nDays;
set Cars;

param price{Days,Cars}; # HUF

# Variables

## How many do I buy / sell from a car on a scpecific day.
var buy{Days,Cars}, integer, >=0, <=garagecapacity;
var sell{Days,Cars}, integer, >=0, <=garagecapacity;
var buyorsell{Days,Cars}, binary;
    # 1 if buying, 0 if selling
    
# Constraints

## I shouldn't spend more money than what I have
s.t. NoNegativeBalance{d in Days}:
    sum{c in Cars} buy[d,c] * price[d,c]
    <=
    startbudget
    + sum {dd in 1..d, c in Cars} sell[dd,c] * price[dd,c]
    - sum {dd in 1..d-1, c in Cars} buy[dd,c] * price[dd,c]
    ;
    

## I can not sell a car that I don't have
s.t. SellOnlyWhatIHave{d in Days, c in Cars}:
    sell[d,c] <=  sum {dd in 1..d} buy[dd,c] - sum {dd in 1..d-1} sell[dd,c];
    
## I shouldn't have more cars at the end of the day, then my garage capacity
s.t. MeetGarageCapacity{d in Days}:
    sum {dd in 1..d, c in Cars} (buy[dd,c]-sell[dd,c]) <= garagecapacity;

## We shouldn't buy and sell the same type of car on the same day
s.t. DontBuyAndSellTogether1{d in Days, c in Cars}:
    sell[d,c] <= M * (1 - buyorsell[d,c]);
s.t. DontBuyAndSellTogether2{d in Days, c in Cars}:
    buy[d,c] <= M * buyorsell[d,c];



## It is meaningless to buy more cars a day, than the capacity
s.t. RedundantConstraint1{d in Days}:
    sum{c in Cars} buy[d,c] <= garagecapacity;
## It is not advantageous to buy anything on the last day
s.t. RedundantConstraint2 {c in Cars}:
    buy[nDays,c] = 0;

# Objective funtction

## I want to maximize my budget in the end
maximize FinalBudget: startbudget + sum {d in Days,c in Cars} price[d,c]*(sell[d,c]-buy[d,c]);


solve;

for {d in Days}
{
    printf "Day %2d:\n",d;
    printf "\tBUY:";
    for{c in Cars : buy[d,c]!=0}
        printf " %s(%d)",c,buy[d,c];
    printf "\n";
    printf "\tSELL:";
    for{c in Cars : sell[d,c]!=0}
        printf " %s(%d)",c,sell[d,c];
    printf "\n\t--------------------\n";
    printf "\tGARAGE [%d/%d]:", sum{dd in 1..d, c in Cars} (buy[dd,c]-sell[dd,c]),garagecapacity;
    for{c in Cars : sum{dd in 1..d} (buy[dd,c]-sell[dd,c])!= 0}
       printf " %s(%d)",c,sum{dd in 1..d} (buy[dd,c]-sell[dd,c]);
    printf "\n";
    printf "\tBUDGET: %d", startbudget+sum{dd in 1..d, c in Cars} price[dd,c]*(sell[dd,c]-buy[dd,c]);
    printf "\n\n";    
}
