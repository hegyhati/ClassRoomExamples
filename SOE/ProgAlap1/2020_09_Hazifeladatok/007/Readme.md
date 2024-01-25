Van egy bankszámlánk, amit január 1-én 0 forintos egyenleggel nyitunk. Minden hónap elején levonásra kerül 2000 forint számlavezetési díj, kivéve januárban, azt ajándékba kapjunk a számlanyitásért. 

Hónap végén ha az egyenlegünk negatív, 10%-os kamat kerül a tartozásunkra. Ha pozitív, akkor +5%-os megtakarítás.

Kérjük be egyesével mind a 12 hónap összesített pénzmozgását, ahol pozitív érték jelöli, hogyha többet fizettünk be, mint amennyit felvettünk, és negatív, ha fordítva. Felvételi, befizetési díjaktól most eltekintünk, ha töredékforint jönne ki, a bank mindig a 0 fele kerekít.

| Hónap    | Nyitóegyenleg | Pénzmozgás | Záróegyenleg | Kamat után |
| -------- | ------------- | ---------- | ------------ |----------- |
| Január   | 0             | +3500      | 0+3500=3500  | +5% ⇨ 3675 |
| Február  | 3675          | +1000      | 3675-2000+1000=2675  |  +5% ⇨ 2808 |
| Március  | 2808          | -4000      | 2808-2000-4000=-3192 | -10% ⇨ -3511 |
| ...

A 12 egész szám beolvasása után írja ki a program először, hogy újévkor mennyi lesz az egyenlegünk, majd azt is, hogy mennyi lenne az "egyenlegünk", ha nem nyitunk számlát. (Feltételezhetjük, hogy kaptunk volna rokontól kamatmentes kölcsönt, amikor/ha negatívba kényszerülünk.)

A fenti három hónap után például ez volna a kimenet:
```
-3511
500
```



