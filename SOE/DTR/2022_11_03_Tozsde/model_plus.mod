set Currencies;
set Exchanges := setof{c in Currencies, cc in Currencies: c!= cc} (c,cc);

param nDays;
set Days := 1..nDays;

param account_fee_in_dollars;

param dollar_value{Currencies,Days};
param initial_money{Currencies};
param final_currency symbolic in Currencies;

param M := 99999;

var exchange{Exchanges, Days} >= 0;
var balance{Currencies,Days union {0} } >= 0;
var open_account{Currencies} binary;

s.t. set_initial_balance{c in Currencies}:
    balance[c,0] = initial_money[c];

s.t. set_balance_other_days {c in Currencies, d in Days}:
    balance[c,d] = balance[c,d-1]
            + sum {(c,cc) in Exchanges} exchange[cc,c,d] / dollar_value[cc,d] * dollar_value[c,d]
            - sum {(c,cc) in Exchanges} exchange[c,cc,d]     
            ;
s.t. only_use_open_accounts_1 {(c,cc) in Exchanges}:
    sum{d in Days} (exchange[c,cc,d] + exchange[cc,c,d]) <= M * open_account[c];

s.t. only_use_open_accounts_2 {(c,cc) in Exchanges}:
    sum{d in Days} (exchange[c,cc,d] + exchange[cc,c,d]) <= M * open_account[cc];

maximize Dollars:
    balance[final_currency,nDays] - sum{c in Currencies} open_account[c] * account_fee_in_dollars
;

solve;

for {d in Days} 
{
    printf "Day %d:\n", d;
    for { (c,cc) in Exchanges : exchange[c,cc,d] != 0}
        printf " %g %s -> %g %s\n",exchange[c,cc,d],c, exchange[c,cc,d] / dollar_value[c,d] * dollar_value[cc,d], cc;
    
    printf "\n";
    for {c in Currencies}
        printf " - %s: %g\n", c, balance[c,d];
    
}

end;
