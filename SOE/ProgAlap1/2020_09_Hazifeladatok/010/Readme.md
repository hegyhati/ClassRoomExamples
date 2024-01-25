# ZH

A program célja, hogy kiszámolja, mennyibe kerülne nekünk egy  előfizetéses mobilcsomag az éves telefonálási, sms-ezgetési adataink alapján.
Ebben a leegyszerűsített esetben egy csomagot három egész szám ír le:
  - havidíj, ami teljes mértékben lebeszélhető
  - percdíj (mindenhova)
  - SMS díj (mindenhova)

Szintén az egyszerűsítés végett feltételezhető, hogy minden hónapban valahány egész percet telefonálunk. Azt is tudjuk, hogy a teljes havidíj telefonálásra, SMS-ezésre felhasználható, viszont nyilván akkor is ki kell fizetnünk, ha be sem kapcsoltuk a telefonunkat.

Tehát például ha a havidíj 1000 Ft, a percdíj 50 Ft, az SMS díj 100 Ft, akkor 5 perc és 1 SMS után is 1000 forintot kell fizetni. Viszont ha beszélünk 8 órát, de nem küldünk SMS-t, akkor az 2400 Ft.

A program először kérjen be 24 egész számot, melyek tartalmazzák, hogy:
1. Januárban hány percet telefonáltunk
2. Januárban hány SMS-t küldtünk
3. Februárban hány percet telefonáltunk
4. Februárban hány SMS-t küldtünk
5. Márciusban...

Ezt követően 3 egész számot kérjünk be:
1. A csomag havidíja
2. A csomag percdíja
3. A csomag SMS díja

Ezután a program egy listában írja ki, hogy melyik hónapban mennyit fizettünk, illetve utána a teljes évi költséget.

Pelda bemenet:
```
121
40
187
48
272
11
246
6
43
39
283
30
126
39
105
31
109
3
202
5
261
42
296
12
1000
16
15
```

És a hozzá tartozó kimenet:

```
[2536, 3712, 4517, 4026, 1273, 4978, 2601, 2145, 1789, 3307, 4806, 4916]
40606
```
