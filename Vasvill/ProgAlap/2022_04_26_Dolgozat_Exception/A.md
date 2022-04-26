# Dolgozat - A csoport
2022.04.26.

## 1. Feladat

Írj programot, mely bekér egy 100 és 999 közötti számot, és kiírja a számjegyeinek összegét.
 - `123` -> `6`
 - `519` -> `15`


## 2. feladat 
Készíts programot, mely bekér néhány (legalább 1) vesszővel elválasztott szót és kiírja (tetszőleges módon tagolva) a legrövidebbeket. A szavak előtt és után tetszőlegesen sok szóköz lehet. 

 - `alma, körte, kés, szék, pap` -> `kés pap`
 - `gereblye` -> `gereblye`

## 3. feladat
Adott egy `futok.json` fájl, amiben a következő szerkezetben találhatók az adatok arról, hogy melyik futáson (dátum) kik voltak ott (futók nevei: A, B, C, ...):
```json
[
  {
    "date": "2018.11.27",
    "runners": ["A", "B", "C"]
  },
  {
    "date": "2018.12.04",
    "runners": ["D", "A", "B", "E"]
  },
  ...
]

```
Írj egy függvényt (`exactly_one`), mely két futó nevét kapja, és visszaadja listában azokat a dátumokat, amikor pontosan az egyikőjük volt ott futáson.

Az alábbi kóddal működjön együtt a függvény:

```python
for r1 in ['D', 'O', 'G']:
    for r2 in ['C','A','M']:
        print(f"{ len(exactly_one(r1,r2)) } db olyan futás volt, ahol {r1} és {r2} közül pontosan az egyik volt ott.")
```