/*
  Néhány tárgyból szeretnénk puskát csinálni.
  Van pár haver, akit be lehet vonni, mindegyikőjük legfeljebb egy puskát vállal, mert annyi fér bele, és megvan, hogy melyiket hány sörért.

  Mi a legkevevesebb befektetés, amiből az összes holnapi ZH-ra el tud készülni a puska?

*/

set Targyak;
set Emberek;

param dij{Emberek,Targyak};

var y{Emberek,Targyak} binary;

s.t. LegalabbEgyJegyzet{t in Targyak}:
  sum{e in Emberek} y[e,t] >= 1;

s.t. MindenkiMaxEgyet{e in Emberek}:
  sum{t in Targyak} y[e,t] <= 1;

minimize OsszesPenz:
  sum{e in Emberek, t in Targyak} y[e,t]*dij[e,t];

data;

set Targyak := OS Halo AI Donteselokeszites;
set Emberek := Ancsi Joska Pisti Zsuzsi Sanyi;

param dij:
          OS    Halo    AI    Donteselokeszites:=
  Ancsi   4     3       8     99
  Joska   6     9       15    5 
  Zsuzsi  3     5       4     3
  Pisti   2     6       8     1
  Sanyi   6     12      54    0
  ;

end;
