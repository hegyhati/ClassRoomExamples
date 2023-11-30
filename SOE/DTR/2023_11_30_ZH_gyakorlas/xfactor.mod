/*
A TV-Klub tévécsatorna tehetségkutató műsorának vezetésével bíztak meg minket. Az előválogatók után 8 versenyző került az élő műsorba, ahol 7 héten keresztül mindig kiesik valaki, és a végén egyetlen győztes marad. A műsor menetrendje a szokásos: miközben a versenyzők előadják az aktuális heti darabjukat, és elmesélik életük valamely szomorú epizódját, addig a nézők szorgalmasan küldözgetik az emelt díjas SMS-eket. A műsor vége előtt kihirdetjük az utolsó két helyen lévőt, és adunk
további 20 percet SMS-ek küldözésére. A 20 perc lejárta után a kevesebb szavazattal
rendelkező kiesik.

A selejtezők során már készítettünk egy statisztikai felmérést, amiből tudjuk, hogy
melyik versenyzőnek hány támogatója van, akik hajlandóak sms-t küldeni, ha a
választottjuk az utolsó két hely valamelyikére kerülne.

Az üzleti modell kevésbé publikus része, hogy tetszőlegesen belenyúlhatunk bármikor az
eredményekbe, tehát lényegében mi mondjuk meg, hogy egy héten ki legyen az a kettő
versenyző, aki párbajozik, majd a szavazatok számától függetlenül melyikőjük legyen az,
aki kiesik.

Célunk természetesen az, hogy a 7 forduló során minél több bevételünk származzon az
emelt díjas sms-ekből.
• Ha egy versenyző kiesett, akkor értelemszerűen a következő műsorokban már
nem szerepel, így nem is párbajozhat.
• Azokat az sms-eket nem számoljuk, amik a performanszok közben érkeznek.
• A látszat érdekében senki nem juthat tovább párbajból 2-nél többször.

Melyik héten ki essen ki, és ki legyen, akivel párbajozik, hogy a lehető legtöbb
bevételünk legyen.

*/

set Versenyzok;
set Fordulok := 1 .. card(Versenyzok)-1;

param sms{Versenyzok}  >= 0, integer;

var parbajozik{Versenyzok,Fordulok}  binary;
var kiesik{Versenyzok,Fordulok}  binary;
/*
 - 3-nal tobbszor nem parbajozhat valaki (harmadiknal ki kell esni)
*/

# Aki nem parbajozik, az nem is eshet ki
s.t. Az_eshet_ki_aki_parbajozik{v in Versenyzok, f in Fordulok}:
    kiesik[v,f] <= parbajozik[v,f];

s.t. Pontosan_ketten_parbajoznak{f in Fordulok}:
    sum{v in Versenyzok} parbajozik[v,f] = 2;

s.t. Pontosan_egy_ember_esik_ki{f in Fordulok}:
    sum{v in Versenyzok} kiesik[v,f] = 1;

s.t. Egyvalaki_legfeljebb_egyszer_eshet_ki{v in Versenyzok}: # nem szukseges
    sum{f in Fordulok} kiesik[v,f] <= 1;

/*
1. ford: OK
2. ford:
 - Ha Kriszti kiesett az elso forduloban, akkor a maodikban nem parbajozhat
  Ha kiesik[Kriszti,1] == 1 akkor parbajozik[Kriszti,2] = 0
  parbajozik[Kriszti,2] <= 1 - kiesik[Kriszti,1]

 - Ha Gergo kiesett az elso forduloban, akkor a masodikban nem parbajozhat
 - Ha Mate kiesett az elso forduloban, akkor a masodikban nem parbajozhat
3. ford:
 - Ha Kriszti kiesett az elso vagy masodik forduloban, akkor a harmadikban nem parbajozhat
 - Ha Gergo kiesett az elso vagy masodik forduloban, akkor a harmadikban nem parbajozhat
 - Ha Mate kiesett az elso vagy masodik forduloban, akkor a harmadikban nem parbajozhat
    Ha kiesik[Mate,1] == 1 vagy kiesik[Mate,2] == 1 akkor parbajozik[Mate,3] = 0
    parbajozik[Mate,3] <= 1 - kiesik[Mate,1] - kiesik[Mate,2]
*/
s.t. Nem_parbajozhat_aki_mar_kiesett{v in Versenyzok, f in Fordulok : f>1}:
    parbajozik[v,f] <= 1 - sum{fkorabbi in 1..f-1} kiesik[v,fkorabbi];

/*
    Senki nem nyezhet kettonel tobbszor
    Ha mar a harmadik parbajnal jar Krisziti, akkor kieseik
    6. korben:
    Ha az elso hat korben 3x parbajozik Kriszti, akkor most kiesik
    Ha sum{f in 1..6} parbajozik[Kriszti,f] == 3 akkor kiesik[Kriszti,6] = 1
    kiesik[Kriszti,6] >= -2 + sum{f in 1..6} parbajozik[Kriszti,f]
*/

s.t. Ha_harmadjara_parbajozik_akkor_ki_kell_esnie{v in Versenyzok, f in Fordulok : f>2}:
    kiesik[v,f] >= -2 + sum{fnemkesobbi in 1..f} parbajozik[v,fnemkesobbi];

/*
    Kirszti nem nyerhet kettonel tobbszor
    Ahanyszor kriszti nyer <= 2
    Ahanyszor parbajozik a Kriszti es nem esik ki az <= 2
    Ahanyszor parbajozik[Kriszti] == 1 es kiesik[Kriszti] == 0 az <= 2
    Ahanyszor parbajozik[Kriszti] - kiesik[Kriszti] == 1 az <= 2
*/
s.t. Mindenki_legfeljebb_ketszer_nyerhet{v in Versenyzok}:
    sum{f in Fordulok} (parbajozik[v,f] - kiesik[v,f]) <= 2;

maximize Bevetel: sum{v in Versenyzok, f in Fordulok} sms[v] * parbajozik[v,f];

solve;

for {f in Fordulok}:
{
    printf "Fordulo %d\n", f;
    for {v in Versenyzok : parbajozik[v,f] == 1}:
    {
        printf " - %s %s\n", v, if kiesik[v,f] == 1 then "kiesik" else "bentmarad";
    }
}