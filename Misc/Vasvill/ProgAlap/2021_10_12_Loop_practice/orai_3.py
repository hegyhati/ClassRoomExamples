# 2. Kerjunk `a_0`, `d`-t es `n`-et. Irjuk ki a szamtani sorozat elso n elemet. Pl. `5 3 10` ⟶ `5 8 11 14 17 20 23 26 29 32`
# 3. u.a. csak tegyuk listaba. Pl.  `5 3 4` ⟶ `[5, 8, 11, 14]`

a0 = int(input("Mi a szamtani sorozat elso eleme? "))
d = int(input("Mi a szamtani sorozat differenciaja? "))
n = int(input("Hany elemet irjuk ki a szamtani soroozatnak? "))

sorozat = [a0]

for _ in range(n-1):
    sorozat.append(sorozat[-1] + d)

print(sorozat)
