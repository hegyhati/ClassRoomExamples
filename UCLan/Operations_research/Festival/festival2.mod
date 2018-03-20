set Bands;
set Festivals;

param performs{Bands,Festivals};

var y{Festivals}, binary;

s.t. BandConstraint {b in Bands}:
    sum{f in Festivals} y[f]*performs[b,f] >=1;

minimize numberofvisitedfestivals: 
    sum{f in Festivals} y[f];

data;

set Bands := a b d c;
set Festivals := f1 f2 f3;

param performs :    f1  f2  f3 :=
            a       1   0   1
            b       1   1   0
            c       1   0   0
            d       0   1   1
            ;    
