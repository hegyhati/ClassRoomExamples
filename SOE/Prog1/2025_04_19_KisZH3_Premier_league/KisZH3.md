# KisZH3
2025.04.03.

## Adatok
A [Premier_league](Premier_league/) könyvtárban minden angol csapatnak van egy alkönyvtára, amiben a csapat játékosaihoz tartozik 1-1 fájl. 
A fájlok elnevezése a következő formátumú: `NUM_NAME_NAT.json`, ahol:
 - `NUM` a mezszám
 - `NAME` a játékos családneve
 - `NAT` a játékos nemzetisége

## Feladat
Írjon programot, mely bemenetről bekér egy nemzetiséget.  
Ezek után a program a kimenetre az alábbi formában kiírja az összes olyan focistát, aki ahhoz a nemzetiséghez tartozik, az alábbi formában:

```
Groß - Brighton-and-Hove-Albion (13)
Gündogan - Manchester-City (8)
Koch - Leeds-United (5)
Shabani - Wolverhampton-Wanderers (57)
Karius - Liverpool (22)
Rüdiger - Chelsea (2)
Werner - Chelsea (11)
Havertz - Chelsea (29)
Leno - Arsenal (1)
Özil - Arsenal (10)
Mustafi - Arsenal (20)
Meyer - Crystal-Palace (7)
```

## Kezelendő hibák
A `Premier_league` könyvtárban előfordulhatnak egyéb fájlok is a könyvtárakon kívül.
