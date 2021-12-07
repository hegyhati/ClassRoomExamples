#  1. Kerjunk be ket szamot: `n` es `m`. Csinaljunk egy listat, amiben `m`-szer szerepel `n`. Pl.: `3 12` ⟶ `[12, 12, 12]`

elem = int(input("Mi legyen a listaba teendo elem? "))
hanyszor = int(input("Hanyszor tegyem bele a listaba? "))

lista = []

for _ in range(hanyszor):
    lista.append(elem)
    
print(lista)
