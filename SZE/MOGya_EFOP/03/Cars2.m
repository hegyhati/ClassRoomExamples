/*

Szenvedélyünk a gyerekkorunkat meghatározó autók gyűjtése. Öt egymást követő napon tervezünk
vásárolni egy Trabantot, egy Ladát, egy Wartburgot, egy Skodát, valamint egy Kispolskit. Minden nap
pontosan egy autóval szeretnénk meglepni magunkat, azonban az autók ára a világpiaci helyzettől
függően naponta változik az alábbi táblázatban prognosztizált módon. Milyen sorrendben vásároljuk
meg az autókat, hogy a kollekciónk teljes legyen a lehető legkisebb költségek mellett?

            Hétfő   Kedd    Szerda  Csütörtök   Péntek
Wartburg    60000   65000   61000   66000       60000
Lada        50000   55000   63000   60000       52000
Kispolski   30000   32000   33000   30000       27000
Trabant     70000   65000   77000   85000       100000
Skoda       65000   70000   75000   90000       70000

*/

set Days;
set Cars;
param price{Cars,Days};

var buy{Cars,Days} binary;

s.t. ExactlyOneCarEachDay{d in Days}:
    sum{c in Cars} buy[c,d] = 1;
 
s.t. EachCarExactlyOnce{c in Cars}:
    sum{d in Days} buy[c,d] =1;

minimize totalCost:
    sum{c in Cars, d in Days} buy[c,d]*price[c,d];

solve;

printf "\n\n";

for{c in Cars, d in Days:buy[c,d]==1}
    printf "%10s:\t%s - %d\n",c,d,price[c,d];

printf "\n\n";

data;

set Days:= Hetfo Kedd Szerda Csutortok Pentek;
set Cars:= Wartburg Lada Kispolski Trabant Skoda;

param price:
            Hetfo   Kedd    Szerda  Csutortok   Pentek :=
Wartburg    60000   65000   61000   66000       60000
Lada        50000   55000   63000   60000       52000
Kispolski   30000   32000   33000   30000       27000
Trabant     70000   65000   77000   85000       100000
Skoda       65000   70000   75000   90000       70000
;
