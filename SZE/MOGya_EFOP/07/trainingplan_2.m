/*
A sport fontos szerepet tölt be életünkben, ugyanakkor nagyon szűkös az időbeosztásunk is, így előre szeretnénk megtervezni a novemberi edzésrendünket.  Négyféle sportot űzünk: futás, bringázás, görkorizás és úszás. 

A cél egy edzésterv elkészítése a következő információk birtokában, és feltételek figyelembe vételével:
  Minden napról tudjuk előre, hogy mennyi szabadidővel fogunk rendelkezni.
  Egy nap nem váltogatunk többféle mozgás között.
  Sajnos mindegyik sport űzése jár valamennyi sallang idővel (átöltözés, zuhanyzás, stb.), ezek ismeretesek, és függetlenek az edzés hosszától. Ha nincs legalább ennyi szabad időnk,  nyilván el sem indulunk.
  Mindegyik sporthoz adott az edzéstempónk.
  Görkorizni esős időben a csúszós úton nem lehet. Egy időjós ismerősünk szerencsére meg tudja jósolni, hogy előreláthatólag melyik napokon fog esni.
  Szeretjük a változatosságot, így két egymást követő nap nem szeretnénk ugyanazt sportolni.
  Minden sportnemhez adott, hogy legalább mekkora távolságot muszáj a hónapban letudni, hogy az éves kvóta meglegyen.
A fenti korlátozásokon túl szeretnénk minél több napot futással tölteni, hiszen a négy közül az a kedvencünk.
*/

# Input Data
param dayCount;
set Days:= 1..dayCount;

param freetime{Days}; # hours
param rain{Days}; # 1-rains, 0-doesn't rain

set Sports;
set DrySports within Sports;
param overhead{Sports}; # hours
param speed{Sports}; # km/h
param mindistance{Sports}; # km

param favorite symbolic in Sports;


set PossibleTrainings := 
  setof {d in Days, s in Sports diff DrySports :  overhead[s] < freetime[d] } (d,s)  
  union 
  setof {d in Days, s in DrySports: overhead[s] < freetime[d] && rain[d]==0} (d,s)
  ;

# Variables
var train{PossibleTrainings} binary;

# Constraints

# At most one sport per day
s.t. SportSelection {d in Days} :
  sum{(d,s) in PossibleTrainings} train[d,s]<=1;

# Don't do the same in consecutive days
s.t. Variety{(d,s) in PossibleTrainings: d!=1 && (d-1,s) in PossibleTrainings}:
  train[d,s]+train[d-1,s] <= 1;

# Train the minimum distance from each sport type
s.t. MinimumDistance{s in Sports}:
  sum{(d,s) in PossibleTrainings} train[d,s] * (freetime[d] - overhead[s]) * speed[s]>= mindistance[s];


# Objective function
maximize RunningDays : sum{(d,favorite) in PossibleTrainings} train[d,favorite];

# Display
solve;

for{d in Days}
{
  for {(d,s) in PossibleTrainings:train[d,s]==1}
  {
    printf "Day %2d: %s \t%g hours \t%g km\n",d,s,freetime[d]-overhead[s],(freetime[d]-overhead[s])*speed[s];
  }
}
printf "\n\n";
printf "%10s\tDays\tTotal km\n","Sport";
for{s in Sports}
{
  printf "%10s\t%2d\t%g\n",s,sum{(d,s) in PossibleTrainings}train[d,s],sum{(d,s) in PossibleTrainings} train[d,s] * (freetime[d] - overhead[s]) * speed[s];
}

