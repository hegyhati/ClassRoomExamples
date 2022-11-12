set Barracks;
set Depots;
param fix_cost{Depots} >= 0; # $/l
param prop_cost{Depots} >= 0; # $
param demand{Barracks} >=0; # l
param connected{Depots,Barracks} binary; # -

param M := sum{b in Barracks} demand[b];

var build{Depots} binary; # -
var transport{Depots,Barracks} >= 0; # l

s.t. Satisfy_demand{b in Barracks}:
    sum{d in Depots} transport[d,b] * connected[d,b] >= demand[b];

s.t. Omly_use_builded_depots{d in Depots}:
    sum{b in Barracks: connected[d,b] == 1} transport[d,b] <= M * build[d];

minimize Objective:
    sum{d in Depots} build[d] * fix_cost[d] + sum{b in Barracks: connected[d,b] == 1} transport[d,b] * prop_cost[d];

end;
