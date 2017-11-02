set Emberek;
set Szamok;

param nTrackList;
set Tracks:= 1..nTrackList;

param szeret{Emberek,Szamok};

#valtozok

var jatszik{Szamok,Tracks}, binary;
var tancol{Emberek,0..nTrackList}, binary;
var iszik{Emberek,0..nTrackList}, binary;
var alszik{Emberek,0..nTrackList}, binary;

#KOrlatozasok

# Kezdetben mindenki tancos kedvvel jott
s.t. MindenkiTancolvaKezd{e in Emberek}:
    tancol[e,0]=1;

# Egyszerre csak egy szamot jatszhatunk
s.t. EgySzam {t in Tracks}:
    sum{s in Szamok} jatszik[s,t] = 1;


# EGy ember egyszerre csak 1 dolgot
s.t. EgyDolgotCSinal{t in Tracks, e in Emberek}:
    tancol[e,t]+iszik[e,t]+alszik[e,t] = 1;


# Ha szereti a zenet (es meg nem aludt), akkor tancol

s.t. Haszeretiesnemaludtakkortnacol{e in Emberek, t in Tracks}:
    tancol[e,t] >= 1 - 2 * ( 1 -
        sum{sz in Szamok} szeret[e,sz]*jatszik[sz,t] + alszik[e,t-1]);

# Ha nem szereti a zenet, de elobb meg tancolt, akkor iszik

s.t. Haelobbtancoltmostiszikfeltvehogynemszereti{e in Emberek, t in Tracks}:
iszik[e,t] >= 1 - 2 * ( 1 - tancol[e,t-1] + sum{sz in Szamok} szeret[e,sz]*jatszik[sz,t]);


# Ha ne mszereti a zenet, de elobb mar ivott, akkor alszik

s.t. Haelobbivottmostalszikfeltvehogynemszereti{e in Emberek, t in Tracks}:
alszik[e,t] >= 1 - 2 * (1-iszik[e,t-1]+sum{sz in Szamok} szeret[e,sz]*jatszik[sz,t]);

# Aki alszik, alva is marad

s.t. Nemkelfel {e in Emberek, t in Tracks}:
    alszik[e,t]>=alszik[e,t-1];


#celfuggveny

# Minel tobb sort eladni
maximize Sorfogyasztas: sum{e in Emberek, t in Tracks} iszik[e,t];

solve;

for {t in Tracks, sz in Szamok : jatszik[sz,t]}
{
    printf "%d-%s -- ",t,sz;
    for {e in Emberek:szeret[e,sz]}
        printf " %s",e;
    printf "\n\tTancol: ";
    for {e in Emberek: tancol[e,t]=1}
        printf " %s",e;
    printf "\n\tIszik:";
    for {e in Emberek: iszik[e,t]=1}
        printf " %s",e;
    printf "\n\tAlszik:";
    for {e in Emberek: alszik[e,t]=1}
        printf " %s",e;
    printf "\n";
}

printf "\n\n";
for {e in Emberek}
{
    printf "%s:\t%d\n",e,sum{t in Tracks} iszik[e,t];
}
printf "\nSUM:\t%d\n",sum{t in Tracks,e in Emberek} iszik[e,t];
