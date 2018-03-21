var y1, binary;
var y2, binary;
var y3, binary;
var y4, binary;
var y5, binary;
var y6, binary;

s.t. ACDC: y1+y2+y4+y5 >= 1;
s.t. Maroon5: y1+y3+y5+y6 >= 1;
s.t. LadyGaga: y2+y4+y5 >=1;
s.t. Metallica: y2+y3+y4 >=1;
s.t. PinkFloyd: y3+y6 >= 1;
s.t. RollingStones: y3+y4 >=1;
s.t. LinkinPark: y1+y2+y3 >= 1;
s.t. Beethoven: y4+y5+y6>=1;

minimize numberofvisitedfestivals: y1+y2+y3+y4+y5;
