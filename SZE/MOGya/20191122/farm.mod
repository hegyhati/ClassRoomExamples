set Farmers;
param price{Farmers};
param farm{Farmers};
param ready{Farmers};
param initial;
param nDays;

set Days:=1..nDays;

var moneyMorning{Days} >=0;
var moneyAfterPurchase{Days} >=0;
var buy{Farmers,Days} >= 0, integer;
var farmers{Farmers,Days} >=0, integer;

s.t. InitialMoney:
    moneyMorning[1]=initial;

s.t. MorningPurchase{d in Days}:
    moneyAfterPurchase[d]=moneyMorning[d]-sum{f in Farmers} buy[f,d]*price[f];

s.t. NextDayMoney{d in Days: d>1}:
    moneyMorning[d]=moneyAfterPurchase[d-1]+sum{f in Farmers} farmers[f,d-1]*farm[f];

s.t. FarmerCountInitial{f in Farmers, d in Days: d<=ready[f]}:
    farmers[f,d]=0;

s.t. FarmerGrowth{f in Farmers, d in Days: d>ready[f]}:
    farmers[f,d]=farmers[f,d-1]+buy[f,d-ready[f]];

maximize FinalMoney: moneyAfterPurchase[nDays];

solve;

for{d in Days:d!=nDays}
{
    printf "\nDay %2d: %g -> %g -> %g\n",d, moneyMorning[d],moneyAfterPurchase[d],moneyMorning[d+1];
    printf "%15s|",""; for{f in Farmers} printf "%10s|",f; printf "\n";
    printf "     ----------+"; for {f in Farmers} printf "----------+"; printf "\n";
    printf "%15s|","Buy "; for{f in Farmers} printf "%9d |",buy[f,d]; printf "\n";
    printf "%15s|","Cost "; for{f in Farmers} printf "%9d |",buy[f,d]*price[f]; printf " TOTAL: -%d\n", sum{f in Farmers } buy[f,d]*price[f];
    printf "     ----------+"; for {f in Farmers} printf "----------+"; printf "\n";
    printf "%15s|","Working "; for{f in Farmers} printf "%9d |",farmers[f,d]; printf "\n";
    for{{0}:d!=1}{
        printf "%15s|","(New) "; for{f in Farmers} printf "%9d |",farmers[f,d]-farmers[f,d-1]; printf "\n";
    }
    printf "%15s|","Farmed "; for{f in Farmers} printf "%9d |",farmers[f,d]*farm[f]; printf " TOTAL: %d\n", sum{f in Farmers } farmers[f,d]*farm[f];
    printf "     ----------+"; for {f in Farmers} printf "----------+"; printf "\n";
}

printf "\n\n================================================\n\n";
printf "Final money on the morning of the %dth day: %d\n\n",nDays, moneyMorning[nDays];
