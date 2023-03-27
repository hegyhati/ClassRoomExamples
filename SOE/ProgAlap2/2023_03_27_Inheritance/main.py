from army import Army
from warrior import Agile_Warrior, Shielded_Warrior, Warrior

orcs = Army()
elves = Army()

orcs.recruit(Warrior("Grog",20,5))
orcs.recruit(Warrior("Balrog",20,5))
orcs.recruit(Agile_Warrior("Shelob",20,5))

elves.recruit(Warrior("Legolas",50,6))
elves.recruit(Warrior("Lego lass",10,2))
elves.recruit(Shielded_Warrior("Legless Legolas",20,1,2))

orcs.battle(elves)
