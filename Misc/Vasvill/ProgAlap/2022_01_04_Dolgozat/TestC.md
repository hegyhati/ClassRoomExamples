# Dolgozat 2 - C csoport
2021.12.14.

A dolgozat első két feladata papíros, erre 10-15 perc áll rendelkezésre. A programozós feladatokra így 30-35 perc marad.

## Mit ír ki az alábbi program? (5p)
```python
l = [1,3,5,6,3,4,5,6,4,2,1,4]
a = 7
for _ in range(5):
    print(a)
    a -= l[a]
```

## Melyik állítás(ok) igaz(ak)? (3p)
 - `'alma'[0:3:2] == 'am'`
 - Egy függvényben kötelező legalább egy `return` -nek lennie.
 - `'alma'.split('m') == ['al', 'a']`


## Programozás - 1 (4p)

Írj programot, mely kiírja a negatív számokat a `my_list` listából. A megadott kódrészletet ne módosítsd, az csak csinál egy véletlenszerű listát, hogy ne kelljen a bemenetről bekérni.

```python
import random
my_list = [ random.randint(-100,100) for _ in range(random.randint(5,10)) ]
print(my_list)
# Ide ird a kododat
```
## Programozás - 2 (6p)

Írj egy `strip_repeated_front_letter` függvényt, mely egy szót vár, és visszaadja úgy, hogy ha az elején ugyanaz a karakter volt ismételve többször, akkor csak egy maradjon belőle.

```python
# Ide ird a fuggveny kodjat
print( strip_repeated_front_letter('nnnno') ) # no
print( strip_repeated_front_letter('rRrRrR') ) # rRrRrR
print( strip_repeated_front_letter('...') ) # .
print( strip_repeated_front_letter('vege') )  # vege
```