set University := Sopron Gyor Budapest Veszprem Pecs Szeged;
set Brewery := Sopron Pecs Nagykanizsa Budapest;

param production_hl :=
    Sopron       100
    Pecs          80
    Nagykanizsa  150
    Budapest     200;

param demand_hl := 
    Sopron   130
    Gyor       1
    Budapest 170
    Veszprem  30
    Pecs      40
    Szeged    45;

param distance_km : Sopron Gyor Budapest Veszprem Pecs Szeged :=
    Sopron 0 96 216 149 397 383
    Pecs 397 332 239 192 0 189
    Nagykanizsa 161 195 211 154 140 374
    Budapest 216 121 0 115 239 175;
    
param beer_density_kg_per_l := 1.01; 
param transportation_cost_HUF_per_kg_per_km := 0.02; 