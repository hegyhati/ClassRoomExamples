set Supplies;
param supply{Supplies} >= 0;

set Demands;
param demand{Demands} >=0;

param distance{Supplies,Demands} >= 0;

var transport{Supplies,Demands} >= 0;

s.t. Max_Supply{s in Supplies}:
    sum{d in Demands} transport[s,d] <= supply[s];

s.t. Min_Demand{d in Demands}:
    sum{s in Supplies} transport[s,d] >= demand[d];

minimize Transportation_cost:
    sum{s in Supplies, d in Demands} distance[s,d] * transport[s,d];

solve;

for {s in Supplies}
{
    printf "Transport from %s:\n", s;
    for {d in Demands : transport[s,d] != 0 }
        printf "\t-> %s : %g\n",d,transport[s,d];
}


