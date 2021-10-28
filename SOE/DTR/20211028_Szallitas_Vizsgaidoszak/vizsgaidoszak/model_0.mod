set Targyak;
param szukseges_ora{Targyak}; # ora
param vizsganap{Targyak}; 
set Napok;
param szabadido{Napok}; # ora

var tanulok{Napok,Targyak} >= 0; #ora

# Egy nap nem tanulhatok tobbet a szabadidomnel
s.t. Szabadido_betartas{n in Napok}:
    sum{t in Targyak} tanulok[n,t] <= szabadido[n];

# Egyik targybol sem szabad megbukni
s.t. Felkeszules_korlatozas{t in Targyak}:
    sum{n in Napok} tanulok[n,t]>= szukseges_ora[t];

# Ne tanuljunk vizsga utan
s.t. Kesei_tanulas_tiltasa{n in Napok, t in Targyak : n >= vizsganap[t]}:  
    tanulok[n,t]=0;

minimize Osszes_tanulas:
    sum{n in Napok, t in Targyak} tanulok[n,t];

solve;

for {n in Napok}
{
    printf "Nap %d:\n",n;
    for {t in Targyak : n == vizsganap[t]}
        printf " - Vizsga %s-bol\n",t;
    for {t in Targyak: tanulok[n,t]>0}:
        printf " - Tanulok %s-re %g orat.\n",t,tanulok[n,t];
    }

