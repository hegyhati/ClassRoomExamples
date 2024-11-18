Trivialis lenne felveni egy `width{Plane}` es `height{Plane}` valtozot, ezeket hasznalni a 4 lefedo korlatozasban, azonban be kellene allitani, hogy a terulet nem lepheti at a megadottat, azaz valami ilyesmi:

```ampl
s.t. Max_Area{p in Planes}:
    width[p] * height[p] <= area;
```

Ez azonban mar nem linearis. Ezert a megoldasban gyakorlatilag az elozore vezetunk vissza annyival, hogy a lehetseges mereteket diszkretizaljuk. Bevezetodik egy `minStep` parameter, ami megadja, hogy a szelesseg hanyasaval novekedhet, es akkor ehhez mar kiszamolhato a megfelelo magassag. Azaz az elozo megoldasban levo `Areas` setet, es a hozza tartozo parametereket automatikusan generaljuk:


```ampl

param area;
param minStep default 1; 
param areaCount integer := area / minStep;
set Areas := 1..areaCount;
param areaWidth{a in Areas} := a * minStep;
param areaHeight{a in Areas} := area / a / minStep;

```