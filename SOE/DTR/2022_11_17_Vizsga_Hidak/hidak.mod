set Helyek;
set Hidak;

param jaratszam >= 1;
set Jaratok := 1..jaratszam;

param start{Jaratok} symbolic in Helyek;
param cel{Jaratok} symbolic in Helyek;
param kapacitas{Hidak} >= 0;
param tav{Helyek,Hidak} >= 0;


var atmegy{Jaratok,Hidak} binary;


minimize ossztav: sum{j in Jaratok, h in Hidak} atmegy[j,h] * (tav[start[j],h] + tav[cel[j],h]);


s.t. HidHozzarendeles{j in Jaratok}:
    sum{h in Hidak} atmegy[j,h] = 1;

s.t. Hidkapacitas{h in Hidak}:
    sum{j in Jaratok} atmegy[j,h] <= kapacitas[h];

# szorgalmi
var lezarva{Hidak} binary;

s.t. EgyHidLezarva: sum{h in Hidak} lezarva[h] = 1;

# Ez magaban foglalja a Hidkapacitas korlatozast is
s.t. HidLezaras{h in Hidak}:
    sum{j in Jaratok} atmegy[j,h] <= kapacitas[h] * (1 - lezarva[h]);

solve;


printf{j in Jaratok, h in Hidak: atmegy[j,h]} "%2d %11s %9s %9s\n", j, start[j], h, cel[j];
printf "Ossztav: %d\n", ossztav;
# szorgalmi
printf{h in Hidak: lezarva[h]} "%s lezarva.\n", h;

end;
