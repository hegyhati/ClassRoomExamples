set Termek;
set Hozzavalok;
param ar{Termek};
param hasznal{Termek,Hozzavalok} default 0;
param keszlet{Hozzavalok};

var elad{Termek} >= 0;

s.t. Keszlet_betartasa{hozzavalo in Hozzavalok}:
    sum{termek in Termek} elad[termek] * hasznal[termek,hozzavalo] 
    <= keszlet[hozzavalo];

maximize Profit:
    sum{termek in Termek} elad[termek] * ar[termek]
;

solve;

for {termek in Termek: elad[termek] != 0}
    printf "%s: %g \n",termek,elad[termek];

data;

set Termek := Krudy kisfroccs nagyfroccs hosszulepes kisvadasz nagyvadasz trio dizel;
set Hozzavalok := feherbor szoda vorosbor kola sor;
param ar :=
    kisfroccs   150
    nagyfroccs  300
    hosszulepes 200
    Krudy       300
    kisvadasz   200
    nagyvadasz  400      
    trio        220
    dizel       300
    ;

param hasznal: 
                feherbor    szoda   vorosbor    kola    sor:=
    kisfroccs   1           1       .           .       .
    nagyfroccs  2           1       .           .       .
    Krudy       9           1       .           .       .
    hosszulepes 1           2       .           .       .
    kisvadasz   .           .       1           1       .
    nagyvadasz  .           .       2           1       .
    trio        .           1       1           1       .
    dizel       .           .       .           1       1
    ;

param keszlet :=
    feherbor 1000
    szoda    1500
    vorosbor 500
    kola     500
    sor      1000
    ;
end;
