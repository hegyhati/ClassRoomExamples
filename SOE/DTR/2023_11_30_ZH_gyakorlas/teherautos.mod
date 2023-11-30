#Variables 

set Szallitok;
set Varosok;
set Teherauto;

param Tavolsag {Szallitok, Varosok}; #km
param supply {Szallitok}; #liter
param demand {Varosok}; #liter

param TeherautoTomeg{Teherauto}; #kg
param TeherautoKapacitas{Teherauto}; #kg
param suruseg; #kg/liter

var Szallit{Szallitok, Varosok} >= 0; # liter
var KamionSzama{Szallitok, Varosok, Teherauto} >= 0 integer; # darab

# Constraints

s.t. Supply {S in Szallitok}: sum {V in Varosok} Szallit[S,V] <= supply[S]; #literek
s.t. Demand {V in Varosok}: sum {S in Szallitok} Szallit[S,V] >= demand[V];

s.t. Teherauto_kapacitasok {S in Szallitok, V in Varosok : Tavolsag[S,V] > 0}: 
    suruseg * Szallit[S,V] <= sum {t in Teherauto} TeherautoKapacitas[t] * KamionSzama[S,V,t];

# Objective function

minimize TotalSor: sum {S in Szallitok, V in Varosok} ( sum {t in Teherauto} TeherautoTomeg[t] * KamionSzama[S,V,t]*2 + Szallit[S,V] * suruseg);

solve;

for {S in Szallitok} 
{
    printf "%s:\n", S;
    for {V in Varosok : Szallit[S,V] > 0} 
    {
        printf "  %s: %g\n", V, Szallit[S,V];
        for {t in Teherauto: KamionSzama[S,V,t] > 0} 
        {
            printf "   %d %s\n", KamionSzama[S,V,t], t;
        }
    }
}

end;
