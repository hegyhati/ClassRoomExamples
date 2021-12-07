# Minta dolgozat 2
2021.11.29.

A dolgozat első két feladata papíros, erre 10-15 perc áll rendelkezésre. A programozós feladatokra így 30-35 perc marad.

## Mit ír ki az alábbi program?
```python
l = [1,'a',3,'b',2,'a']
for i in range(0,4,2):
    print(l[i+1] * l[i])
```

## Melyik állítás(ok) igaz(ak)?
 - `string[a:b:c]` esetén `str[c]` mindig ki lesz írva.
 - Egy függvénynek lehet 0 argumentuma.
 - `dict` pakolható `list`-be, de `list` nem lehet `dict`-ben kulcshoz rendelt érték.
 - `dict`-ből `dictionary[key] = None` -nal törüljük ki a `key` kulcsot és a hozzá tartozó értéket.


## Programozás - 1

Írj programot, mely bekér két szót, majd kiírja az összes olyan betűt, ami mindkettőben előfordul.

## Programozás - 2

Ugyanígy bekér két szót, de az összes olyan karaktersorozatot írja ki, mely mindkettőben előfordul. pl: `kalap,paplan -> a,l,la,ap`

## Programozás - 3 

Kérjük be egy ház szobáinak méreteit egy `input`-tal a következő módon, majd írjuk ki a szobák számát és a ház teljes területét. Pl.:
`4x2,6x3,3x3,5x4 -> 4 szoba, 55 nm`

