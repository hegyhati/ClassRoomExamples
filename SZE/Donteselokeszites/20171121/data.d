set Mezo := mezo1 mezo2 mezo3 mezo4;
set Malom := malom1 malom2;
set Pek := pek1 pek2 pek3;

param tav1:     malom1  malom2 := #km
        mezo1   201	79
        mezo2   174	143
        mezo3   107	102
        mezo4   130	21
;


param tav2:     pek1    pek2    pek3:= #km
        malom1  184	98	60
        malom2  79	58	159
;

param orlesarany:=0.9;

param teherautokapacitas:=500; #kg

param buza:= # kg
    mezo1   36526
    mezo2   12368
    mezo3   25634
    mezo4   9999
;

param kapacitas:= #kg
    malom1  50000
    malom2  60000
;

param ures_fogyasztas := 10; # l / 100 km
param valtozo_fogyasztas := 0.006; # l / kg / 100 km

param benzinar:= 300; # Ft / 100 km


