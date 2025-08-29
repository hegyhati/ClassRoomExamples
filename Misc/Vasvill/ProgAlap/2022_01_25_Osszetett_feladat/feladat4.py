def load_animals(filename):
    # Kenguru csapat 1. kódja
    return animal_list

def print_animal(animal):
    # Zsiráf csapat 1. kódja
    pass

def clone_animal(animal):
    # Tücsök csapat 2. kódja
    return clone

def random_animal(animal_list):
    # Kenguru csapat 2. kódja
    return cloned_animal

def random_animal_list(animal_list, count):
    # Zsiráf csapat 2. kódja
    return cloned_animal_list

def print_army(army):
    # Tücsök csapat 2. kódja
    pass


def is_alive(animal):
    # Tücsök csapat 3. kódja
    pass


def animal_fight(animal1, animal2):
    # Kenguru csapat 3. kódja
    pass

def animal_fight_til_death(animal1, animal2):
    # Kenguru csapat 3. kódja
    return fight_count


def bury_dead(army):
    # Tücsök csapat 4. kódja
    pass

def is_defeated(army):
    # Kenguru csapat 4. kódja
    pass

def battle_and_bury(army1, army2):
    # Zsiráf csapat 4. kódja

def battle_til_defeat(army1, army2):
    # Közös 4. kód


animals = load_animals('animals.json')
army1 = random_animal_list(animals,10)
army2 = random_animal_list(animals,10)
battle_til_defeat(army1,army2)
