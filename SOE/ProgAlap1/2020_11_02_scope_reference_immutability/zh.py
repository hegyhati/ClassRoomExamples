percek = []
sms=[]

for honap in range(12):
    percek.append(int(input()))
    sms.append(int(input()))

havidij=int(input())
percdij=int(input())
smsdij=int(input())

szamla=[]
total=0

for honap in range(12):
    mennyilenne=percdij*percek[honap] + smsdij * sms[honap]
    if mennyilenne > havidij: 
        szamla.append(mennyilenne)
    else:
        szamla.append(havidij)

for sz in szamla:
    total+=sz

print(szamla)
print(total)



    