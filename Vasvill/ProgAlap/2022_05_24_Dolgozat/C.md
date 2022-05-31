# Dolgozat - C csoport
2022.05.24.

## 1. Feladat

Írj programot, mely generál 3 véletlen számjegyet, és kiírja az ezekből készíthető legnagyobb háromjegyű számot.


## 2. feladat 
Készíts programot, mely bekér néhány (legalább 1) vesszővel elválasztott szót és kiírja azokat tetszőleges tagolással, amik olyan betűvel kezdődnek, ami többször is előfordul a szóban.

 - `alma, körte, kék, sárga, pap` -> `alma kék pap`
 - `gereblye, vizsla, Sopron, Nagykanizsa` -> `Nagykanizsa`

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
Írj egy függvényt (`all_runners`), mely visszaadja az összes futó nevét egy listában, mindegyiket csak egyszer. 

Írj egy másik függvényt (`is_fit`), mely egy futó nevét várja paraméterül, és megadja, hogy a futó volt-e legalább háromszor futni. Ha sosem volt futni az illető, dobjon `ValueError`-t.

Az alábbi kóddal működjön együtt a függvény:

```python
runners = all_runners() 
for runner in runners + ['X', 'Y']
  try:
    if is_fit(runner):
      print( f"{runner} szorgalmasan fut.")
    else:
      print( f"{runner} nem fut elég szorgalmasan.")
  except ValueError:
    print(f"{runner} egyáltalán nem fut.")

```