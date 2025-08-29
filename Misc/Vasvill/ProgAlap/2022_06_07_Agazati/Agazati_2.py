szamok = input("Kérem a számokat vesszővel elválasztva: ").split(',')
szam_lista=[]
for szam in szamok:
    szam_lista.append(int(szam))
darab = 0
egyszer = []
for szam in szam_lista:
    if szam_lista.count(szam) == 1:
        darab += 1
        egyszer.append(szam)
print(darab,"db:")
for szam in egyszer:
    print(szam)