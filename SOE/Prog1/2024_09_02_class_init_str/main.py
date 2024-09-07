Akos = {
    "dmg" : 2,
    "hp" : 13,
    "max_hp" : 20
}

Attila = {
    "dmg" : 1,
    "hp" : 39,
    "max_hp" : 40
}

def attack(attacker:dict, defender:dict):
    defender["hp"] -= attacker["dmg"]

def heal(person):
    person["hp"] += 10
    
def fullheal(person):
    person["hp"] = person["max_hp"]

def level_up(person):
    person["max_hp"] += 10
    fullheal(person)



Attila["haircolor"] = "white"