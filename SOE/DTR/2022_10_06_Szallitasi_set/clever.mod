set Sources;
param capacity{Sources};

set Destinations;
param demand{Destinations};

param distance{Sources,Destinations};


var transport{Sources,Destinations} >= 0;

s.t. Capacity{s in Sources}:
    sum{d in Destinations} transport[s,d] <= capacity[s];

s.t. Demand{d in Destinations}:
    sum{s in Sources} transport[s,d] >= demand[d];

minimize TransportCost:
    sum{s in Sources, d in Destinations} distance[s,d] * transport[s,d];

