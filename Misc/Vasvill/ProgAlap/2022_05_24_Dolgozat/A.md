# Dolgozat - A csoport
2022.05.24.

## 1. Feladat

Írj programot, mely generál két véletlen egész számot 1 és 1000 között, majd kiírja, hogy a kisebbik osztója-e a nagyobbiknak.


## 2. feladat 
Készíts programot, mely bekér néhány (legalább 1) vesszővel elválasztott szót és kiírja azokat tetszőleges tagolással, amik magánhangzóra végződnek.

 - `alma, 12, kés, 3, pap` -> `alma`
 - `gereblye, 1, 2, körte` -> `gereblye körte`

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
Írj egy függvényt (`more_diligent`), mely 2 futó nevét kapja, és visszaadja, hogy kettőjük közül ki volt a legtöbbször futni. Ha ugyanannyiszor futottak, adja vissza az elsőt. Ha valamelyik futó egyszer sem volt, dobjon a függvény `ValueError`-t.

Az alábbi kóddal működjön együtt a függvény:

```python
for r1 in ['D', 'O', 'G']:
    for r2 in ['C','A','M','X']:
      try:
        print(f"{r1} és {r2} közül { more_diligent(r1,r2) } futott többször.")
      except ValueError:
        print(f"{r1} és {r2} közül valaki egyszer sem futott.")

```