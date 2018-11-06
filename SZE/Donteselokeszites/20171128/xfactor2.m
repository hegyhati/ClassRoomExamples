/*
A TV-Klub tévécsatorna tehetségkutató műsorának vezetésével bíztak meg minket. Az előválogatók után 8 versenyző került az élő műsorba, ahol 7 héten keresztül mindig kiesik valaki, és a végén egyetlen győztes marad. A műsor menetrendje a szokásos: miközben a versenyzők előadják az aktuális heti darabjukat, és elmesélik életük valamely szomorú epizódját, addig a nézők szorgalmasan küldözgetik az emelt díjas SMS-eket. A műsor vége előtt kihirdetjük az utolsó két helyen lévőt, és adunk
további 20 percet SMS-ek küldözésére. A 20 perc lejárta után a kevesebb szavazattal
rendelkező kiesik.

A selejtezők során már készítettünk egy statisztikai felmérést, amiből tudjuk, hogy
melyik versenyzőnek hány támogatója van, akik hajlandóak sms-t küldeni, ha a
választottjuk az utolsó két hely valamelyikére kerülne.

Az üzleti modell kevésbé publikus része, hogy tetszőlegesen belenyúlhatunk bármikor az
eredményekbe, tehát lényegében mi mondjuk meg, hogy egy héten ki legyen az a kettő
versenyző, aki párbajozik, viszont ott már a népszerűbbiknek kell bentmaradnia.

Célunk természetesen az, hogy a 7 forduló során minél több bevételünk származzon az
emelt díjas sms-ekből.
• Ha egy versenyző kiesett, akkor értelemszerűen a következő műsorokban már
nem szerepel, így nem is párbajozhat.
• Azokat az sms-eket nem számoljuk, amik a performanszok közben érkeznek.

Melyik héten kik párbajozzanak, hogy a lehető legtöbb bevételünk legyen.

*/


set Resztvevok;

param adasok_szama:=card(Resztvevok)-1;

set Adasok := 1..adasok_szama;

param sms{Resztvevok};

var pbe{Adasok,Resztvevok}, binary;
var pki{Adasok,Resztvevok}, binary;

s.t. EgyValakiEsikKi{a in Adasok}:
    sum{r in Resztvevok} pki[a,r] = 1;

s.t. EgyValakiMaradBent{a in Adasok}:
    sum{r in Resztvevok} pbe[a,r] = 1;

s.t. LegfeljebbKetszerGyoz {r in Resztvevok}:
    sum{a in Adasok} pbe[a,r] <= 2;

s.t. ElozoPluszRegebbiEgyben{av in Adasok, r in Resztvevok}:
    pki[av,r]+pbe[av,r] <= 1 - sum{a in Adasok: a<av} pki[a,r];

#kovetkezovel redundans
s.t. NepszerubbMarad{a in Adasok, r1 in Resztvevok, r2 in Resztvevok: r1 != r2}:
    sms[r1] >= sms[r2] - 500 * (2-pbe[a,r1]-pki[a,r2]);
    

s.t. NepszerubbMarad2{a in Adasok}:
    sum{r in Resztvevok} pbe[a,r]*sms[r] >= sum{r in Resztvevok} pki[a,r]*sms[r];



# TODO cfv
maximize TotalSMS : sum{a in Adasok, r in Resztvevok} sms[r]*(pki[a,r]+pbe[a,r]);

solve;

printf "\n\n";
for {a in Adasok}
{
    printf "Adas %d: ",a;
    for{r in Resztvevok: pbe[a,r]==1}
        printf "\tBentmarad: %s (%d)",r,sms[r];
    for{r in Resztvevok: pki[a,r]==1}
        printf "\tKiesik: %s (%d)",r,sms[r];
    printf "\n";
}

printf "\n\nOsszes SMS: %d\n\n",TotalSMS;

data;

set Resztvevok := Gizike DJSanyee Rockkati TucTuci MsLady Belaba Maunika Popapi;

param sms:=
    Gizike      12
    DJSanyee    23
    Rockkati    123
    TucTuci     45
    MsLady      369
    Belaba      125
    Maunika     255
    Popapi      1
;

end;
