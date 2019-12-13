/*
Adottak az alabbi egyuttesek es fesztivalok, illetve hogy melyik egyuttes melyik fesztivalon lep fel. A cel, hogy mindegyik egyuttest legalabb egyszer meghallgassuk ugy, hogy a leheto legkevesebb fesztivalon vegyunk reszt.

            RockMarathon    Sziget  Volt    Metalfest   Festival5
Dalriada    0               1       1       1           1
Metallica   1               1       0       0           1
Eluveitie   1               0       0       1           0
Liva        1               1       1       0           1
IcedEarth   0               1       1       1           1
Virrasztok  0               0       1       1           0
IronMaiden  1               1       0       1           1

*/


# Sets and parameters

set Festivals;
set Bands;
param performs{Bands,Festivals};

# Variables

var goto{Festivals} binary;

# Constraints

s.t. MustSeeEachBandAtLeastOnce{b in Bands}:
    sum{f in Festivals} goto[f] * performs[b,f] >= 1;

# Objective
minimize FestivalsWeGo:
    sum{f in Festivals} goto[f];

solve;

printf "\n\n";
for{f in Festivals: goto[f]==1}
    printf "%s\n", f;
printf "\n\n";

# Set and parameter values, definitions
data;

set Festivals := RockMarathon Sziget Volt Metalfest;
set Bands:= Dalriada Metallica Eluveitie Liva IcedEarth Virrasztok IronMaiden;

param performs:
                RockMarathon    Sziget  Volt    Metalfest :=
    Dalriada    0               1       1       1           
    Metallica   1               1       0       0           
    Eluveitie   1               0       0       1           
    Liva        1               1       1       0           
    IcedEarth   0               1       1       1           
    Virrasztok  0               0       1       1           
    IronMaiden  1               1       0       1           
;


end;


