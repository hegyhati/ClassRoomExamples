set ProductGroups;
param space{ProductGroups} >=0;
param averagePrice{ProductGroups} >=0;
set MustBeTogether within ProductGroups cross ProductGroups;
set MustBeSeparated within ProductGroups cross ProductGroups;

param nRows >= 1, integer;
set Rows := 1..nRows;
param maxRowLength;

param cachierCount >=1, <=nRows, integer;
param cachierWidth >=0;

set CustomerGroups;
param buys{CustomerGroups,ProductGroups} binary;
param count{CustomerGroups} >=0, integer;
param probabilityToBuy{CustomerGroups} >=0, <=1;

set Manipulation := setof{c in CustomerGroups, p in ProductGroups : buys[c,p]==0}(c,p);
var sees{Manipulation} binary;
var place{ProductGroups,Rows} binary;

s.t. PutEveryThingOnARow{p in ProductGroups}:
    sum{r in Rows} place[p,r]=1;

s.t. MaxRowLength{r in Rows}:
    sum{p in ProductGroups} place[p,r]*space[p] <= maxRowLength 
    - if r <=cachierCount then cachierWidth ;

s.t. ProductsOnSameShelf{(p1,p2) in MustBeTogether, r in Rows}:
    place[p1,r]=place[p2,r];

s.t. ProductsOnDifferentShelf{(p1,p2) in MustBeSeparated, r in Rows}:
    place[p1,r]+place[p2,r]<=1;

s.t. IfNoBoughtProductInSameRowThenNotSeen{r in Rows, (c,p) in Manipulation}:
    sees[c,p] <= sum{bp in ProductGroups:buys[c,bp]==1} place[bp,r]
    + (1-place[p,r]);

maximize ManipulatedIncome:
    sum{(c,p) in Manipulation}
    sees[c,p] * averagePrice[p] * probabilityToBuy[c] * count[c];

solve;

printf "%f\n",ManipulatedIncome;

for {r in Rows}{
    printf "Row %d [%f]: ",r,sum{p in ProductGroups:place[p,r]==1} space[p];
    for {p in ProductGroups:place[p,r]==1} printf "%s ",p;
    printf "\n";
}

printf "\n";

for {c in CustomerGroups}{
    printf "%8s buys: ",c;
    for {p in ProductGroups:buys[c,p]==1} printf "%s ",p;
    printf "\n";
    printf "%8s sees: ","";
    for {(c,p) in Manipulation:sees[c,p]==1} printf "%s ",p;
    printf "\n";
    printf "%4s not sees: ","";
    for {(c,p) in Manipulation:sees[c,p]==0} printf "%s ",p;
    printf "\n";
}
