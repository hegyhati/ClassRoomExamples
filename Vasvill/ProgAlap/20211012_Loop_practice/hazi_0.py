# 0. Kerjunk be ket szamot. Csinaljunk listat a ket szam kozotti szamookbol novekvo sorrendben. Pl.: `6 11` ⟶ `[6, 7, 8, 9, 10, 11]`

egyik = int(input("Kerem az egyik szamot: "))
masik = int(input("Kerem a masik szamot: "))

if egyik < masik:
    kisebb = egyik
    nagyobb = masik
else:
    kisebb = masik
    nagyobb = egyik

# elso mod
lista = [kisebb]
while lista[-1] != nagyobb:
    lista.append(lista[-1]+1)
print(lista)


# masodik mod
lista2=[]
aktualis = kisebb
while aktualis != nagyobb:
    lista2.append(aktualis)
    aktualis += 1
print(lista2)

# harmadik mod
lista3 = list(range(kisebb,nagyobb+1))
print(lista3)

