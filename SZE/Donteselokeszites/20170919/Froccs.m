#valtozok
var xKF; # adag
var xNF; # adag
var xHL; # adag
var xHM; # adag
var xVHM; # adag
var xKrF; # adag
var xSF; # adag
var xPF; # adag


#korlatozasok

s.t. Bor: # deciliter
  1*xKF + 2*xNF + 1*xHL + 3*xHM + 2*xVHM + 9*xKrF + 1*xSF + 6*xPF <= 1000;

s.t. Szoda: # deciliter
  1*xKF + 1*xNF + 2*xHL + 2*xHM + 3*xVHM + 1*xKrF + 9*xSF + 3*xPF <= 1500;


#celfuggveny
# profit legyen minel nagyobb

maximize Profit: 0;
