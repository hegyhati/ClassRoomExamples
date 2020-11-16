param nDays >=0, integer;
set Days := 1..nDays;

param arrive{Days} >= 0;

set Orders;
param need{Orders};
param day{Orders};
param profit{Orders};

var do{Orders} binary;

s.t. ResourceBalance{d in Days};
    sum{o in Orders : day[o]<=d} need[o]*do[o] <= sum{d2 in 1..d} arrive[d2];

maximize Profit: sum{o in Orders} profit[o]*do[o];

