# Dolgozat - C csoport
2022.04.26.

## 1. Feladat

Írj programot, mely bekér egy 100 és 999 közötti számot, és kiírja a legkisebb számjegyét.
 - `123` -> `1`
 - `519` -> `1`


## 2. feladat 
Készíts programot, mely bekér néhány (legalább 1) vesszővel elválasztott szót és kiírja (tetszőlegesen tagolva) a páros sok magánhangzót tartalmazókat. A szavak előtt és után tetszőlegesen sok szóköz lehet. 

 - `alma, körte, kés, szék, pap` -> `alma körte`
 - `gereblye` -> ` `

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
Írj egy függvényt (`together`), mely két futó nevét kapja, és visszaadja listában azokat a dátumokat, amikor mindkettejük ott volt a futáson.

Az alábbi kóddal működjön együtt a függvény:

```python
for r1 in ['D', 'O', 'G']:
    for r2 in ['C','A','M']:
        print(f"{r1} és {r2} pontosan { len(together(r1,r2)) } alkalommal futott együtt.")
```