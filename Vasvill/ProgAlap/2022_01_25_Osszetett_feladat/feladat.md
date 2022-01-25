# Összetett csoportfeladat

A mai órán a feladat egy összetettebb játék közös leprogramozása. 
Alakítsatok 3 csoportot, az egyes részfeladatokat külön-külön párhuzamosan végezzétek el, majd tegyétek össze a kódokat. 
Ha minden csapat jól csinálta a dolgát, a végén tudtok játszani a játékkal.

# Az alapot adó játék

Az elkészítendő program alapötletét a [Crazy Auto Pets](https://teamwood.itch.io/super-auto-pets) nevű játék adja. 
Mi ennek egy nagyon lebutított változatát fogjuk közösen megcsinálni. 
Hogy a játéklogikát megértsétek, játszatok 1-2 kört vendégként (Play as Guest, Arena Mode).

Röviden a lényeg:
 - Vannak állatkák, mindegyiknek van egy támadása és egy életereje. A speciális képességektől, ennivalóktól, pénztől mi most eltekintünk.
 - Van két állathad, ezek küzdenek meg egymással.
 - Amikor két állat egymásnak esik, akkor mindegyiknek az életereje csökken a másik támadásával. Ha egy állat életereje 0-ra vagy az alá csökken, akkor elpusztul. 
 - Amikor két állathad csatázik, akkor mindig a legelől álló állatkák esnek egymásnak, amíg az egyik had teljesen el nem pusztul. 

Valami ilyesmit kezdünk el építgetni pici lépésekben.

# Fejlesztés

A fejlesztést több körre osztjuk, mindegyik körben minden csapatnak adott egy feladata, azt kell megoldania, majd a kódot megosztani a többiekkel, és lesz egy fő függvény, ami teszteli az addig elkészülteket.
Minden csapat csak abban a függvényben dolgozzon, ami feladatul meg van adva, a főkód nem módosítható, csak annyiban, hogy a fájl elejére beszúrható szükséges `import`.

Nem kell előre végigolvasni mindent, elég mindig csak a következő körrel foglalkozzatok.

Második óra végén küldjétek el nekem (1 ember), hogy mi az utolsó működő stabil kód. 

## Feladat 0 : csapatok kialakítása

Oszoljatok három csapatra, amit mostantól hívjunk Tücsök, Kenguru, Zsiráf csapatoknak.

## Feladat 1: alapozás

### Tücsök/1: adatgyűjtés

Ebben a körben ennek a csapatnak a legkellemesebb a feladata: amíg a többiek vadul kódolnak, Ti gyűjtsétek össze minél több állatnak az adatait, és írjátok bele az `animals.json` fájlba az ott látható szerkezetben. 
Én mintának beírtam már hármat.

### Kenguru/1: adat betöltés

Írjátok meg a `load_animals` függvényt, ami beolvassa a paraméterként megkapott fájlban található állatokat, és visszaadja azok listáját. 

### Zsiráf/1: állat adatainak kiírása

Ez a csapat a `print_animal` kódot írja meg, mely a következő formában írja ki egy megkapott állat (`animal` argumentum, ami egy dict az `animals.json` fájlban látható kulcsokkal) adatait:

```
Hangya - ⚔ / ♥♥
```
vagy pl:
```
Gorilla - ⚔⚔⚔⚔⚔⚔ / ♥♥♥♥♥♥♥♥♥
```
### Tesztelés/1

Ha mindhárom csapat végzett, akkor a `feladat1.py`-jal tudtok tesztelni, ez egyszerűen csak kiírja a fent megadott formában a json fájlba beleírt állatokat.



## Feladat 2: Toborzás

### Tücsök/2: Állat másolás

Technikailag (a mögöttes dolgokat majd megbeszéljük később) szükség lesz rá, hogy egy állatról másolatot csináljunk. Azaz csináljunk egy ugyanolyan dict-et, ugyanazokkal a kulcsokkal és adatokkal, majd azt adjuk vissza. Erre szolgál  `clone_animal` függvény, mely a kapott állatból csinál egy "klónt". (Ennek röviden az a célja, hogy ha például van két lovunk, és az egyik sebződik, akkor a másik ettől független legyen, ne ugyanazok legyenek.)

A `print_army` egyetlen paramétert vár: egy állatlistát, és írja ki a haderőt az alábbi formátumban, felhasználva a `print_animal` függvényt (és nem bemásolva annak a kódját). 

```
1. Kacsa - ⚔ / ♥♥
2. Gorilla - ⚔⚔⚔⚔⚔⚔ / ♥♥♥♥♥♥♥♥♥
3. Elefánt - ⚔⚔⚔ / ♥♥♥♥♥
```

### Kenguru/2: Véletlen had

A `random_animal` függvény egy paramétert vár, az összes lehetséges állat listáját, és adja vissza egy véletlenszerű állat **klónját**. Értelemszerűen itt használni kell a tücsök csapat függvényét is. 

### Zsiráf/2: Haderő kiírása

A `random_animal_list` függvény két paramétert vár:
 - az összes lehetséges állat listáját
 - egy létszámot
A függvény véletlenszerűen visszaad egy létszám méretű listát **klónozott** állatokból.
Itt természetesen előfordulhat az is, hogy kétszer ugyanolyan típusú állat van a listában. 
Értelemszerűen a Kenguru csapat `random_animal` függvényét kell használni itt.

### Tesztelés/2

A `feladat2.py`-ba az első kör függvényeit átmásolva, valamint a 3 újat elkészítve futtatható a főprogramban lévő teszt, mely kiír egy véletlenszerű 10 létszámú állatsereget.

## Feladat 3: alap csata

### Tücsök/3: pulzus kitapogatás

Az `is_alive` függvény egy állatot (dict) vár argumentumul, és visszaad egy `True`/`False` értéket annak megfelelően, hogy a kapott állat még életben van-e(életerő pozitív).

### Kenguru/3: egy pofoncsere

Az `animal_fight` függvény két állatot kap (dict-ekben), és ezek megütik egymást egyszer, azaz mindegyiknek csökken az életereje a másik támadásával.

### Zsiráf/3: csihipuhi a végsőkig
Az `animal_fight_til_death` függvény is két állatot kap (dict-ekben) és addig ütközteti őket az `animal_fight` függvénnyel, amíg legalább az egyikőjük el nem pusztul.
Ez a függvény mindkét másik csapat függvényét használja.
A függvény térjen vissza az ütközetek számával.

### Tesztelés/3

A `feladat3.py`-ban megadott kód két véletlenszerű állatot ütköztet egymással.

## Feladat 4: Hadak csatája

### Tücsök/4: temetés

A `bury_dead` egy haderőt vár paraméterül, ami állatoknak egy listája, és kitörli a listából azokat, amelyek már elpusztultak. 

### Kenguru/4: vereség

Az `is_defeated` egy haderőt vár paraméterül (állatok listája) és visszatér `True`-val vagy `False`-szal attól függően, hogy vereséget szenvedett-e a haderő. 
Akkor szenvedett vereséget egy haderő, ha az elpusztult állatok temetése után (Tücsök csapat kódja) senki nincs már életben.

### Zsiráf/4: csata

A `battle_and_bury` függvény két haderőt (állatlisták) vár paraméterül, és az első sorban állókat ütközteti addig, amíg valamelyik el nem esik. Itt az `animal_fight_til_death` függvényt kell használni az előző körből. 
Az ütköztetés után temessen mindkét oldalon (`bury_dead`).

### Közösen

A `battle_til_defeat` szintén két haderőt ütköztet.
Amíg mindkét oldalon vannak még csatázni képes állatok, addig:
 - írja ki, hogy áll a két csapat (`print_army`)
 - ütköztesse az elöl lévőket, amíg legalább az egyik el nem patkol, majd temessen (`battle_and_bury`)
 - írja ki, hogy hány pofonváltás történt

 ### Tesztelés/4

 A `feladat4.py`-ban készül két random 10 fős sereg, és ezeket ütköztetjük.