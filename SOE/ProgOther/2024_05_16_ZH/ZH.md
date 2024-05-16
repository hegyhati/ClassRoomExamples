# Programozas I. ZH - 2024.05.16.

Mindegyik feladat megoldasa kulon fajlba keszuljon. Standalone `.py` vagy .`ipynb` notebook kozul tetszolegesen lehet valasztani izlesnek megfeleloen. Utobbi esetben ha nem egyszer kell egymas utan futtatni a code blockokat, akkor arrol legyen egyertelmu markdown leiras.

A feladatok megoldasahoz minden korabbi kod, interneten talalhato statikus tartalom (stackoverflow es tarsai), youtube videok, barmi hasznalhato. Ami nincs megengedve: kulso segitseg (ember vagy AI) hasznalata, beleertve a copilotot is. 

# Feladatok 

## 1. Hazassagi nevek - 4 pont
 - **a)** Keszits programot, mely beolvassa valaki nevet, es kiirja kulon a vezeteknevet es a keresztnevet, pl.:
```
Kerem a nevet: Bolyai Farkas
Vezeteknev: Bolyai
Keresztnev: Farkas
```
 - **b)** Modositsd a programot ugy, hogy beolvassa a ferj nevet es a feleseg leanykori nevet, es kiirja a feleseg lehetseges hazassagi neveit. Pl.:
```
Kerem a ferj nevet: Bolyai Farkas
Kerem a feleseg leanykori nevet: Benko Zsuzsanna
A lehetséges házassági nevek:
 - Benko Zsuzsanna
 - Bolyai Farkasne
 - Bolyai Farkasne Benko Zsuzsanna
 - Bolyaine Benko Zsuzsanna
 - Bolyai Zsuzsanna
 - Bolyai-Benko Zsuzsanna
 - Benko-Bolyai Zsuzsanna
```


## 2. Repulo tulfoglalasok - 4 pont
Bevett gyakorlat, hogy a legitarsasagok tobb jegyet adnak el egy jaratra, mint ahany ulohely van, ismerve a statisztikakat, hogy nem mindenki jon tenylegesen el. Irj programot, mely beolvassa a jarat kapacitasat, a jegyek arait, az eladott jegyek szamat, megjelent utasok szamat, es a karterites merteket (ha valaki nem fer fel) es kiszamolja, hogy mennyi a bevetel. Pl.:
```
Kerem a jarat kapacitasat: 200
Kerem az egy jegy arat: 10000
Kerem az eladott jegyek szamat: 180
Kerem a megjelent utasok szamat: 180
Kerem a karterites merteket: 30000
A bevetel: 1800000
```
vagy
```
Kerem a jarat kapacitasat: 200
Kerem az egy jegy arat: 10000
Kerem az eladott jegyek szamat: 180
Kerem a megjelent utasok szamat: 20
Kerem a karterites merteket: 3000000000
A bevetel: 1800000
```
vagy
```
Kerem a jarat kapacitasat: 200
Kerem az egy jegy arat: 10000
Kerem az eladott jegyek szamat: 220
Kerem a megjelent utasok szamat: 150
Kerem a karterites merteket: 30000
A bevetel: 2200000
```
vagy
```
Kerem a jarat kapacitasat: 200
Kerem az egy jegy arat: 10000
Kerem az eladott jegyek szamat: 220
Kerem a megjelent utasok szamat: 210
Kerem a karterites merteket: 30000
A bevetel: 1900000
```

## 3. Repulojarat statisztika - 6 pont

Tegyuk fel, hogy:
 - 200 ferohelyes a jarat 
 - 10000 Ft egy jegy
 - 30000 Ft a karterites merteke
 - minden utas 95% esellyel jelenik meg
 - 210 jegyet adunk el

Irj programot, mely 1000 jaratot szimulal, kiszamolja, hogy hanyan jelennek meg, es mennyi lett a bevetel. Ezt abrazolja egy boxploton. 

**Bonusz** : Ismeteld meg a feladatot 200, 210, 220, 230 eladott jegyre, es azokat is abrazold egy boxploton.

## 4. Love is in the air - 6 pont

Elsokent toltsd le ezt az az adathalmazt: 
https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles

 - **a)** Szurd le az adathalmazt azokra a sorokra, amikben nem hianyzik a kor, statusz, nem, magassag, bevetel, munka, vallas.
 - **b)** Keszits egy olyan diagrammot, mely a kor es a magassag kozotti osszefuggest abrazolja.
 - **c)** Ferfiakra es nokre leszurve abrazold kulon-kulon oszlopdiagrammon, hogy melyik beveteli kategoriaban mennyien vannak.
 - **d)** Csinalj meg egy szabadon valasztott kimutatast az adathalmaz alapjan.


## 6. Money-Money-Money - 6 pont

A feladat megoldasahoz az alabbi public API-t hasznald: 
https://github.com/hakanensari/frankfurter/blob/main/README.md

 - **a)** 2000-tol kezdve 2024-ig kerd le minden evre a januar 1 napi EUR/HUF arfolyamot, majd abrazold ezt egy diagrammon.
 - **b)** Szamold ki, hogyha minden evben januar 1-en 100000 Ft-ot eurora valtottunk volna 2000-tol 2023-ig, majd 2024 januar 1-en visszavaltottuk volna forintra, akkor a befektetett 2.4 millio Ft-bol mennyi penzunk lett volna. *BONUSZ*  Egy diagrammon abrazold, hogy mikent valtozott volna a penzunk erteke, ha atvaltjuk/nem vatljuk at a penzunket. 


## BONUSZ: 7. Petofi szinhaz programja - 6 pont

Irj programot, mely a Petofi szinhaz oldalarol (https://www.soproniszinhaz.hu/) kigyujti, es 1-2 listaban kiirja a szinmuveszeket, tancmuveszeket es eloadomuveszeket.