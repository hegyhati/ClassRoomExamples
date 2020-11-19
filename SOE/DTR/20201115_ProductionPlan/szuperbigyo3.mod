param nDays >=0, integer;
set Days := 1..nDays;

set RawMaterials;
param arrive{Days,RawMaterials} >= 0;
param price{RawMaterials} >=0;

set Orders;
param need{Orders,RawMaterials};
param day{Orders};
param profit{Orders};
param hours{Orders};

param maxhours;

param maxstorage >=0;
param maxstorageday >=0, integer;
var do{Orders} binary;

set StorageDayPairs := setof {d1 in Days, d2 in Days: d2>d1 && d2 <= d1 + maxstorageday} (d1,d2);
var storage{RawMaterials, StorageDayPairs} >= 0; 
var throwaway{Days,RawMaterials} >= 0; 
vat buy{d in Days, m in RawMaterials} >=0;

s.t. Initial:
    sum{m in RawMaterials, (0,d2) in StorageDayPairs} storage[m,0,d2]=0;

s.t. NextDay{d in Days, m in RawMaterials};
    sum{(d,d2) in StorageDayPairs} storage[m,d,d2] + throwaway[d,m] = sum{(d1,d) in StorageDayPairs} storage[m,d1,d] + arrive[d,m] - sum{o in Orders: day[o]==d} need[o,m]*do[o] + buy[d,m];
  
s.t. MaxStorage{d in Days, m in RawMaterials}:
  sum{(d1,d2) in StorageDayPairs: d1<=d && d2>d} storage[m,d1,d2] <= maxstorage;

s.t. WordkDayHours{d in Days}:
  sum{o in Orders: day[o]==d} do[o] * hours[o] <= maxhours;

maximize Profit: sum{o in Orders} profit[o]*do[o] - sum {d in Days, m in RawMaterials} buy[m,d]*price[m];


