set Cars;
param nDays;
set Days := 1..nDays;
param price{Days,Cars};
param inital_money;

var sell{Days,Cars} >=0 integer;
var buy {Days,Cars} >=0 integer;

s.t. Dont_overspend{d in Days}:
    0 <= inital_money 
        + sum {pd in 1..d, c in Cars} 
            price[pd,c] * (sell[pd,c] - buy[pd,c])
            ;

s.t. Dont_sell_what_you_dont_have{d in Days, c in Cars}:
    sell[d,c] <= sum{pd in 1..d} (buy[pd,c]-sell[pd,c])
                        ;

maximize Money_at_end:
    inital_money 
        + sum {pd in Days, c in Cars} 
            price[pd,c] * (sell[pd,c] - buy[pd,c])
            ;
