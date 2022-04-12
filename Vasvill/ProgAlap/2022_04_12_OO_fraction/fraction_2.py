def lko(a,b):
    a, b = max(a,b), min(a,b)
    if a % b == 0:
        return b
    else:
        return lko(b,a%b)

class Tort:

    def __init__(self, szamlalo=1, nevezo=1, szoveg = "") -> None:
        if szoveg == "":
            self.szamlalo = szamlalo
            self.nevezo = nevezo
        else:
            szamok = szoveg.split('/')
            self.szamlalo = int(szamok[0])
            self.nevezo = int(szamok[1])
        self.egyszerusites()
    
    def egyszerusites(self):
        oszto = lko(self.szamlalo, self.nevezo)
        self.szamlalo //= oszto
        self.nevezo //= oszto

    def __str__(self):
        return f"{self.szamlalo} / {self.nevezo}"
    
    def __add__(self, masik:"Tort"):
        szamlalo = (self.szamlalo*masik.nevezo + masik.szamlalo*self.nevezo)
        nevezo = self.nevezo * masik.nevezo
        return Tort(szamlalo, nevezo)
    
    def csini_kiiratas(self):
        szelesseg = max(len(str(self.szamlalo)),len(str(self.nevezo)))+2
        print(f"{self.szamlalo:^{szelesseg}}")
        print("-"*szelesseg)
        print(f"{self.nevezo:^{szelesseg}}")



tort1 = Tort(szoveg=input("Adj meg egy tortet a/b alakban: "))
tort2 = Tort(szoveg=input("Adj meg egy masik tortet a/b alakban: "))
print(f"{tort1} + {tort2} = {tort1 + tort2} ")

(tort1 + tort2).csini_kiiratas()