# Dolgozat 2 - A csoport
2021.12.14.

A dolgozat első két feladata papíros, erre 10-15 perc áll rendelkezésre. A programozós feladatokra így 30-35 perc marad.

## Mit ír ki az alábbi program? (5p)
```python
l = [1,3,5,6,3,4,5,6,4,2,1,4]
a = 0
while a != 4:
    print(l[a])
    a = l[a]
```

## Melyik állítás(ok) igaz(ak)? (3p)
 - `'alma'[1:2:3] == 'a'`
 - Egy függvénynek lehet 2 argumentuma.
 - `'ALMa'.lower() == 'almA'`


## Programozás - 1 (4p)

Írj programot, mely kiírja a páros számokat a `my_list` listából. A megadott kódrészletet ne módosítsd, az csak csinál egy véletlenszerű listát, hogy ne kelljen a bemenetről bekérni.

```python
import random
my_list = [ random.randint(1,100) for _ in range(random.randint(5,10)) ]
print(my_list)
# Ide ird a kododat
```
## Programozás - 2 (6p)

Írj egy `strip_if_same` függvényt, mely egy szót vár, és 
 - visszaadja ezt a szót, ha nem egyezik meg az első és utolsó karaktere
 - visszaadja az első és utolsó karakter lecsípéséből álló szót, ha azok megegyeznek.

```python
# Ide ird a fuggveny kodjat
print( strip_if_same('alma') )  # lm
print( strip_if_same('almak') ) # almak
print( strip_if_same(' alma') ) #  alma
print( strip_if_same('kerek') )  # ere
```