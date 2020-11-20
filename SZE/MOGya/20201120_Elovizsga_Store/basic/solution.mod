set ProductGroups;
param space{ProductGroups} >=0;

param nRows >= 1, integer;
set Rows := 1..nRows;

param cachierCount >=1, <=nRows, integer;
param cachierWidth >=0;

var place{ProductGroups,Rows} binary;
var max_row_length;

s.t. PutEveryThing{p in ProductGroups}:
    sum{r in Rows} place[p,r]=1;

s.t. MaxRowLength1{r in Rows: r <= cachierCount}:
    sum{p in ProductGroups} place[p,r]*space[p] <= max_row_length - cachierWidth;

s.t. MaxRowLength2{r in Rows: r > cachierCount}:
    sum{p in ProductGroups} place[p,r]*space[p] <= max_row_length;

minimize BuildingLength: max_row_length;

solve;

printf "%f\n",BuildingLength;


