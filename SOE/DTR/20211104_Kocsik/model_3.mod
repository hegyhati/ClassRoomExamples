set Cars;
param nDays;
set Days := 1..nDays;
param price{Days,Cars};
param inital_money;

var sell_buy{Days,Cars} integer; # sell-buy

s.t. Dont_overspend{d in Days}:
    0 <= inital_money 
        + sum {pd in 1..d, c in Cars} 
            price[pd,c] * sell_buy[pd,c]
            ;

s.t. Dont_sell_what_you_dont_have{d in Days, c in Cars}:
    0 >= sum{pd in 1..d} sell_buy[pd,c];

maximize Money_at_end:
    inital_money 
        + sum {pd in Days, c in Cars} 
            price[pd,c] * sell_buy[pd,c]
            ;
