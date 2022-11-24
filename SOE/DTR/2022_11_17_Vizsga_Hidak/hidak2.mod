set InduloHelyek;
set Uticelok;
set Hidak;

param jarat{InduloHelyek,Uticelok} binary, default 0;

param kapacitas{Hidak} >= 0;
param tav1{InduloHelyek,Hidak} >= 0;
param tav2{Uticelok,Hidak} >= 0;


var atmegy{InduloHelyek,Uticelok,Hidak} binary;


minimize ossztav: sum{i in InduloHelyek, u in Uticelok, h in Hidak} atmegy[i,u,h] * (tav1[i,h] + tav2[u,h]);


s.t. HidHozzarendeles{i in InduloHelyek, u in Uticelok}:
    sum{h in Hidak} atmegy[i,u,h] = jarat[i,u];

s.t. Hidkapacitas{h in Hidak}:
    sum{i in InduloHelyek, u in Uticelok} atmegy[i,u,h] <= kapacitas[h];

# szorgalmi
var lezarva{Hidak} binary;

s.t. EgyHidLezarva: sum{h in Hidak} lezarva[h] = 1;

# Ez magaban foglalja a Hidkapacitas korlatozast is
s.t. HidLezaras{h in Hidak}:
    sum{i in InduloHelyek, u in Uticelok} atmegy[i,u,h] <= kapacitas[h] * (1 - lezarva[h]);

solve;


printf{i in InduloHelyek, u in Uticelok, h in Hidak: atmegy[i,u,h]} "%11s %9s %9s\n", i, h, u;
printf "Ossztav: %d\n", ossztav;
# szorgalmi
printf{h in Hidak: lezarva[h]} "%s lezarva.\n", h;

end;
