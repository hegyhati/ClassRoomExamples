set Brewery;
set University;

param distance_km{Brewery,University} >= 0; 
param production_hl{Brewery} >= 0; 
param demand_hl{University} >= 0; 
param beer_density_kg_per_l >= 0; 
param transportation_cost_HUF_per_kg_per_km >= 0; 

var transport_hl{Brewery,University} >= 0; 

s.t. Brewery_capacity {b in Brewery}:
    sum{u in University} transport_hl[b,u] <= production_hl[b];

s.t. University_demand {u in University}:
    sum{b in Brewery} transport_hl[b,u] >= demand_hl[u];

minimize Transportation_cost_HUF:
    sum{b in Brewery, u in University}
    transportation_cost_HUF_per_kg_per_km * beer_density_kg_per_l * 100 * distance_km[b,u] * transport_hl[b,u] 
;

solve;
for{b in Brewery, u in University : transport_hl[b,u] > 0}
{
    printf "%s --%g--> %s \n",b,transport_hl[b,u],u;
}

end;