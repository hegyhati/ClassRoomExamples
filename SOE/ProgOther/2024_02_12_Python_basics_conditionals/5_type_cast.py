nev1 = input("Hogy hivnak? ")
kor1 = int(input("Hany eves vagy? ")) # int-re konvertalas nelkul nem vart eredmeny 6 vs 14 esetben!
nev2 = input("Hogy hivnak? ")
kor2 = int(input("Hany eves vagy? "))

if kor1 > kor2:
    print(nev1 + " az oregebb")
else:
    print(nev2 + " az oregebb")
