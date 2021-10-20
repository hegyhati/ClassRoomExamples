#  1. Kerjunk be egy szamot, irjuk ki az osztoit. Pl.: `12` ⟶ `1 2 3 4 6 12`

num = int(input("Kerem a szamot: "))

for divider in range(1,num+1):
    if num % divider == 0:
        print(divider)
