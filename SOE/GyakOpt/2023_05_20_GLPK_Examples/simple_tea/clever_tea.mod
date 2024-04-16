set Farms;
param supply{Farms} >= 0;

set Markets;
param demand{Markets} >= 0;

param distance{Farms,Markets} >= 0;

var transport{Farms,Markets} >= 0;

s.t. Supply_can_not_be_overreached{f in Farms}:
    sum{m in Markets} transport[f,m] <= supply[f] ;

s.t. Demand_must_be_met{m in Markets}:
    sum{f in Farms} transport[f,m] >= demand[m];

minimize Transportation_cost:
    sum{f in Farms, m in Markets} distance[f,m] * transport[f,m];

solve;

for {f in Farms, m in Markets: transport[f,m] > 0}
    printf "%s -> %s : %g \n", f, m, transport[f,m] ;