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
    Ha Kriszti parbajozik es Gergo parbajozik es Krisztinek tobb sms kuldoje van, akkor Gergo kiesik
    Ha parbajozik[K] == 1 es parbajozik[G] == 1 es sms[K] > sms[G] akkor kiesik[G] = 1
    kiesik[G] >= -2 + parbajozik[K] + parbajozik[G] + (sms[K] > sms[G])
*/

s.t. A_kevesebb_smssel_rendelkezo_essen_ki{f in Fordulok, v1 in Versenyzok, v2 in Versenyzok : v1 != v2}:
    kiesik[v2,f] >= -2 + parbajozik[v1,f] + parbajozik[v2,f] + if (sms[v1] > sms[v2]) then 1 else 0;
    

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