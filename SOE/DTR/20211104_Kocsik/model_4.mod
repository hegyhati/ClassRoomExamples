set Cars;
param nDays;
set Days := 1..nDays;
param price{Days,Cars};
param inital_money;

var sell_buy{Days,Cars} integer; # sell-buy
var money{Days} >= 0;


s.t. Initial_money:
    money[1] = inital_money 
               + sum{c in Cars} price[1,c] * sell_buy[1,c]
    ;

s.t. Set_money{d in Days : d != 1}:
    money[d] = money[d-1] 
               + sum{c in Cars} price[d,c] * sell_buy[d,c]
    ;

s.t. Dont_sell_what_you_dont_have{d in Days, c in Cars}:
    0 >= sum{pd in 1..d} sell_buy[pd,c];

maximize Money_at_end: money[nDays];

solve;

for {d in Days}
{
    printf "Day %d: %g\n",d,money[d];
    for {c in Cars : sell_buy[d,c] != 0}:
        printf " - %s %g\n",c,sell_buy[d,c];
}
