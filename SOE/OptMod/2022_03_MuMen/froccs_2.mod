set Froccs;
param borkeszlet;
param szodakeszlet;
param borhasznalat{Froccs};
param szodahasznalat{Froccs};
param ar{Froccs};

var adag{Froccs} >= 0;

s.t. Bor_keszlet_korlatozas:
sum{f in Froccs} borhasznalat[f] * adag[f] <= borkeszlet;

s.t. Szoda_keszlet_korlatozas:
sum{f in Froccs} szodahasznalat[f] * adag[f] <= szodakeszlet;

maximize Bevetel:
sum{f in Froccs} ar[f] * adag[f];

end;