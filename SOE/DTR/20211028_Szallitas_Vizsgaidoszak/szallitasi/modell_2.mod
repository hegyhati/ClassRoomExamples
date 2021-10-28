set Gyarak;
set Kocsmak;
set Visszonylatok := Gyarak cross Kocsmak;
param igeny{Kocsmak};
param keszlet{Gyarak};
param uthossz{Visszonylatok};

var szallit{Visszonylatok} >= 0;

# Keszlet erejeig szallithatunk el
s.t. Keszlet_korlatozas{gy in Gyarak}:
    sum{k in Kocsmak} szallit[gy,k] <= keszlet[gy];

# Igenyeket ki kell elegiteni
s.t. Igeny_korlatozas{k in Kocsmak}:
    sum{gy in Gyarak} szallit[gy,k] >= igeny[k];

minimize Szallitasi_koltseg:
    sum{(gy,k) in Visszonylatok} 
        szallit[gy,k] * uthossz[gy,k]
;

solve;

for {gy in Gyarak}
{
    printf "%s:\n",gy;
    for {k in Kocsmak: szallit[gy,k] > 0}
        printf " - %s (%g)\n",k,szallit[gy,k];
}
