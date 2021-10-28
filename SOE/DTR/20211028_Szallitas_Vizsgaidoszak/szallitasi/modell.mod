set Gyarak;
set Kocsmak;
param igeny{Kocsmak};
param keszlet{Gyarak};
param uthossz{Gyarak,Kocsmak};

var szallit{Gyarak,Kocsmak} >= 0;

# Keszlet erejeig szallithatunk el
s.t. Keszlet_korlatozas{gy in Gyarak}:
    sum{k in Kocsmak} szallit[gy,k] <= keszlet[gy];

# Igenyeket ki kell elegiteni
s.t. Igeny_korlatozas{k in Kocsmak}:
    sum{gy in Gyarak} szallit[gy,k] >= igeny[k];

minimize Szallitasi_koltseg:
    sum{gy in Gyarak, k in Kocsmak} 
        szallit[gy,k] * uthossz[gy,k]
;

solve;

for {gy in Gyarak}
{
    printf "%s:\n",gy;
    for {k in Kocsmak: szallit[gy,k] > 0}
        printf " - %s (%g)\n",k,szallit[gy,k];
}
