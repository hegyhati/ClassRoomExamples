# Programozás alapjai 2. - PótZH
2021.04.16.

## 0. Bevezető
A feladat egy olyan alkalmazás elkészítése, ami az általunk teljesített teljesítménytúrákat menedzseli, érdekes statisztikát mutat meg róla.

A programunk egyelőre csak a gyalogos (`hiking`), valamint kerékpáros (`cycling`) túrákat kezeli. 
A típus mellett minden túrának adott a neve, valamint az, hogy milyen hosszú volt km-ben, és hány méter szintet kellett közben mászni.

Minden ilyen túrának az adatai egy-egy JSON fájlban vannak eltárolva ilyen módon:

```json
{
    "name" : "Éjszakai Kommandó 30 km",
    "type" : "hiking",
    "distance" :  29.2,
    "climb" : 903
}
```

Vagy például egy kerékpáros túra esetén:

```json
{
    "name" : "BRM200 - Balaton kerülés 2019 200+ ",
    "type" : "cycling",
    "distance" :  210,
    "climb" : 570
}
```

Példának adott 6 ilyen fájl a [`John_Doe_2019`](John_Doe_2019/) könyvtárban.

## 1. `Activity` osztály

Az első osztályunk egy teljesítménytúrát modellez le.
Inicializáláshoz kapjon négy paramétert: típus, név, táv km-ben, szintemelkedés m-ben.

Tehát a fenti túrákat pl így lehessen kézzel létrehozni:
```python
kommando = Activity("hiking", "Éjszakai Kommandó 30 km", 29.2, 903)
brm200 = Activity("cycling", "BRM200 - Balaton kerülés 2019 200+ ",  210, 570)
```

Ez az inicializáló függvény ellenőrizze az adatokat, és ha értelmetlen adatot kap, dobjon egy `ValueError` kivételt.
Hibásak a bemeneti adatok, ha az alábbiakból legalább egy teljesül:
 - a típus nem `"hiking"` vagy `"cycling"`
 - a név üres
 - a táv nem pozitív
 - a szintemelkedés negatív

Legyen az osztálynak egy `is_of_type` függvénye, mely visszaadja, hogy a paraméterben megadott típussal rendelkezik-e a túra.

```python
kommando.is_of_type("hiking") # True
kommando.is_of_type("hike") # False
kommando.is_of_type("cycling") # False
kommando.is_of_type("running") # False
brm200.is_of_type("hiking") # False
brm200.is_of_type("hike") # False
brm200.is_of_type("cycling") # True
brm200.is_of_type("running") # False
```

Legyen az osztálnynak egy argumentum nélküli `mtsz_points` metódusa, ami visszaadja, hogy a túra hány [MTSZ pontot](http://mtsz.org/mtsz_minositesi_szabalyzat_2018-) ér.

Mi most egy egyszerűsített pontszámítással élünk:
 - Gyalogos túra esetében minden megtett km 1.5 pontot ér, szintemelkedésnél minden befejezett 100 méter 2 pontot. 
 - Kerékpáros túránál a km szorzó 0.5 és 100 méterenként 1 pont jár

Szintemelkedésre, távra, és így a teljes túrára is igaz, hogy nem járhat töredékpont. A maradékot "le kell csapni".

```python
kommando.mtsz_points() # 61
brm200.mtsz_points() # 110
```

# 2. `Calendar` osztály

Ez az osztály lesz felelős az évi teljesített túrákból való statisztikák elkészítéséért.

Inicializáláskor egyetlen argumentumot vár, egy könyvtárnevet, ahol a túrákat tartalmazó fájljaink is vannak:
```python
jd2019=Calendar("John_Doe_2019")
```

Az inicializáló függvény a következőket tegye:
 1. Lépjen be a megadott könyvtárba (feltételezhető, hogy létezik)
 2. A könyvtárban található összes JSON fájlt olvassa be, és az összes valid adatokkal rendelkezőt tárolja el egy `Activity` formájában.
 3. Más fájlok, vagy hibás adatokat tartalmazó JSON-ok ne akasszák meg a beolvasást.

Legyen az osztálynak egy `total_activity_count` függvénye, mely visszaadja, hogy hány túrán vettünk részt, valamint egy `total_distance` függvénye, mely adott típushoz megadja, hogy olyan típusból összesen hány km-t teljesítettünk.
Ha érvénytelen típus van megadva, szimplán térjen vissza 0-val.

```python
print(f"Participated in {jd2019.total_activity_count()} activities.")
for type in ["hiking","cycling","skiing"]:
    print(f" - {jd2019.total_distance(type)} km of {type}")
```

A fenti bemenetre a megadott fájlokkal ez a kimenet várható:
```
Participated in 6 activities.
 - 246.219 km of hiking
 - 210.0 km of cycling
 - 0.0 km of skiing
```

# Statisztika készítése

A `Calendar` osztálynak legyen egy `generate_statistics` függvénye, mely egy fájlnevet (pl.: `"stats.png"`) vár, és a megadott fájlba generál egy két diagrammból álló képet:
 - Az elsőn egy oszlopdiagrammon látszódjon, hogy km-ben mennyit bringáztunk, gyalogoltunk összesen.
 - A másikokon egy scatter ploton látszódjon, hogy a gyalogos túrák esetében milyen volt a távolság, szintemelkedés viszonya.

 A példakönyvtárban megadott adatok alapján például egy ilyen kép készülhet el:
 
![`John_Doe_2019/stats.png`](John_Doe_2019/stats.png)


# 4. Tesztelés

A [`main.py`](main.py)-ban egyben megtalálhatók a `Calendar`-hoz kötődő fenti kódrészletek. 
A tesztelhető függvények itt megadott tesztjeit tessék doctest-be beletenni. 