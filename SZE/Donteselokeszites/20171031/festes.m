set Emberek;
set Munkak;

param nSzakasz;
set Szakaszok:= 1..nSzakasz;

param tav{Emberek,Munkak};

# Valtozok
var csinal{Emberek,Szakaszok,Munkak}, binary;
var hantaskm{0..nSzakasz} >=0;
var alapkm{0..nSzakasz} >=0;
var festeskm{0..nSzakasz} >= 0;
var lakkkm{0..nSzakasz} >=0;


# Korlatozasok

# Minden folyamaton minden szakaszban legalabb 1 ember dolgozik

s.t. MindigMindentCsinalValaki{m in Munkak, sz in Szakaszok}:
    sum{e in Emberek} csinal[e,sz,m] >= 1;


# Egy ember minden szakaszban csak 1 dolgot csinalhat
s.t. EgyEmberEgyszerreCsakEgyet{e in Emberek, sz in Szakaszok}:
    sum{m in Munkak} csinal[e,sz,m] = 1;


# Max annyit haladunk, amennyit a feladathoz rendelt emberek 100 perc alatt tudnak

s.t. HantasInit: hantaskm[0]=0;
s.t. HantasHaladas{sz in Szakaszok}:
    hantaskm[sz] <= hantaskm[sz-1] + sum{e in Emberek} csinal[e,sz,'hantas']*tav[e,'hantas']*100/60;

s.t. alapInit: alapkm[0]=0;
s.t. alapHaladas{sz in Szakaszok}:
    alapkm[sz] <= alapkm[sz-1] + sum{e in Emberek} csinal[e,sz,'alap']*tav[e,'alap']*100/60;

s.t. festesInit: festeskm[0]=0;
s.t. festesHaladas{sz in Szakaszok}:
    festeskm[sz] <= festeskm[sz-1] + sum{e in Emberek} csinal[e,sz,'festes']*tav[e,'festes']*100/60;

s.t. lakkInit: lakkkm[0]=0;
s.t. lakkHaladas{sz in Szakaszok}:
    lakkkm[sz] <= lakkkm[sz-1] + sum{e in Emberek} csinal[e,sz,'lakk']*tav[e,'lakk']*100/60;

# hantas es a lakk kozott max 2 km lehet minden szakasz vegen
s.t. HantasNemMehetTulMesszeALakkozastol{sz in Szakaszok}:
    hantaskm[sz]<=lakkkm[sz]+2;


# Nem elozhetik be egymast a folyamatok egyik szakaszban sem
s.t. AlapozasNemEloz{sz in Szakaszok}:
    alapkm[sz]<=hantaskm[sz];
s.t. FestesNemEloz{sz in Szakaszok}:
    festeskm[sz]<=alapkm[sz];
s.t. LakkozasNemEloz{sz in Szakaszok}:
    lakkkm[sz]<=festeskm[sz];

#Celfuggveny

# lakkozas minel messzebb jusson a vegen
maximize TeljesenKeszenVan: lakkkm[nSzakasz];

solve;

for {sz in Szakaszok}
{
    printf "%d. szakasz:\n",sz;
            printf "\t%4s %4f -> %4f: ", "hantas",hantaskm[sz-1],hantaskm[sz];
            for {e in Emberek: csinal[e,sz,'hantas']=1}
                printf "%s ",e;
            printf "\n";
            
            printf "\t%4s %4f -> %4f: ", "alap",alapkm[sz-1],alapkm[sz];
            for {e in Emberek: csinal[e,sz,'alap']=1}
                printf "%s ",e;
            printf "\n";        
            
            printf "\t%4s %4f -> %4f: ", "festes",festeskm[sz-1],festeskm[sz];
            for {e in Emberek: csinal[e,sz,'festes']=1}
                printf "%s ",e;
            printf "\n";
            
            printf "\t%4s %4f -> %4f: ", "lakk",lakkkm[sz-1],lakkkm[sz];
            for {e in Emberek: csinal[e,sz,'lakk']=1}
                printf "%s ",e;
            printf "\n";
    
}
