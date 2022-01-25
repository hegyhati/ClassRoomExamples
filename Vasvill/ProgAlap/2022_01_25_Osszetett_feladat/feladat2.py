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


animals = load_animals('animals.json')
my_army = random_animal_list(animals,10)
print_army(my_army)
