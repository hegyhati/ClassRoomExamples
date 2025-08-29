set Cars;
param nDays;
set Days := 1..nDays;

param budget;
param garagespace;
param price{Cars,Days};

var buy{Cars,Days}, integer, >=0;
var sell{Cars,Days}, integer, >=0;
var buyorsell{Cars,Days}, binary;


s.t. Buyorsell1{c in Cars, d in Days}:
    buy[c,d]<=buyorsell[c,d]*garagespace;
s.t. Buyorsell2{c in Cars, d in Days}:
    sell[c,d]<=(1-buyorsell[c,d])*garagespace;

s.t. DontSpendMoreThanWhatYouHave{d in Days}:
    budget + sum{d2 in 1..d,c in Cars}(price[c,d2]*(sell[c,d2]-buy[c,d2])) >= 0;

s.t. DontSellCarsYouDontHave{d in Days, c in Cars}:
    sum{d2 in 1..d}(buy[c,d2]-sell[c,d2]) >= 0;

s.t. DontExceedGarageSpace{d in Days}:
    sum{d2 in 1..d,c in Cars}(buy[c,d2]-sell[c,d2]) <= garagespace;

maximize FinalBudget:
    budget + sum{d in 1..nDays,c in Cars}(price[c,d]*(sell[c,d]-buy[c,d]));

solve;

for {d in Days}
{
    printf "Day %d\n",d;
    
    for {c in Cars : sell[c,d]!=0}
        printf "\t Sell %d %s.\n",sell[c,d],c;
    for {c in Cars : buy[c,d]!=0}
        printf "\t Buy %d %s.\n",buy[c,d],c; 
}


data;

param garagespace:=4;
param budget := 300;

set Cars:= Audi Mercedes BMW;
param nDays := 5;
param price:        1   2   3   4   5 :=
        Audi        110 105 115 120 125
        Mercedes    90  95  85  80  90
        BMW         120 128 115 118 120
        ;


end;
