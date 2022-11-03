set Currencies;
set Days;

param dollar_value{Currencies,Days};
param initial_money{Currencies};

var exchange{Currencies,Currencies,Days} >= 0;
var balance{Currencies,Days} >= 0;

s.t. set_balance_first_day {c in Currencies}:
    balance[c,1] = initial_money[c] 
            + sum {cc in Currencies : cc != c} exchange[cc,c,1] / dollar_value[cc,1] * dollar_value[c,1]
            - sum {cc in Currencies : cc != c} exchange[c,cc,1] 
    ;

s.t. set_balance_other_days {c in Currencies, d in Days: d != 1}:
    balance[c,d] = balance[c,d-1]
            + sum {cc in Currencies : cc != c} exchange[cc,c,d] / dollar_value[cc,d] * dollar_value[c,d]
            - sum {cc in Currencies : cc != c} exchange[c,cc,d] 
    ;

maximize Dollars:
    balance['USD',card(Days)]
;
