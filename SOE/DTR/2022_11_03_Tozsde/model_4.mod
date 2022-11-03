set Currencies;

param nDays;
set Days := 1..nDays;

param dollar_value{Currencies,Days};
param initial_money{Currencies};
param final_currency symbolic in Currencies;

var exchange{c in Currencies,cc in Currencies,Days : cc!= c} >= 0;
var balance{Currencies,Days union {0} } >= 0;

s.t. set_initial_balance{c in Currencies}:
    balance[c,0] = initial_money[c];

s.t. set_balance_other_days {c in Currencies, d in Days}:
    balance[c,d] = balance[c,d-1]
            + sum {cc in Currencies : cc != c} exchange[cc,c,d] / dollar_value[cc,d] * dollar_value[c,d]
            - sum {cc in Currencies : cc != c} exchange[c,cc,d]     ;

maximize Dollars:
    balance[final_currency,nDays]
;

solve;

for {d in Days} 
{
    printf "Day %d:\n", d;
    for {c in Currencies, cc in Currencies : exchange[c,cc,d] != 0}
        printf " %g %s -> %g %s\n",exchange[c,cc,d],c, exchange[c,cc,d] / dollar_value[c,d] * dollar_value[cc,d], cc;
    
    printf "\n";
    for {c in Currencies}
        printf " - %s: %g\n", c, balance[c,d];
    
}

end;
