import random
from matplotlib import pyplot as plt

dobasszam = int(input("Hany kiserletet vegezzek? "))
# hanykocka = int(input("Hany kockaval dobsz egyszerre? "))


for hanykocka in range(1,20):
    plt.cla()
    dobasossegek = []

    for _ in range(dobasszam):
        osszeg = 0
        for _ in range(hanykocka):
            osszeg += random.randint(1,6)
        dobasossegek.append(osszeg)

    minimal = hanykocka
    maximal = hanykocka*6

    x = list(range(minimal,maximal+1))
    y = []
    for osszeg in x:
        y.append(dobasossegek.count(osszeg))

    plt.bar(x,y)
    # plt.show()
    plt.savefig(f"{hanykocka}-kocka.jpg")