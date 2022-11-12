set Barracks;
set Depots;
param fix_cost{Depots} >= 0; # $/l
param prop_cost{Depots} >= 0; # $
param demand{Barracks} >=0; # l
param connected{Depots,Barracks} binary; # -

set Connections := setof {b in Barracks, d in Depots : connected[d,b]==1} (d,b);

param M := sum{b in Barracks} demand[b];

var build{Depots} binary; # -
var size{Depots} >= 0; # l
var transport{Connections} >= 0; # l

s.t. Satisfy_demand{b in Barracks}:
    sum{(d,b) in Connections} transport[d,b] >= demand[b];

s.t. Set_size_variable{d in Depots}:
    size[d] = sum{(d,b) in Connections} transport[d,b];

s.t. Omly_use_builded_depots{d in Depots}:
    size[d] <= M * build[d];

minimize Objective:
    sum{d in Depots} build[d] * fix_cost[d] + size[d] * prop_cost[d];

end;
