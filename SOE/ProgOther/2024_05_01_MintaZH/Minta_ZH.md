# Programozas I. Minta ZH

Mindegyik feladat megoldasa kulon fajlba keszuljon. Standalone `.py` vagy .`ipynb` notebook kozul tetszolegesen lehet valasztani izlesnek megfeleloen. Utobbi esetben ha nem egyszer kell egymas utan futtatni a code blockokat, akkor arrol legyen egyertelmu markdown leiras.

A feladatok megoldasahoz minden korabbi kod, interneten talalhato statikus tartalom (stackoverflow es tarsai), youtube videok, barmi hasznalhato. Ami nincs megengedve: kulso segitseg (ember vagy AI) hasznalata, beleertve a copilotot is. 

Az egyes feladatok tobbszor fel vannak bontva reszlepesekre, erdemes ezek szerint haladni, de nem kotelezo.

# Feladatok 

## 1. Szamjegy osszegek
 - **a)** Keszits programot, mely beolvas egy szamot, es kiirja a szamjegyeinek az osszeget.
 - **b)** Egeszitsd ki a programot azzal, hogy ha negativ szamot adnak meg, akkor kerjen addig ujra, amig nemnegativ egeszet nem kap. (Arra nem kell felkesziteni a programot, hogy tortek, nem szamok esetet lekezelje.)
 - **c)** Miutan kiszamolta a szamjegyek osszeget a pogram, ismetelje ezt addig, amig egyjegyu szamhoz nem jutunk, es kozben irja is ki ezeket. Pl.: 2024 -> 8, vagy 1989 -> 27 -> 9

## 2. Szamjegyosszeg statisztika
Irj programot, mely 0-tol 10<sup>6</sup>-ig minden szamra vegrehajtja az 1. feladatban leirt algoritmust, es feljegyzi, hogy hany sorozat vegzodott 0-ban, 1-ben, .., 9-ben. Ez legyen egy oszlopdiagrammon abrazolva, melyet `digitsums.png` neven mentse el a program.

## 3. Peti "blackjackezik"
Peti egy blackjack szeru jatekot jatszik dobokockaval. A jatek lenyege, hogy a jatekos dobokockaval dob, es a dobott szamok osszege minel kozelebb kell legyen 11-hez, de alulrol. Ha tullepi, akkor automatikusan vesztett. 

Peti strategiaja, hogy dob addig, amig az eddigi osszeg 7  vagy az alatt van, es akkor "megall". Nehany elofordulo scenario:
 - Elso dobas 6, masodik dobas 2, Peti megall 8-cal.
 - Elso dobas 2, masodik dobas 5, harmadik dobas 3, Peti megall 10-zel.
 - Elso dobas 6, masodik dobas 6, Peti vesztett.

Irj programot, ami lejatszik 1000 jatekot, majd egy torta diagrammon abrazolja, hogy hanyszor vesztett Peti. 

## 4. Rozsi is jatszik

Rozsi hasonlo modon jatszik, mint Peti, csak batrabb, meg 8-nal is dob egyet. Elkezdnek egymas ellen jatszani. Minden korben mindkettejuk reszerol 1 Ft a tet. Ha:
 - mindketten vesztnek, akkor a bank viszi el a 2 Ft-ot. 
 - egyikojuk veszit, akkor a masik viszi el a 2 Ft-ot.
 - egyik sem veszit, de valamelyikojuk kozelebb van a 11-hez, az viszi a 2 forintot
 - egyikojuk sem veszit, es ugyanannyival allnak meg, visszakapjak az 1-1 forintjukat

 - **a)** Irj egy programot, mely egyetlen jatekot szimulal, es leirja, hogy a fenti 4 kozul mi lett a vegeredmeny.
 - **b)** Irj programot, mely a fenti jatekot 100x lejatsza egymas utan, majd egy vonaldiagrammon abrazolja Peti, Rozsi es a bank egyenleget. (mindegyik 0-rol indul).

## 5. Mount Everest 

Elsokent toltsd le ezt az az adathalmazt: 
https://www.kaggle.com/datasets/shivamb/mount-everest-climbing-deaths

Majd keszitsd el a kovetkezo szureseket, kimutatasokat pandas/matplotlib segitsegevel:
 - **a)** Csinalj egy uj oszlopot, mely a baleset evet tartalmazza.
 - **b)** Egy scatter ploton abrazold az eseteket, ahol az x tengely az ev, az y a hegymaszo kora.
 - **c)** Oszlopdiagrammon abrazold, hogy melyik orszagbol hany halaleset volt.
 - **d)** Oszlopdiagrammon abrazold, hogy a nepali hegymaszok eseteben melyik ok hany hegymaszo eletet kovetelte.

## 6. Naphosszok

A feladat megoldasahoz az alabbi public API-t hasznald: https://sunrise-sunset.org/api
 - **a)** Kerd le, hogy Sopronban milyen hosszu egy nap minden honap elsejen (iden), es abrazold egy vonaldiagrammon. (2024-01-01-tol 2025-01-01-ig, tehat 13 pont legyen.)
 - **b)** Ismeteld meg ugyanezt Reykjavik-ra, Sydney-re, es azokat is tedd ra a diagrammra.


## 7. Petofi szinhaz programja

Irj programot, mely a Petofi szinhaz oldalarol (https://www.soproniszinhaz.hu/) kigyujti, es harom listaban kiirja, hogy milyen felnott, ifjusagi, illetve gyerekelodasok vannak musoron.
