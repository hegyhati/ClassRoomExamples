set Students;
set Classes;

param beer{Students,Classes};

var prepare{Students,Classes} binary;

s.t. Class_constraint{c in Classes}:
  sum{s in Students} prepare[s,c] = 1;

s.t. Student_constraint{s in Students}:
  sum{c in Classes} prepare[s,c] <=1;

minimize TotalBeers:
  sum{s in Students, c in Classes} beer[s,c]*prepare[s,c];


solve;

for {c in Classes, s in Students : prepare[s,c]=1}
  printf "%s will be prepared by %s for %d beers\n",c,s,beer[s,c];


data;

set Students := Miguel    Quim    Ferran    Daniel    Marta  Ivan;

set Classes := Energy Const Auto Fabr OM;


param beer (tr): 
        Miguel    Quim    Ferran    Daniel    Marta  Ivan:=
Energy  16         7        8        3         2 2
Const   15         7       9         2           5 3
Auto    11 2 3 4 5 3
Fabr    13 6 5 8 7 3
OM      13 6 5 4 7 3
;
