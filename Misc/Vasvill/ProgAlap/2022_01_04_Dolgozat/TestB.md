# Dolgozat 2 - B csoport
2021.12.14.

A dolgozat első két feladata papíros, erre 10-15 perc áll rendelkezésre. A programozós feladatokra így 30-35 perc marad.

## Mit ír ki az alábbi program? (5p)
```python
l = [1,3,5,6,3,4,5,6,4,2,1,4]
a = 3
while l[a] != 2:
    print(a+l[a])
    a += 2
```

## Melyik állítás(ok) igaz(ak)? (3p)
 - `'alma'[1:3:2] == 'la'`
 - Egy függvényben csak egy `return` szerepelhet.
 - `'ALMa'.upper() == 'ALMA'`


## Programozás - 1 (4p)

Írj programot, mely kiírja a 42-nél nagyobb számokat a `my_list` listából. A megadott kódrészletet ne módosítsd, az csak csinál egy véletlenszerű listát, hogy ne kelljen a bemenetről bekérni.

```python
import random
my_list = [ random.randint(1,100) for _ in range(random.randint(5,10)) ]
print(my_list)
# Ide ird a kododat
```
## Programozás - 2 (6p)

Írj egy `once_if_repeated` függvényt, mely egy szót vár, és 
 - ha a szó úgy néz ki, hogy egy szó megismételve kétszer, akkor térjen vissza a felével
 - különben térjen vissza az eredeti szóval

```python
# Ide ird a fuggveny kodjat
print( once_if_repeated('blabla') ) # bla
print( once_if_repeated('rotor') ) # rotor
print( once_if_repeated('xyxyx') ) # xyxyxy
print( once_if_repeated('xyxy') )  # xy
```