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
