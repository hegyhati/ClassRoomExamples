from warrior import Warrior


class Army:
    def __init__(self) -> None:
        self.warriors = []
    
    def recruit(self, warrior:Warrior) -> None:
        self.warriors.append(warrior)

    def battle(self, other_army:'Army') -> None:
        while len(self.warriors) > 0 and len(other_army.warriors) > 0:
            print(f" {self.warriors[0]} vs. {other_army.warriors[0]} ")
            self.warriors[0].attack_til_death(other_army.warriors[0])
            if not self.warriors[0].is_alive():
                self.warriors.pop(0)
                print(f"   {other_army.warriors[0]} is victorious!")
            if not other_army.warriors[0].is_alive():
                other_army.warriors.pop(0)
                print(f"   {self.warriors[0]} is victorious!")
