from character import Character

hero = Character("Jonathan", 30, 4)
monster = Character("Vampire lord", 50, 2)

while hero.is_alive() > 0 and monster.is_alive() >0:
    hero.attack(monster)
    monster.attack(hero)

print(hero,monster)
