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

solve;

printf "Osszes penz: %g\n\n",OsszesPenz;

for{e in Emberek, t in Targyak: y[e,t]==1}
{
  printf "%20s\t%10s\t%4g\n",t,e,dij[e,t];
}
end;
