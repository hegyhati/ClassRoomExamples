class Unit:
    name = "Unit"
    _dmg = 0
    max_hp = 0
    hp = 0

    def __init__(self, name:str, dmg:int, max_hp:int):
        self.name=name
        self._dmg = dmg
        self.hp = self.max_hp = max_hp
    
    def is_alive(self):
        return self.hp>0
    
    def get_damage(self):
        return self._dmg
    
    def attack(self,other_unit):
        if self.is_alive() and other_unit.is_alive():
            damage = self.get_damage()
            other_unit.hp -= damage
            return damage
        return 0
    
    def print(self):
        print("{} HP: {}/{} DMG:{}".format(self.name, self.hp, self.max_hp, self._dmg))

class Player(Unit):
    xp=0

    def attack(self, other_unit):
        self.xp += super().attack(other_unit)
        if self.xp > 10:
            self.xp = 0
            self._dmg += 1
            self.max_hp+=5
            self.hp = self.max_hp

class DoubleWielder(Player):
    round = True
    _dmg2 = 0

    def __init__(self, name, dmg, dmg2, max_hp):
        Unit.__init__(self,name, dmg, max_hp)
        self._dmg2 = dmg2

    def get_damage(self):
        if self.round:
            return self._dmg
        else:
            return self._dmg2
        self.round = not self.round

sanyi = DoubleWielder("Alexander the great",3,7,10)
sarkany = Unit("Susu",1,2000)


while sarkany.is_alive() and sanyi.is_alive():
    sanyi.print()
    sarkany.print()
    sarkany.attack(sanyi)
    sanyi.print()
    sarkany.print()
    sanyi.attack(sarkany)


print("End of battle")
sanyi.print()
sarkany.print()
