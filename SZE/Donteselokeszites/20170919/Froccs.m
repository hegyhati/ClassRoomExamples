#valtozok
var xKF >=0, integer; # adag
var xNF >=0, integer; # adag
var xHL >=0, integer; # adag
var xHM >=0, integer; # adag
var xVHM >=0, integer; # adag
var xKrF >=0, integer; # adag
var xSF >=0, integer; # adag
var xPF >=0, integer; # adag


#korlatozasok

s.t. Bor: # deciliter
  1*xKF + 2*xNF + 1*xHL + 3*xHM + 2*xVHM + 9*xKrF + 1*xSF + 6*xPF <= 1000;

s.t. Szoda: # deciliter
  1*xKF + 1*xNF + 2*xHL + 2*xHM + 3*xVHM + 1*xKrF + 9*xSF + 3*xPF <= 1500;


#celfuggveny
# profit legyen minel nagyobb

maximize Profit:
90*xKF + 170*xNF + 100*xHL + 250*xHM + 180*xVHM + 650*xKrF + 140*xSF + 480*xPF;
