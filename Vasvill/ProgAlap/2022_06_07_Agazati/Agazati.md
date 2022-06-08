# Ágazati vizsga feladatsor 
2022.06.07.

## 1. Feladat (8 pont)

Írjon programot, mely bekéri, hogy hány csapat nevezett az iskolai focibajnokságba. Ha csak 1, akkor írja ki, hogy nem lesznek meccsek. Ha több, akkor írja ki a program, hány focimeccs lesz, hogyha minden csapat mindegyik másikkal pontosan egyszer játszik. 

Példa kimenet-bemenet párok:
 - `2` -> `1 meccs lesz.`
 - `1` -> `Nem lesznek meccsek.`
 - `5` -> `10 meccs lesz`
 - `10` -> `45 meccs lesz`

## 2. feladat (13 pont)
Készítsen programot, mely bekér néhány vesszővel elválasztott számot. Szóközök tetszőleges mennyiségben előfordulhatnak bárhol, és feltételezhető, hogy legalább egy számot megadott a felhasználó. A program ezután írja ki, hogy hány olyan szám van, amit pontosan egyszer adott meg a felhasználó, és mik ezek.

Példa bemenet-kimenet párok:
 - `1,2,2,3,3,3,4,5,5` -> `2 db: 1 4`
 - `  1    ,    2 ,  3 ` -> `3 db: 1 2 3`
 - `2,          2` -> `0 db:`

A kimenet tetszőlegesen tördelhető, a fenti egy minta. A programot nem kell hibás bemenetre felkészíteni. 

## 3. feladat (19 pont)
Adott egy `soproni_jelzesek.json` fájl, amiben a következő szerkezetben találhatók az adatok:
```json
[
    {
        "jelzes" : "Z",
        "POI" : ["Erzsébet kert", "Lőver uszoda", "Deák kút", ...]
    },
    {
        "jelzes" : "K△",
        "POI" : ["Szívszanatórium", "Dalos-kő", "Károly-kilátó", "Trianon emlékmű"]
    },
    {
        "jelzes" : "S",
        "POI" : ["Szívszanatórium", "Trianon emlékmű", "Hét-bükkfa", ...]
    },
    ...
]
```
Írjon egy függvényt (`get_Trails`), mely paraméterként kap egy POI nevet, és visszaadja azon turistajelzések listáját (`list[str]` típus), amik áthaladnak rajta.

Az alábbi kóddal működjön együtt a függvény:
```python
for poi in ["Károly kilátó", "Hétbükkfa", "Valéta", "Erdő Háza", "Vasvilla"]:
    print(f"{poi}-t érintő jelzések: {', '.join(get_Trails(poi))}")
```
Melyre a helyes kimenet:
```
Károly kilátó-t érintő jelzések: Z△, K△, S△
Hétbükkfa-t érintő jelzések: K, K+, S
Valéta-t érintő jelzések: K, S
Erdő Háza-t érintő jelzések: Z, K
Vasvilla-t érintő jelzések: 
```

Oldja meg, hogy a program akkor se okozzon hibát, ha a fájl nem létezik, hanem ezt írja ki, majd szabályosan érjen véget.
