import random
import matplotlib.pyplot as plt

kiserlet_szam = int(input("Hanyszor dobjak? "))
kocka = int(input("Hany oldalu dobokockaval dobjak?"))


for kockaszam in range(1,11):

    eredmenyek = []

    for _ in range(kiserlet_szam):
        osszeg = 0
        for _ in range(kockaszam):
            osszeg += random.randint(1,kocka)
        eredmenyek.append(osszeg)
        
    legkisebb = kockaszam
    legnagyobb = kockaszam * kocka 

    statisztika = {}
    for eredmeny in range(legkisebb, legnagyobb+1):

        statisztika[eredmeny] = eredmenyek.count(eredmeny)

    plt.cla()
    plt.bar(statisztika.keys(), statisztika.values())
    plt.title(f"{kiserlet_szam} kockadobas eredmenye {kockaszam} db d{kocka} kockaval")
    plt.savefig(f"{kiserlet_szam}_{kockaszam}_d{kocka}.jpg", dpi=200)