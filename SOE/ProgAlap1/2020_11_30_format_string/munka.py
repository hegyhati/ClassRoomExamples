def beutemez(feladat):
    kezdes = int(input("Hanyadik naptol kezdjem el a feladatot? "))
    while kezdes + feladat["idotartam"] - 1 > feladat["hatarido"]:
        kezdes = int(input("Nem jo kezdes, hataridoig nem keszulne el, adj meg uj kezdest! "))
    return {"feladat":feladat, "kezdes":kezdes}

def intervallum(munka):
    kezdes = munka["kezdes"]
    befejezes = kezdes + munka["feladat"]["idotartam"]-1
    return (kezdes,befejezes)

def kiir(munka):
    nev = munka["feladat"]["nev"]
    (kezdes,befejezes) = intervallum(munka)
    print("{:^10}: {:3}-{:<3}".format(nev,kezdes,befejezes))

def utkozik(munka1,munka2):    
    (kezdes1,befejezes1) = intervallum(munka1)
    (kezdes2,befejezes2) = intervallum(munka2)
    return not (befejezes1 < kezdes2 or befejezes2 < kezdes1)
