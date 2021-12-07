# 2. Kerjunk `a_0`, `d`-t es `n`-et. Irjuk ki a szamtani sorozat elso n elemet. Pl. `5 3 10` ⟶ `5 8 11 14 17 20 23 26 29 32` 


a0 = int(input("Mi a szamtani sorozat elso eleme? "))
d  = int(input("Mi a szamtani sorozat differenciaja? "))
n  = int(input("Hany elemet irjuk ki a szamtani soroozatnak? "))

aktualis = a0
print(aktualis)

for _ in range(n-1):
    aktualis += d
    print(aktualis)
