import random


class Domino:
    bal = 1
    jobb = 1

    def __init__(self, bal=random.randint(1,6), jobb=random.randint(1,6)):
        self.bal = bal
        self.jobb = jobb
        
    def kiir(self):
        print("+---+---+")
        print("| "+str(self.bal)+" | "+str(self.jobb)+" |")
        print("+---+---+")

    def megfordit(self):
        self.bal, self.jobb = self.jobb, self.bal

    def jobbrol_hozzapakolhato(self, domino):
        return self.jobb == domino.bal

d1 = Domino(1,2)
d2 = Domino()

d1.kiir()
d2.kiir()

if d1.jobbrol_hozzapakolhato(d2):
    print("egymashoz pakolhatok")
else:
    print("nem pakolhatok egymashoz")
    d2.megfordit()
    if d1.jobbrol_hozzapakolhato(d2):
        print("egymashoz pakolhatok megforditva")
    else:
        print("megforditva sem pakolhatok egymashoz")
