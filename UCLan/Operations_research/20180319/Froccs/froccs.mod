var xSF>=0,integer;
var xBF>=0, integer;
var xLS>=0, integer;
var xHM>=0, integer;
var xVHM>=0, integer;
var xKF>=0, integer;
var xRF>=0, integer;
var xPF>=0, integer;

s.t. WhiteWine:
    0.1 * xSF + 0.2 * xBF + 0.1 * xLS + 0.3 * xHM + 0.2 * xVHM + 0.9 * xKF + 0.1 * xRF + 0.6 * xPF <=100;

s.t. Soda:
    0.1 * xSF + 0.1 * xBF + 0.2 * xLS + 0.2 * xHM + 0.3 * xVHM + 0.1 * xKF + 0.9 * xRF + 0.3 * xPF <=150;

maximize profit :
    90 * xSF + 170 * xBF + 100 * xLS + 250 * xHM + 150 * xVHM + 650* xKF + 180 * xRF + 450 * xPF;
