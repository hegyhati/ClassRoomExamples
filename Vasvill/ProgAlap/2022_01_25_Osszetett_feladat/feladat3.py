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


animals = load_animals('animals.json')
animal1 = random_animal(animals)
animal2 = random_animal(animals)
print('Akik megcsatáznak:')
print_animal(animal1)
print_animal(animal2)
fight_count = animal_fight_til_death(animal1,animal2)
print(f"A csata {fight_count} ütközet után zárult:")
if is_alive(animal1):
    print('A győztes: ', end='')
    print_animal(animal1)
elif is_alive(animal2):
    print('A győztes: ', end='')
    print_animal(animal2)
else:
    print('Mindkét állat elpatkolt.')

