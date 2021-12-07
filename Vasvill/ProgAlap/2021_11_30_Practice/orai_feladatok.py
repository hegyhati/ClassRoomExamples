# Orai feladat


#  1. Kerjunk be egy derekszogu haromszog ket befogojat, irjuk ki az atfogot.

def atfogo(a, b):
    return (a*a + b**2) ** 0.5


def feladat_1():
    a = float(input("Kerem az egyik befogot: "))
    b = float(input("Kerem a masik befogot: "))
    print("A haromszog atfogoja:", atfogo(a, b))


#  2. Kerjunk be egy szot, mondjuk meg, hogy massalhangzobol vagy maganhangzobol van-e benne tobb.

def szamlalo(szo, betulista):
    darab = 0
    for c in szo:
        if c in betulista:
            darab += 1
    return darab


def szamlalo2(szo, betulista):
    darab = 0
    for betu in betulista:
        darab += szo.count(betu)


def feladat_2():
    szo = input("Kerem a szot:")
    mgh_szam = szamlalo(szo.lower(), ['e', 'u', 'i', 'o', 'a'])
    egyeb_szm = szamlalo(szo, [' ', ',', '.', '!', '?', ':', '-', '"'])
    msh_szam = len(szo)-mgh_szam-egyeb_szm
    print("Maganhangzok szama:", mgh_szam)
    print("Massalhangzok szama:", msh_szam)


#  3. Kerjunk be ket szot, irjuk ki a leghosszabb kozos prefixuket.

def feladat_3():
    szo1 = input("Kerem az elso szot: ")
    szo2 = input("Kerem a masodik szot: ")
    hossz = 0
    while szo1[hossz] == szo2[hossz]:
        hossz += 1
    print("Leghosszabb kozos prefix:", szo1[:hossz])

#  5. Kerjunk be 3 hosszt, irjuk ki, hogy szerkesztheto-e belole haromszog.


def feladat_5():
    a = float(input())
    b = float(input())
    c = float(input())

    if c < a+b and a < b+c and b < a+c:
        print("Szerkesztheto")
    else:
        print("Nem szerkesztheto")

    l = [a, b, c]
    l.sort()
    print("Szerkesztheto" if l[2] < l[1] + l[0] else "Nem szerkesztheto")
