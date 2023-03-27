from random import choice

class Warrior:
    
    def __init__(self, name:str, health:int, damage:int) -> None:
        self._name = name
        self._health = health
        self._damage = damage
        self._check_dead()

    def __str__(self) -> str:
        return f"{self._name} (HP: {self._health}, DMG: {self._damage})"

    def _check_dead(self) -> None:
        if self._health < 0:
            self._health = 0
    
    def is_alive(self) -> bool:
        return self._health > 0

    def receive_damage(self, attack_points:int):
        self._health -= attack_points
        self._check_dead()

    def attack(self, defender : 'Warrior', silent=False) -> None:
        if self.is_alive():
            if not silent: print(f"{self} attacks {defender} and makes {self._damage} damage")
            defender.receive_damage(self._damage)
        else:
            if not silent: print(f"{self} cannot attack, because pepsi")
    
    def attack_til_death(self, defender: 'Warrior'):
        while self.is_alive() and defender.is_alive():
            self.attack(defender, silent=True)
            defender.attack(self, silent=True)

class Shielded_Warrior(Warrior):
    def __init__(self, name:str, health:int, damage:int, defense:int =0) -> None:
        super().__init__(name,health,damage)
        self._defense = defense

    def __str__(self) -> str:
        return f"{self._name} (HP: {self._health}, DMG: {self._damage}, DEF: {self._defense})"

    def receive_damage(self, attack_points:int):
        attack_points -= self._defense
        if attack_points > 0:
            self._health -= attack_points
            self._check_dead() 

class Agile_Warrior(Warrior):
    def __init__(self, name: str, health: int, damage: int) -> None:
        super().__init__(name, health, damage)
        self.__avoid_next=choice([True,False])
    
    def receive_damage(self, attack_points: int):
        if not self.__avoid_next:
            return super().receive_damage(attack_points)
        self.__avoid_next = not self.__avoid_next


    

    
