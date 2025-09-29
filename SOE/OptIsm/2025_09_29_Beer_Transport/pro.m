set Brewery;
set University;

param distance_km{Brewery,University} >= 0; 
param production_hl{Brewery} >= 0; 
param demand_hl{University} >= 0; 
param beer_density_kg_per_l >= 0; 
param transportation_cost_HUF_per_kg_per_km >= 0; 

set Trucktype;
param truck_weight_t{Trucktype} >= 0;
param truck_carry_capacity_t{Trucktype} >=0;

var transport_hl{Brewery,University} >= 0; 
var trips{Brewery,University,Trucktype} >=0, integer;

s.t. Brewery_capacity_hl {b in Brewery}:
    sum{u in University} transport_hl[b,u] <= production_hl[b];

s.t. University_demand_hl {u in University}:
    sum{b in Brewery} transport_hl[b,u] >= demand_hl[u];

s.t. Enough_transport_capacity_for_transported_beer_t{b in Brewery, u in University}:
    beer_density_kg_per_l * transport_hl[b,u] / 10 
    <= 
    sum {t in Trucktype} trips[b,u,t] * truck_carry_capacity_t[t];

minimize Transportation_cost_HUF:
    sum{b in Brewery, u in University}
    transportation_cost_HUF_per_kg_per_km * distance_km[b,u] * (
        beer_density_kg_per_l * 100 * transport_hl[b,u]  
        + sum {t in Trucktype} 2 * trips[b,u,t] * truck_weight_t[t] * 1000
    )
;

solve;

printf "\nCost: %g\n\n", Transportation_cost_HUF;

for{b in Brewery, u in University : transport_hl[b,u] > 0}
{
    printf "%s --%g[",b,transport_hl[b,u]; 
    for {t in Trucktype : trips[b,u,t] != 0} {
        printf " %s:%d ", t, trips[b,u,t];
    }
    printf "]--> %s \n",u;
}

end;