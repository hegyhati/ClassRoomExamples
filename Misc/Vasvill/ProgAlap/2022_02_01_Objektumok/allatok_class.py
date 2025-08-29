import random

class Allat:
    nev = ""
    elet = 0
    tamadas = 0

    def __init__(self, nev, elet, tamadas):
        self.nev = nev
        self.elet = elet
        self.tamadas = tamadas

    def kiir(self):
        print(self.nev,"<3 "*self.elet, "/ "*self.tamadas )

    def megut(self, vedekezo):
        if self.elet > 0:
            vedekezo.elet -= self.tamadas
            if vedekezo.elet < 0:
                vedekezo.elet = 0


mokus = Allat("Chip",random.randint(3,5),random.randint(1,2))
elefant  = Allat("Dumbo",random.randint(10,15),random.randint(4,6))

mokus.kiir()
elefant.kiir()

print("Elefant meguti a mokust")
elefant.megut(mokus)
mokus.kiir()
elefant.kiir()

print("Mokus meguti az elefantot")
mokus.megut(elefant)
mokus.kiir()
elefant.kiir()
