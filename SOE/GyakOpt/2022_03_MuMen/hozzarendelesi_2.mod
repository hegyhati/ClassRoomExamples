set Emberek;
set Targyak;
param sor{Targyak,Emberek} >= 0;

var megcsinal{Emberek,Targyak} binary;

s.t. Minden_targyat_egyszer{t in Targyak}:
    sum{e in Emberek} megcsinal[e,t] = 1;

s.t. Minden_ember_egyet{e in Emberek}:
    sum{t in Targyak} megcsinal[e,t] = 1;

minimize Osszes_megvett_sor:
    sum{e in Emberek, t in Targyak} sor[e,t]*megcsinal[e,t];


solve;

for {e in Emberek, t in Targyak : megcsinal[e,t]==1}
    printf "%s csinalja meg a %s targy jegyzetet.\n", e, t;

end;

