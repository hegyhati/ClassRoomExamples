# Variables

var xSS >= 0;
var xSV >= 0;
var xSGy >= 0;
var xSP >= 0;
var xSSz >= 0;
var xPS >= 0;
var xPV >= 0;
var xPGy >= 0;
var xPP >= 0;
var xPSz >= 0;
var xNS >= 0;
var xNV >= 0;
var xNGy >= 0;
var xNP >= 0;
var xNSz >= 0;

# Constraints

s.t. SopronSupply: xSS + xSV + xSGy + xSP + xSSz <= 1000;
s.t. PecsSupply: xPS + xPV + xPGy + xPP + xPSz <= 500;
s.t. KanizsaSupply: xNS + xNV + xNGy + xNP + xNSz <= 200;

s.t. SopronDemand: xSS + xPS + xNS >= 250;
s.t. VeszpremDemand: xSV + xPV + xNV >= 350;
s.t. GyorDemand: xSGy + xPGy + xNGy >= 500;
s.t. PecsDemand: xSP + xPP + xNP >= 500;
s.t. SzombathelyDemand: xSSz + xPSz + xNSz >= 100;

# Objective function

minimize TotalSor: 0*xSS + 150*xSV + 80*xSGy + 350*xSP + 70*xSSz + 350*xPS + 250*xPV + 300*xPGy + 0*xPP + 250*xPSz + 200*xNS + 140*xNV + 220*xNGy + 150*xNP + 90*xNSz;


end;
