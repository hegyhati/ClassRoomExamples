# Dolgozat 3 - Minta
2022.03.06.

A dolgozat első feladata papíros, erre 5-10 perc áll rendelkezésre. A programozós feladatokra így 35-40 perc marad.

## Mit ír ki az alábbi program? (5p)
```python

def qwe(a,b):
    if a > b :
        return 2*a
    else:
        return a + b

for x in range(5):
    print(qwe(x+2,x**2))

```

## Programozás (8p)

Írj programot, mely beolvassa a mellékelt `szavak.json` fájlban lévő szavak listáját, és kiírja azokat, amelyekben nincsenek ismétlődő karakterek. A feladat megoldásához írj külön függvényt, mely leellenőrzi, hogy egy szóban van-e ismétlődő karakter.

```python

def van_ismetlodo_karakter(szo):
    # ide ird a kodot, ami visszater True-val, ha van ismetlodo karakter es False-szal ha nincs
    pass

# Ide ird a kodot, ami beolvassa a fajlbol a szavakat, es kiirja azokat, amikben nincsenek ismetlodo karakterek
```

## Kódjavítás (6p)

Az alábbi program vesszőkkel elválasztott számokat kér be, majd megnézi, hogy van-e köztük két olyan szám, aminek az összege 100. Ha igen, kiírja őket. Viszont több helyen hibás a program, ezeket a hibákat kell kijavítani. Pythontutort lehet (és érdemes) használni.


```python
numbers_with_commas = input()
number_list = numbers_with_commas.strip()

for number in number_list:
    for number2 in number_list:
        if number + number == 100:
            print(f"number + number2 = 100")
```

