# Elméleti feladatok, illetve a megoldások feltöltése
Itt: https://szelearning.sze.hu/course/view.php?id=3163

# Alap feladat közepes jegyért

Egy megépítendő áruház sorait szeretnénk megtervezni úgy, hogy minél kevésbé legyen "hosszú" az áruházunk.

A terület szélességét ismerjük, és ebből bemenetként adott, hogy hány sorral tervezhetünk. Tudjuk továbbá azt is, hogy hány kasszát kell beépíteni. Minden kassza egy sornyi szélességet foglal el, a hossza pedig adott. Értelemszerűen, azoknak a soroknak ennyivel rövidebbeknek kell lennie, amelyik végén kassza van.

Tehát a layout valami ilyesmi például 7 sor és 3 kassza esetén, ahol minden kassza hossza most itt 4, a (nem kasszás) sorok hossza pedig 10.

```bash
 $$$  $$$  $$$   ##   ##   ##   ##
 $$$  $$$  $$$   ##   ##   ##   ##
 $$$  $$$  $$$   ##   ##   ##   ##
 $$$  $$$  $$$   ##   ##   ##   ##
  ##   ##   ##   ##   ##   ##   ##
  ##   ##   ##   ##   ##   ##   ##
  ##   ##   ##   ##   ##   ##   ##
  ##   ##   ##   ##   ##   ##   ##
  ##   ##   ##   ##   ##   ##   ##
  ##   ##   ##   ##   ##   ##   ##
```

Vannak különböző termékcsoportjaink, amikhez adott, hogy egy soron hány méternyi helyet foglalnának el. (Feltételezzük, hogy minden sor két oldalas, és ez a szám már a kétoldalas pakolás esetén értendő.) Egy termékcsoport termékei nem oszthatók szét több sorba.

A feladat úgy megtervezni az áruház pakolását, hogy a sorokat (és ezáltal az épületet) minél rövidebbre tudjuk venni. Az épület hosszát most egyszerűen úgy vesszük, mint a leghosszabb sor hosszát (amibe most értelemszerűen a kassza hosszát is belevesszük, ha van a sorban).

## Példa bemenet

```ampl
param nRows         :=   3;
param cashierCount  :=   1;
param cashierLength := 2.5;

set ProductGroups :=  Group1 Group2 Group3 Group4 Group5 Group6 Group7 Group8;

param space :=
Group1	0.04
Group2	0.62
Group3	0.13
Group4	1.28
Group5	0.56
Group6	0.21
Group7	1.39
Group8	1.47
;
```

Ezekre az adatokra a helyes kimenet: `2.750000`

## Technikai megjegyzés

Ez a szint automatikusan, egy script által lesz javítva, ezért:
 - a modell fájl neve maradjon `model.mod`, és csak ez legyen feltöltve moodle-re (semmi zip és társai)
 - a feltöltött modell fájlban semmiképpen ne szerepeljen data section, mert azt külön fájlból fogja beszedni a script
 - ha tesztelési célzattal voltak további kiiratások, azok feltöltés előtt legyenek kikommentezve

# Kibővített feladat jobb jegyért

Ebben a feladatban már nem az áruház hosszának minimalizálása a cél, ez bemeneti paraméterként adott. A cél most a "manipulált bevétel" maximalizálása.

Manipulált bevétel alatt abból az eladásból származó bevételt értjük, amikor a vásárló megvesz valamit, amit eredetileg nem akart, de mivel meglátta, ezért megveszi.

## Bemenet

Az alap szinthez képest további bemeneti adatok:
 - minden termékcsoporthoz egy átlagos termékár
 - olyan termékcsoport párok halmaza, amiket muszáj ugyanarra a sorra tenni
 - olyan termékcsoport párok halmaza, amiket tilos ugyanarra a sorra tenni
 - a sorok maximális hossza
 - vásárlói csoportok halmaza, valamint mindegyikre:
   - a csoportba tartozó emberek száma
   - annak a valószínűsége, hogy egy ebbe a csoportba tartozó vásárló megvesz valamit, amire nincs szüksége, ha látja
   - melyik termékeket szeretné eleve megvenni

## Manipulálás

Az egyszerűség kedvéért feltételezzük, hogy egy termékcsoportot akkor lát egy vásárló, ha azon a soron van legalább egy másik termékcsoport, amiből akar vásárolni. Ebben az esetben a megadott valószínűséggel megvesz ott egy terméket. Szintén az egyszerűség kedvéért feltételezhetjük, hogy az egy termékcsoportban lévő termékek közül egyenletes eloszlás szerint választnak és csak egy terméket, így ha vásárolnak, akkor a keletkezett (manipulált) többletbevételt tekinthetjük egy darab átlagos termékárnak abból a termékcsoportból.

Szintén az egyszerűség kedvéért feltételezzük, hogy a kasszához való beállás nem eredményez az ahhoz tartozó soron ilyesmit. Nem foglalkozunk azzal sem, hogy egy soron belül melyik termékcsoport hol van, vagy hogy a sorok milyen sorrendben vannak egymás mellett, hogy lehet végigmenni rajtuk, stb.


## Példa bemenet

```ampl
param nRows         :=   6;
param cashierCount  :=   1;
param cashierLength := 2.5;
param maxRowLength  :=   4;

set ProductGroups := Group1	Group2	Group3	Group4	Group5	Group6	Group7	Group8	Group9	Group10	Group11	Group12	Group13	Group14	Group15	Group16	Group17	Group18	Group19	Group20;

param:
                space   averagePrice:=
    Group1	    0.94	282.00
    Group2	    1.12	108.00
    Group3	    0.21	226.00
    Group4	    1.99	264.00
    Group5	    0.70	103.00
    Group6	    0.47	180.00
    Group7	    0.32	219.00
    Group8	    0.86	140.00
    Group9	    1.10	262.00
    Group10	    1.86	127.00
    Group11	    0.18	146.00
    Group12	    0.07	142.00
    Group13	    0.23	152.00
    Group14	    1.55	228.00
    Group15	    1.23	231.00
    Group16	    1.97	123.00
    Group17	    0.68	208.00
    Group18	    1.31	94.00
    Group19	    0.38	93.00
    Group20	    0.56	268.00
;

set MustBeTogether := (Group1,Group2) , (Group12,Group8), (Group9,Group6), (Group3,Group2);
set MustBeSeparated := (Group19,Group20), (Group18,Group16), (Group13,Group11);

set CustomerGroups := CGroup1 CGroup2 CGroup3 CGroup4 CGroup5 CGroup6 CGroup7 CGroup8;

param :
            count   probabilityToBuy :=
    CGroup1	32234	0.171868755564931
    CGroup2	54057	0.006530116263574
    CGroup3	57460	0.296577903833505
    CGroup4	28400	0.218939432473207
    CGroup5	25697	0.235654179732287
    CGroup6	39766	0.239887826996717
    CGroup7	34504	0.032609542717186
    CGroup8	28175	0.165773679595818
;


param buys (tr) :
            CGroup1	CGroup2	CGroup3	CGroup4	CGroup5	CGroup6	CGroup7	CGroup8 :=
    Group1	0	    1	    0	    1	    0	    0	    0	    0
    Group2	0	    0	    0	    0	    0	    0	    0	    0
    Group3	1	    1	    0	    0	    0	    0	    1	    1
    Group4	1	    1	    0	    0	    0	    0	    0	    0
    Group5	1	    0	    0	    0	    0	    1	    0	    0
    Group6	0	    0	    1	    0	    0	    0	    0	    0
    Group7	0	    1	    1	    1	    0	    0	    0	    0
    Group8	1	    1	    0	    0	    0	    0	    0	    0
    Group9	0	    0	    0	    1	    1	    0	    0	    1
    Group10	0	    1	    0	    0	    1	    0	    1	    1
    Group11	0	    1	    1	    0	    0	    1	    0	    0
    Group12	1	    1	    1	    0	    0	    0	    0	    0
    Group13	0	    1	    1	    0	    1	    0	    0	    0
    Group14	0	    1	    1	    0	    1	    0	    0	    0
    Group15	1	    0	    1	    0	    1	    1	    0	    0
    Group16	0	    1	    0	    0	    1	    0	    0	    1
    Group17	0	    1	    0	    0	    1	    0	    0	    0
    Group18	0	    0	    1	    0	    1	    0	    0	    1
    Group19	0	    0	    0	    0	    1	    0	    0	    0
    Group20	0	    1	    0	    0	    0	    0	    1	    0
;
```

## Ellenőrzés

Ennek a szintnek az ellenőrzése manuálisan történik. Egyrészt azért, mert a megvalósítás minőségén múlik az, hogy négyest, vagy ötöst érdemel-e a kód. Másrészt nálam most több mint negyed órája fut a `glpsol` és még mindig van 7.6% gap:

```
Time used: 1020.1 secs.  Memory used: 217.9 Mb.
+3700251: mip =   1.150311899e+08 <=   1.238165285e+08   7.6% (156403; 24195)
+3711974: mip =   1.150311899e+08 <=   1.238116038e+08   7.6% (156930; 24289)
+3724329: mip =   1.150311899e+08 <=   1.238066442e+08   7.6% (157449; 24383)
+3736844: mip =   1.150311899e+08 <=   1.238012925e+08   7.6% (157945; 24477)
```

Kérem, hogy a "bepróbálkozásokat" kerüljük. Ez alatt értem az olyan kódot, ami
 - szintaktikai hibás
 - nem tudja legenerálni a modellt a megadott `data.dat`-tal
 - egyértelműen nem mutat érdemi haladást az alapszinthez képest.

# Github Actions

Ha valaki leforkolja ezt a repót, majd felpusholja a megoldását, akkor 4 CI teszt fog lefutni:
  - helyes megoldások tesztelése az alapfeladatra
  - modellgenerálás szintaktikai tesztje a kibővített feladatra