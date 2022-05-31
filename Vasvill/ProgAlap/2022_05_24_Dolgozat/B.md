# Dolgozat - B csoport
2022.05.24.

## 1. Feladat

Írj programot, mely generál három véletlen egész számot 1 és 1000 között, majd kiírja, hogy a nagyobbik nagyobb-e a két kisebb összegénél.


## 2. feladat 
Készíts programot, mely bekér néhány (legalább 1) vesszővel elválasztott szót és kiírja azokat tetszőleges tagolással, amik visszafele is ugyanazok.

 - `alma, 12, kék, 3, pap` -> `kék 3`
 - `gereblye, 1, 212, körte` -> `1 212`

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
Írj egy függvényt (`lazy_runners`), mely megkap egy dátumot, valamint futók egy listáját, és visszaadja listában azokat, akik azon a napon nem futottak. A függvény dobjon `ValueError`-t, ha a megadott dátumon nem volt futás.

Az alábbi kóddal működjön együtt a függvény:

```python
import random

runners = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ]

for _ in range(5):
  test = random.sample(runners, k=5)
  for date in ['2018.11.27', '2018.11.28']:
    try:
      print(f"A {date}-i futáson a következő futók nem voltak ott: { lazy_runners(date,test) } .")
    except ValueError:
      print(f"{date}: nem volt aznap futás.")

```