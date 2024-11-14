set dolgozok;
set munkafolyamatok;
param utolsomunka symbolic in munkafolyamatok;
param elsomunka symbolic in munkafolyamatok;
param elozo{m in munkafolyamatok: m!= elsomunka} symbolic in munkafolyamatok;
param ora;

set orak := 1..ora;

param sebesseg{dolgozok, munkafolyamatok}>=0;
param munkaora <=1 >=0;
param maxtavolsag := 10;

var dolgozas{orak,dolgozok, munkafolyamatok } binary;
var elorehaladas{orak union {0},munkafolyamatok} >= 0;

s.t. csak_egy_feladat{d in dolgozok, o in orak}:
    sum{m in munkafolyamatok} dolgozas[o,d,m]<=1;

s.t. elorehaladas_kezdet{m in munkafolyamatok}:
    elorehaladas[0,m]=0;


s.t. munka_elorehaladas { o in orak, m in munkafolyamatok}:
    elorehaladas[o,m]<=elorehaladas[o-1,m]+ munkaora * sum{d in dolgozok} dolgozas[o,d,m]*sebesseg[d,m];


s.t.  megelozo_folyamat { o in orak, m in munkafolyamatok : m!= elsomunka}:
    elorehaladas[o,m]<= elorehaladas[o, elozo[m]];

s.t. max_tavolsag{o in orak}:
    elorehaladas[o,elsomunka] - elorehaladas[o, utolsomunka] <= maxtavolsag;


maximize  kesz :
elorehaladas[ora,utolsomunka];
end;














