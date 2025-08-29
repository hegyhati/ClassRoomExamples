import random


def kiir(domino):
    print("+---+---+")
    print("| "+str(domino["bal"])+" | "+str(domino["jobb"])+" |")
    print("+---+---+")


def egymashoz_pakolhatok(bal_domino, jobb_domino):
    return bal_domino["jobb"] == jobb_domino["bal"]

def megfordit(domino):
    domino["bal"],domino["jobb"]=domino["jobb"],domino["bal"]


def veletlen_domino():
    return {"bal": random.randint(1, 6), "jobb": random.randint(1, 6)}


domino1 = {
    "bal": 1,
    "jobb": 4
}



domino3 = veletlen_domino()


kiir(domino1)
print()
kiir(domino3)
if egymashoz_pakolhatok(domino1, domino3):
    print("Osszerakhatok")
else:
    print("Nem osszerakhatok")
    megfordit(domino3)
    if egymashoz_pakolhatok(domino1, domino3):
        print("Megforditva osszerakhatok")
    else:
        print("Megforditva sem rakhatok ossze")
