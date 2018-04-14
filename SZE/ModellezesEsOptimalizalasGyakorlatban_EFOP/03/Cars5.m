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

Kamat (napi): 5%
Garazsberlet 1 napra: 4000
Maximium tartozas: 200000

Cel: het vegere minel tobb penzunk legyen.

*/
param nDays;
set Days:=1..nDays;
set Cars;
param price{Cars,Days};
param initialbudget;
param garagecount;
param interest;
param garagepriceperday;

var buy{Cars,Days} integer;
var budget{0..nDays} >= 0;
var caringarage{Cars,0..nDays} >= 0;
var loan{Days};
var bankbalance{0..nDays} <= 0, >= -200000;
var rentgarage{Days} >= 0, integer;

s.t. InitializeBudget:
    budget[0]=initialbudget;

s.t. InitializeGarage{c in Cars}:
    caringarage[c,0]=0;

s.t. InitialBankBalande:
    bankbalance[0]=0;

s.t. BalanceChange{d in Days}:
    budget[d]=budget[d-1] - sum{c in Cars} buy[c,d]*price[c,d]+loan[d]-rentgarage[d]*garagepriceperday;

s.t. BankBalanceChange{d in Days}:
    bankbalance[d]=bankbalance[d-1]*(1+interest)-loan[d];

s.t. NoLoansAtTheEnd:
    bankbalance[nDays] = 0;

s.t. CarAvailability{d in Days, c in Cars}:
    caringarage[c,d]=caringarage[c,d-1]+buy[c,d];
    
s.t. CannotHaveMoreCarsThanGarageSpace{d in Days}:
    sum{c in Cars} caringarage[c,d] <= garagecount + rentgarage[d];

maximize endbudget: budget[nDays];

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
    printf "\tBank: %d\n",bankbalance[d-1]*(1+interest);
    printf "\tLoan: %d\n",loan[d];
    printf "\tGarage rent: %d\n",rentgarage[d];
    printf "\tBudget: %d\n", budget[d];
    printf "\tBank: %d\n",bankbalance[d];
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
param interest:=0.05;
param garagepriceperday:=4000;
