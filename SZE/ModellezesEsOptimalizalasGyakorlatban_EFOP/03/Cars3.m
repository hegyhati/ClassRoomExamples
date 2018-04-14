/*

Kezdeti penz: 200000
Garazsok szama: 4 (ejszakara csak ott maradhatnak)

Akar tobb nappal is mukodjon.

            1       2       3       4       5
Wartburg    60000   65000   61000   66000   60000
Lada        50000   55000   63000   60000   52000
Kispolski   30000   32000   33000   30000   27000
Trabant     70000   65000   77000   85000   100000
Skoda       65000   70000   75000   90000   70000

Cel: het vegere minel tobb penzunk legyen.

*/
param nDays;
set Days:=1..nDays;
set Cars;
param price{Cars,Days};
param initialbudget;
param garagecount;

var buy{Cars,Days} integer;

s.t. MustHavePositiveBalanceAtTheEndOfEachDay{d in Days}:
    initialbudget - sum{d2 in 1..d, c in Cars} buy[c,d2]*price[c,d2] >= 0;
    
s.t. CannotHaveMoreCarsThanGarageSpace{d in Days}:
    sum{d2 in 1..d, c in Cars} buy[c,d2] <= garagecount;


s.t. CannotSellWhatWeDontHave {d in Days, c in Cars}:
    sum{d2 in 1..d} buy[c,d2] >= 0;

maximize endbudget:
    initialbudget - sum{d in Days, c in Cars} buy[c,d]*price[c,d]
    ;

solve;

for{d in Days}{
    printf "Day %d\n",d;
    printf "\tSell: ";
    for{c in Cars:buy[c,d]<0}
        printf "%s(%d) ",c,-buy[c,d];
    printf "\n\tBuy: ";
    for{c in Cars:buy[c,d]>0}
        printf "%s(%d) ",c,buy[c,d];
    printf "\n";
    printf "\tBudget: %d\n", initialbudget - sum{d2 in 1..d, c in Cars} buy[c,d2]*price[c,d2];
}

data;

param nDays:= 5;
set Cars:= Wartburg Lada Kispolski Trabant Skoda;

param price:
            1       2       3       4           5 :=
Wartburg    60000   65000   61000   66000       60000
Lada        50000   55000   63000   60000       52000
Kispolski   30000   32000   33000   30000       27000
Trabant     70000   65000   77000   85000       100000
Skoda       65000   70000   75000   90000       70000
;

param initialbudget:=200000;
param garagecount:=4;
