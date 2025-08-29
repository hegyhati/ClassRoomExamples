# Dolgozat - B csoport
2022.04.26.

## 1. Feladat

Írj programot, mely bekér egy 100 és 999 közötti számot, és kiírja a legnagyobb számjegyét.
 - `123` -> `3`
 - `519` -> `9`


## 2. feladat 
Készíts programot, mely bekér néhány (legalább 1) vesszővel elválasztott szót és kiírja (tetszőleges módon tagolva) a leghosszabbakat. A szavak előtt és után tetszőlegesen sok szóköz lehet. 

 - `alma, körte, kés, szék, pap` -> `körte`
 - `hal, dal, fal,út` -> `hal dal fal`

## 3. feladat
Adott egy `futok.json` fájl, amiben a következő szerkezetben találhatók az adatok arról, hogy melyik futáson (dátum) kik voltak ott (futók nevei A, B, C, ...):
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
Írj egy függvényt (`ran_together`), mely egy futó nevét kapja, és visszaadja listában azokat a futókat, akikkel már futott együtt, mindenkiét csak egyszer.

Az alábbi kóddal működjön együtt a függvény:

```python
for r in 'ABCDEFGHIJKLMNO':
        print(f"{r} összesen {len(ran_together(r))} másik futót ismer futásokról.")
```