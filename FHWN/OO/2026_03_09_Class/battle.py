import random

class Warrior:
    __name : str
    __dmg : int
    __hp : int
    __max_hp : int
    __hit_chance : float

    def __init__(self, given_name:str, initial_health_points:int, damage:int):
        self.__name = given_name
        self.__hp = initial_health_points
        self.__max_hp = initial_health_points
        self.__dmg = damage
        self.__hit_chance = random.uniform(0.3,0.5)

    def is_alive(self) -> bool:
        return self.__hp > 0
    
    def __get_damage(self):
        return self.__dmg + random.randint(-1,1)

    def __attack(self, defender:"Warrior") -> None:
        if self.is_alive() and defender.is_alive():
            if random.uniform(0,1) < self.__hit_chance:
                defender.__hp -= self.__get_damage()

    def fight_to_death(self, the_other:"Warrior") -> "Warrior":
        if random.randint(0,1) == 1:
            the_other.__attack(self)
        while self.is_alive() and the_other.is_alive():
            self.__attack(the_other)
            the_other.__attack(self)
        return self if self.is_alive() else the_other

    def full_heal(self):
        self.__hp = self.__max_hp
    
    def __str__(self) -> str:
        return f"{self.__name} ({self.__dmg} DMG, {self.__hp} / {self.__max_hp} HP)"

alive = [
    Warrior("Revy", 100, 15),
    Warrior("Dutch", 120, 12),
    Warrior("Benny", 80, 8),
    Warrior("Rock", 90, 10),
    Warrior("Balalaika", 130, 18),
    Warrior("Mr. Chang", 110, 14),
    Warrior("Eda", 95, 11),
    Warrior("Shenhua", 105, 13)
]

round = 0
while len(alive) != 1:
    round += 1
    print(f"ROUND {round}:")
    random.shuffle(alive)  
    winners = []
    for idx in range(0,len(alive),2):
        print(f"\t{alive[idx]} vs. {alive[idx+1]}... ", end="")
        winner = alive[idx].fight_to_death(alive[idx+1])
        print(f"{winner} WINS!")
        winner.full_heal()
        winners.append(winner)
    alive = winners

print(f"""
      
THE CHAMPION: {alive[0]}

""")
    




