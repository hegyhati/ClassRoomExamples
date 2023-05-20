set Farms;
param supply{Farms} >= 0; # kg

set Markets;
param demand{Markets} >= 0; # kg

param distance{Farms,Markets} >= 0; # km

set Vehicles;
param weight{Vehicles} >= 0; # kg
param capacity{Vehicles} >= 0; # kg

param transport_cost default 1; # Ft/kg/km


var travel{Farms,Markets,Vehicles} >= 0, integer; # pcs
var transport{Farms,Markets} >= 0; # kg

s.t. Supply_can_not_be_overreached{f in Farms}:
    sum{m in Markets} transport[f,m] <= supply[f] ;

s.t. Demand_must_be_met{m in Markets}:
    sum{f in Farms} transport[f,m] >= demand[m];

s.t. Vehicle_capacity{f in Farms, m in Markets}:
    # transported amount can not be more than the capacity of vehicles in that route
    # transported amount <= capacity of vehicles in that route
    # transport[f,m] <= capacity of vehicles in that route
    transport[f,m] <= sum {v in Vehicles} capacity[v] * travel[f,m,v];


/*
minimize Transportation_cost:
    # cost of tea transportation
    sum{f in Farms, m in Markets} distance[f,m] * transport[f,m] * transport_cost
    # cost of vehicle travel
    sum{f in Farms, m in Markets, v in Vehicles} distance[f,m] * weight[v] * travel[f,m,v] * 2 * transport_cost 
    ;
*/


minimize Transportation_cost:
    transport_cost * sum {f in Farms, m in Markets} (
        # cost of tea transportation
        transport[f,m]
        # cost of vehicle travel
        + 2 * sum{v in Vehicles} weight[v] * travel[f,m,v] 
    )
    ;

# var totalcost{Farm,Market} >= 0;
# s.t. Set_total_cost {f in Farms, m in Markets}:
#     totalcost[f,m] = transport_cost * (transport[f,m] + 2 * sum{v in Vehicles} weight[v] * travel[f,m,v])
# 
# minimize Transportation_cost:
#     sum{f in Farms, m in Markets} totalcost[f,m];



solve;


for {f in Farms, m in Markets: transport[f,m] > 0}
{
    printf "%s -> %s : %g  with ", f, m, transport[f,m] ;
    for {v in Vehicles : travel[f,m,v] != 0 }
        printf "%d %s ",travel[f,m,v],v;
    printf "\n";
}