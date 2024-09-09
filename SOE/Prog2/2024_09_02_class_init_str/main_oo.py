class Adventurer:
    _alive = True
        
    def __init__(self, dmg:int, max_hp:int):
        self._dmg = dmg
        self._max_hp = max_hp
        self._hp = max_hp
    
    def heal(self, heal_amount  = 10):
        self._hp += heal_amount
        if self._hp > self._max_hp:
            self._hp = self._max_hp
    
    def attack(self, defender:"Adventurer"):
        if self._alive:
            defender._hp -= self._dmg
            if defender._hp < 0:
                defender._hp = 0
                defender._alive = False
    
    def __str__(self) -> str:
        return f"HP: {self._hp} / {self._max_hp}, DMG: {self._dmg}"
        


Akos = Adventurer(2,20)
Attila = Adventurer(1,40)

print(Attila)
Akos.attack(Attila)
print(Attila)





