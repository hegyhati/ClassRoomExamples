/*
A Közép-Dunántúli piros sáv turistajelzést jelzést szeretnénk minél hosszabb szakaszon
felújítani. Szombaton reggel 6-kor hatan érkezünk meg Zircre vonattal: Pygmea,
Repkény, Droid, Bubu, Gethe, Galád.

A jelzések felújításának a folyamata a következő:
1. régi jelzés, fakéreg lehántása
2. fehér alap felfestése
3. jelzésminta felfestése
4. lakkozás

Adott hogy melyik túrázó melyik folyamatban mennyire ügyes, azaz egy óra alatt hány
kilométernyi szakaszt tud megcsinálni.

A cél, hogy este 10-ig minél hosszabb szakaszon legyen kész a lakkozott új jelzés. A
munkát két órás szakaszokban koordináljuk, amiből 100 percet keményen dolgozunk,
majd 20 perc szünetet tartunk, amikor összegyűlünk, eszegetünk, megbeszéljük, hogy a
következő két órában ki-mit csináljon, átadjuk az eszközöket, stb.

Szabályok:
• Ha többen dolgoznak ugyanazon a folyamaton, akkor a sebességük összeadódik.
• Egyik folyamat sem előzheti meg az azt megelőzőt. Azaz ha például a fehér alapot
festő ember utoléri a hántást végzőt, akkor nem előzi meg, hanem az ő
sebességével halad tovább.
• Mivel mindegyik feladathoz külön eszközök kellenek, amit nem szeretnénk
magukra hagyni az erdőben, ezért minden órában mindegyik munkafolyamaton
legalább egy embernek dolgoznia kell.
• Azért, hogy a 20 perc elég legyen az összeröffenésre, a hántó(k) és lakkozó(k)
közötti távolság nem nőhet 1.5 km fölé. Ha így lenne, akkor a hántók
visszavesznek a sebességükből.
• Nem szükséges foglalkozni azzal, hogy hol sötétedik ránk, és onnét hogy utazunk
haza, stb.

*/


set Emberek;
set Munkak;

param nSzakasz;
set Szakaszok:= 1..nSzakasz;

param tav{Emberek,Munkak};

# Valtozok
var csinal{Emberek,Szakaszok,Munkak}, binary;
var hantaskm{0..nSzakasz} >=0;
var alapkm{0..nSzakasz} >=0;
var festeskm{0..nSzakasz} >= 0;
var lakkkm{0..nSzakasz} >=0;


# Korlatozasok

# Minden folyamaton minden szakaszban legalabb 1 ember dolgozik

s.t. MindigMindentCsinalValaki{m in Munkak, sz in Szakaszok}:
    sum{e in Emberek} csinal[e,sz,m] >= 1;


# Egy ember minden szakaszban csak 1 dolgot csinalhat
s.t. EgyEmberEgyszerreCsakEgyet{e in Emberek, sz in Szakaszok}:
    sum{m in Munkak} csinal[e,sz,m] = 1;


# Max annyit haladunk, amennyit a feladathoz rendelt emberek 100 perc alatt tudnak

s.t. HantasInit: hantaskm[0]=0;
s.t. HantasHaladas{sz in Szakaszok}:
    hantaskm[sz] <= hantaskm[sz-1] + sum{e in Emberek} csinal[e,sz,'hantas']*tav[e,'hantas']*100/60;

s.t. alapInit: alapkm[0]=0;
s.t. alapHaladas{sz in Szakaszok}:
    alapkm[sz] <= alapkm[sz-1] + sum{e in Emberek} csinal[e,sz,'alap']*tav[e,'alap']*100/60;

s.t. festesInit: festeskm[0]=0;
s.t. festesHaladas{sz in Szakaszok}:
    festeskm[sz] <= festeskm[sz-1] + sum{e in Emberek} csinal[e,sz,'festes']*tav[e,'festes']*100/60;

s.t. lakkInit: lakkkm[0]=0;
s.t. lakkHaladas{sz in Szakaszok}:
    lakkkm[sz] <= lakkkm[sz-1] + sum{e in Emberek} csinal[e,sz,'lakk']*tav[e,'lakk']*100/60;

# hantas es a lakk kozott max 2 km lehet minden szakasz vegen
s.t. HantasNemMehetTulMesszeALakkozastol{sz in Szakaszok}:
    hantaskm[sz]<=lakkkm[sz]+2;


# Nem elozhetik be egymast a folyamatok egyik szakaszban sem
s.t. AlapozasNemEloz{sz in Szakaszok}:
    alapkm[sz]<=hantaskm[sz];
s.t. FestesNemEloz{sz in Szakaszok}:
    festeskm[sz]<=alapkm[sz];
s.t. LakkozasNemEloz{sz in Szakaszok}:
    lakkkm[sz]<=festeskm[sz];

#Celfuggveny

# lakkozas minel messzebb jusson a vegen
maximize TeljesenKeszenVan: lakkkm[nSzakasz];

solve;

for {sz in Szakaszok}
{
    printf "%d. szakasz:\n",sz;
            printf "\t%4s %4f -> %4f: ", "hantas",hantaskm[sz-1],hantaskm[sz];
            for {e in Emberek: csinal[e,sz,'hantas']=1}
                printf "%s ",e;
            printf "\n";
            
            printf "\t%4s %4f -> %4f: ", "alap",alapkm[sz-1],alapkm[sz];
            for {e in Emberek: csinal[e,sz,'alap']=1}
                printf "%s ",e;
            printf "\n";        
            
            printf "\t%4s %4f -> %4f: ", "festes",festeskm[sz-1],festeskm[sz];
            for {e in Emberek: csinal[e,sz,'festes']=1}
                printf "%s ",e;
            printf "\n";
            
            printf "\t%4s %4f -> %4f: ", "lakk",lakkkm[sz-1],lakkkm[sz];
            for {e in Emberek: csinal[e,sz,'lakk']=1}
                printf "%s ",e;
            printf "\n";
    
}
