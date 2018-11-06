# Az Ultrabalaton szakaszainkat szeretnenk ugy kiosztani a csapattagok kozott, hogy minel jobb legyen az idoeredmenyunk.
# Adott minden futora a sebessege, illetve hogy minimum/maximum mennyit szeretne futni.

set Futok;

param szakaszszam;
set Szakaszok:= 1..szakaszszam;

param hossz{Szakaszok}; #km
param iram{Futok}; #perc/km
param maxtav{Futok}; # km
param mintav{Futok}; # km

var fut{Szakaszok,Futok}, binary;

s.t. EgySzakasztEgyValaki{sz in Szakaszok}:
    sum{f in Futok} fut[sz,f] = 1;

s.t. LegalabbAmennyitSzeretne{f in Futok}:
    sum{sz in Szakaszok} fut[sz,f] *hossz[sz] >= mintav[f];

s.t. LegfeljebbAmennyitSzeretne{f in Futok}:
    sum{sz in Szakaszok} fut[sz,f] *hossz[sz] <= maxtav[f];

minimize Osszido: sum {sz in Szakaszok, f in Futok} fut[sz,f] * (hossz[sz]*iram[f]);

solve;

printf "\n\n";
for {sz in Szakaszok}
{
    printf "Szakasz %d (%.2f km):",sz, hossz[sz];
    for{f in Futok:fut[sz,f]=1}
        printf "\t%s\t%d p\n",f,hossz[sz]*iram[f];
}

printf "\n\n";
for{f in Futok}
{
    printf "%s\t%.2f km\t%d p\n",f,sum{sz in Szakaszok} hossz[sz]*fut[sz,f], sum{sz in Szakaszok} hossz[sz]*fut[sz,f]*iram[f];
}

printf "\nOsszido: %d p\n", Osszido;
printf "\n\n";

