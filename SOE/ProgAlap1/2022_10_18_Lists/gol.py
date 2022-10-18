golok = []

valasz = input("Ki lotte az elso golt? (ures valasz, ha meccs vege) ")
while valasz != "":
    golok.append(valasz)
    valasz = input("Ki lotte a kovetkezo golt? (ures valasz, ha meccs vege) ")

focistak = []
for focista in golok:
    if focista not in focistak:
        focistak.append(focista)
# focistak = set(golok) 

golkiraly = ""
maxgol = -1
for focista in focistak:
    print(focista, golok.count(focista))
    if golok.count(focista) > maxgol:
        maxgol = golok.count(focista)
        golkiraly = focista

print (f"A golkiraly {golkiraly.upper()}, {maxgol} gollal")