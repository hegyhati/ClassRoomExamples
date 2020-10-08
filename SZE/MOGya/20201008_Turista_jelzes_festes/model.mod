set Emberek;
set Feladatok;
param megelozo{Feladatok} symbolic within Feladatok;
param utolsofeladat symbolic within Feladatok;

param oraszam;
set Orak := 1..oraszam;

param sebesseg{Emberek,Feladatok} >= 0; # km/h
param hasznosarany <=1 >=0;

var csinal{Orak,Emberek,Feladatok} binary;
var meddig{Orak union {0},Feladatok} >= 0; # redundans / fixed, km

# 2. Egy ember egy adott oraban csak egy dolgot vegezhet
s.t. EgySzerreEgyDolgotCsinal{e in Emberek, o in Orak}:
    sum{f in Feladatok} csinal[o,e,f] <= 1;

# 4. redundans valtozok kiszamolasa
s.t. ElejenNullarolIndulMind{f in Feladatok}:
    meddig[0,f]=0;

s.t. MeddigJutottEl{o in Orak, f in Feladatok}:
    meddig[o,f]<=meddig[o-1,f]+sum{e in Emberek} csinal[o,e,f]*sebesseg[e,f]*hasznosarany;

# 1. Feladatok nem elozhetik be egymast
s.t. NeElozzekBeEgymast{o in Orak, f in Feladatok}:
    meddig[o,f] <= meddig[o,megelozo[f]];
    
# 5. Vege meg eleje kozott nem lehet 1 km-nel tobb
# 6. Mindent mindig csinaljon valaki

maximize Teljesenmegvan: meddig[oraszam,utolsofeladat];

solve;

for{ o in Orak} {
    printf "%d. ora:\n",o;
    for{f in Feladatok}{
        printf "\t%14s (%.2f -> %.2f):",f,meddig[o-1,f],meddig[o,f];
        for{e in Emberek : csinal[o,e,f]==1}
            printf " %s",e;
        printf "\n";
    }
    printf "\n";
}


data;

set Emberek :=  Andi Bela Cili Dani Elek Feri Gabi Heni Ili;

set Feladatok :=  hantas alapfestes jelzesfestes lakkozas;

param megelozo :=
    hantas       hantas # UGLY FIX LATER
    alapfestes   hantas
    jelzesfestes alapfestes
    lakkozas     jelzesfestes
;

param utolsofeladat := lakkozas;

param oraszam := 8;

param hasznosarany := 0.8;

param sebesseg: 
	    hantas	alapfestes	jelzesfestes	lakkozas:=
Andi	5.49	8.14	    8.46    	    7.79
Bela	5.84	7.76	    5.82    	    8.93
Cili	5.74	7.68	    6.43    	    7.55
Dani	8.20	5.81	    8.09    	    8.76
Elek	7.39	6.62	    5.81    	    7.68
Feri	5.28	6.70	    5.10    	    5.90
Gabi	7.46	7.24	    5.82    	    7.12
Heni	7.35	7.29	    7.01    	    7.70
Ili	    7.22	6.05	    5.38    	    5.17
;
