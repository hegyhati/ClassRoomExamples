## 1. pótzárthelyi feladat

Egy okostelefon alkalmazás-használati statisztikáit elemző parancssoros Python programot kell készíteni.

### Indítás

A program indításkor kérje be az évszámot és a hónap sorszámát, majd töltse be az adatokat az ennek megfelelő nevű (`yyyy-mm.json`) fájlból.

A JSON fájlban egy tömb van a napi statisztikákkal.
Minden naphoz adott a dátum (`"date": "yyyy-mm-dd"`), a hét napjának indexe (0-6, pl. kedd esetén `"weekday": 1`), és az egyes appokban töltött idő (`"usage"` objektum).
Utóbbinak a kulcsai az appok nevei, az értékei pedig a használati idő percekben (pl.: `"TikTok": 39`).

Az adatok betöltése után írja ki a teljes havi használati időt, a napi értékek minimumát és maximumát dátumokkal, majd jelenjen meg a főmenü.

Példa:

```
Évszám: 2024
Hónap sorszáma: 3
2024-03.json betöltve!
Összes használati idő: 5542 perc
Minimum: 2024-03-16 71 perc
Maximum: 2024-03-21 293 perc

Lehetőségek:
1: Napi átlagok
2: Összesítés appok szerint
3: Összesítés kategóriák szerint
0: Kilépés
Válasszon menüpontot: 
```

Az 1-3 menüpontok esetén jelenítse meg a választott statisztikákat, majd térjen vissza a főmenübe.

### 1: Napi átlagok

Írja ki, hogy a hét napjain mennyi az átlagos napi alkalmazás-használat (egész percre kerekítve).
*Figyelem! A hónapban lehetnek csonka hetek, így a napok előfordulási számai eltérhetnek!*

Példa:

```
Válasszon menüpontot: 1
Hétfő: 159 perc
Kedd: 150 perc
Szerda: 172 perc
Csütörtök: 232 perc
Péntek: 215 perc
Szombat: 141 perc
Vasárnap: 182 perc

Lehetőségek:
1: Napi átlagok
2: Összesítés appok szerint
3: Összesítés kategóriák szerint
0: Kilépés
Válasszon menüpontot: 
```

### 2: Összesítés appok szerint

Jelenítse meg, hogy az egyes appok hány percig voltak használva a hónap során.
Az alkalmazások használati idő szerint csökkenő sorrendben legyenek felsorolva.

Példa:

```
Válasszon menüpontot: 2
Terraria: 453 perc
WhatsApp: 398 perc
X: 339 perc
PlayStore: 325 perc
Phone: 322 perc
Twitch: 310 perc
Stardew Valley: 289 perc
...

Lehetőségek:
1: Napi átlagok
2: Összesítés appok szerint
3: Összesítés kategóriák szerint
0: Kilépés
Válasszon menüpontot: 
```

### 3: Összesítés kategóriák szerint

Az alkalmazások kategorizálva vannak az `apps.json` fájlban: a kulcsok a kategóriák nevei, az értékek a kategóriába tartozó appok neveinek listái.
Minden app pontosan egy kategóriába tartozik.

Összesítse a használati időket az egyes kategóriákra, és jelenítse meg az összegeket.

Példa:

```
Válasszon menüpontot: 3
Használat kategóriák szerint:
social: 1600 perc
multimedia: 990 perc
finance: 467 perc
gaming: 1209 perc
navigation: 0 perc
other: 1276 perc

Lehetőségek:
1: Napi átlagok
2: Összesítés appok szerint
3: Összesítés kategóriák szerint
0: Kilépés
Válasszon menüpontot: 
```
