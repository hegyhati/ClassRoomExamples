set Cars;
param nDays;
set Days := 1..nDays;
param price{Days,Cars};
param inital_money;

var sell_buy{Days,Cars} integer; # sell-buy
var money{Days union {0}} >= 0;
var car{Days union {0}, Cars} >=0 integer;


s.t. Initial_money:
    money[0] = inital_money;
    
s.t. Set_money{d in Days}:
    money[d] = money[d-1] 
               + sum{c in Cars} price[d,c] * sell_buy[d,c]
    ;

s.t. Initial_cars{c in Cars}:
    car[0,c] = 0;

s.t. Set_cars{c in Cars, d in Days}:
    car[d,c] = car[d-1,c] - sell_buy[d,c];

maximize Money_at_end: money[nDays];

solve;

for {d in Days}
{
    printf "Day %d: %g\n",d,money[d];
    for {c in Cars : sell_buy[d,c] != 0}:
        printf " - %s %g\n",c,sell_buy[d,c];
}
