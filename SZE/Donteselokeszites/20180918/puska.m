/*
  Három tárgyból szeretnénk puskát csinálni.
  Van 4 haver, akit be lehet vonni, mindegyikőjük legfeljebb egy puskát vállal, mert annyi fér bele, és megvan, hogy melyiket hány sörért.

  Mi a legkevevesebb befektetés, amiből az összes holnapi ZH-ra el tud készülni a puska?


        AI  Halo  OS  
Dani    10  4     4   
Kristof 8   5     9
Isti    2   3     15
Niki    4   3     8
*/

var yDA binary;
var yDH binary;
var yDO binary;
var yKA binary;
var yKH binary;
var yKO binary;
var yIA binary;
var yIH binary;
var yIO binary;
var yNA binary;
var yNH binary;
var yNO binary;

# Minden targybol legalabb 1 jegyzet
s.t. AnyagIsmeret:
  yDA+yKA+yIA+yNA >= 1;
s.t. SzamitogepHalozatok:
  yDH+yKH+yIH+yNH >= 1;
s.t. OperaciosRendszerek:
  yDO+yKO+yIO+yNO >= 1;

# Mindenkinek csak egy jegyzetre van legfeljebb ideje
s.t. Dani:
  yDA+yDH+yDO <= 1;
s.t. Kristof:
  yKA+yKH+yKO <= 1;
s.t. Isti:
  yIA+yIH+yIO <= 1;
s.t. Niki:
  yNA+yNH+yNO <= 1;

minimize Puskapenz:
  10*yDA+ 4*yDH+  4*yDO
+ 8 *yKA+ 5*yKH+  9*yKO
+ 2 *yIA+ 3*yIH+  15*yIO
+ 4 *yNA+ 3*yNH+  8*yNO;  
