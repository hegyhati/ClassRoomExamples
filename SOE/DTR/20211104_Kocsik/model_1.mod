set Cars;
param nDays;
set Days := 1..nDays;
param price{Days,Cars};
param inital_money;

var sell{Days,Cars} >=0 integer;
var buy {Days,Cars} >=0 integer;

s.t. Dont_overspend{current_day in Days}:
    0 <= inital_money 
        + sum {previous_day in 1..current_day, car in Cars} 
            price[previous_day,car] * 
            (sell[previous_day,car] - buy[previous_day,car])
            ;

s.t. Dont_sell_what_you_dont_have{day in Days, car in Cars}:
    sell[day,car] <= sum{previous_day in 1..day} 
                        (buy[previous_day,car]-sell[previous_day,car])
                        ;

maximize Money_at_end:
    inital_money 
        + sum {previous_day in Days, car in Cars} 
            price[previous_day,car] * 
            (sell[previous_day,car] - buy[previous_day,car])
            ;
