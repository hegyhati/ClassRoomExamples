# Az Ultrabalaton szakaszainkat szeretnenk ugy kiosztani a csapattagok kozott, hogy minel jobb legyen az idoeredmenyunk.
# Adott minden futora a sebessege, illetve hogy minimum/maximum mennyit szeretne futni.

set Futok;
set Szakaszok;

param sebesseg{Futok}; # km/h
param min_tav{Futok}; # km
param max_tav{Futok}; # km
param tavolsag{Szakaszok}; # km

# Dontesek

var fut{Futok, Szakaszok} binary;

# Korlatok

s.t. Futokepesseg_korlatozas{f in Futok}:
    min_tav[f] <= sum{s in Szakaszok} fut[f,s] * tavolsag[s] <= max_tav[f];

s.t. Minden_szakaszt_le_kell_futni{s in Szakaszok}:
    sum{f in Futok} fut[f,s] == 1;  


# Celfuggveny

minimize Osszes_ido:
    sum{f in Futok, s in Szakaszok} fut[f,s] * tavolsag[s] / sebesseg[f];

solve;

for {f in Futok}
{
    printf "%s:\n", f;
    for {s in Szakaszok : fut[f,s] == 1}
    {
        printf "%s %g km\n", s, tavolsag[s];
    }
    printf "\n";
}