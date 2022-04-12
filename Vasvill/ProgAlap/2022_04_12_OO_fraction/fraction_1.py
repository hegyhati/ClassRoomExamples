def lko(a,b):
    a, b = max(a,b), min(a,b)
    if a % b == 0:
        return b
    else:
        return lko(b,a%b)

class Tort:
    szamlalo = 1
    nevezo = 1

    def __init__(self, szamlalo, nevezo) -> None:
        self.szamlalo = szamlalo
        self.nevezo = nevezo
    
    def egyszerusites(self):
        oszto = lko(self.szamlalo, self.nevezo)
        self.szamlalo //= oszto
        self.nevezo //= oszto

    def kiir(self):
        print(f"{self.szamlalo} / {self.nevezo}")
    
    def hozzaad(self, masik_tort:"Tort"):
        uj_szamlalo = (self.szamlalo*masik_tort.nevezo + masik_tort.szamlalo*self.nevezo)
        uj_nevezo = self.nevezo * masik_tort.nevezo
        eredmeny = Tort(uj_szamlalo, uj_nevezo)
        eredmeny.egyszerusites()
        return eredmeny

    


t1 = Tort(1,2)
t2 = Tort(1,2)
t3 = t1.hozzaad(t2)
t3.kiir()


