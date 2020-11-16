param nDays >=0, integer;
set Days := 1..nDays;

param arrive{Days} >= 0;

set Orders;
param need{Orders};
param day{Orders};
param profit{Orders};

var do{Orders} binary;
var amount{Days union {0}} >= 0; 

s.t. InitialAmount:
    amount[0]=0;

s.t. NextDay{d in Days};
    amount[d] = amount[d-1] + arrive[d] - sum{o in Orders: day[o]==d} need[o]*do[o];

maximize Profit: sum{o in Orders} profit[o]*do[o];
