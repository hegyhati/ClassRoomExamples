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

var RockMarathon binary;
var Sziget binary;
var Volt binary;
var Metalfest binary;
var Festival5 binary;

s.t. Dalriada:
    Sziget + Volt + Metalfest + Festival5>= 1;

s.t. Metallica:
    RockMarathon + Sziget + Festival5>= 1;

s.t. Eluveitie:
     RockMarathon + Metalfest>=1;

s.t. Liva:
     RockMarathon + Sziget + Volt + Festival5>=1;

s.t. IcedEarth:
     Sziget + Volt + Metalfest + Festival5>=1;

s.t. Virrasztok:
     Volt + Metalfest >=1;
     
s.t. IronMaiden:
     RockMarathon + Sziget + Metalfest + Festival5>= 1;
     
minimize Festivals:
    RockMarathon + Sziget + Volt + Metalfest + Festival5;

end;


