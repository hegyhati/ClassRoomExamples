from math import sin, cos, pi


class Teknoc:
    x = 0
    y = 0
    szog = 90

    def elore(self, mennyit):
        self.x += int(mennyit * cos(self.szog * pi / 180))
        self.y += int(mennyit * sin(self.szog * pi / 180))

    def jobbra(self, mennyivel):
        self.szog -= mennyivel

    def balra(self, mennyivel):
        self.szog += mennyivel

    def kiir(self):
        print(self.x, self.y, self.szog)


t1 = Teknoc()

t1.kiir()
t1.elore(100)
t1.jobbra(90)
t1.kiir()
t1.elore(100)
t1.jobbra(90)
t1.kiir()
t1.elore(100)
t1.jobbra(90)
t1.kiir()
t1.elore(100)
t1.jobbra(90)
