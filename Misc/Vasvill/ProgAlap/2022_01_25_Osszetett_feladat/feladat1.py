def load_animals(filename):
    # Kenguru csapat kódja
    return animal_list

def print_animal(animal):
    # Zsiráf csapat kódja
    pass


animals = load_animals('animals.json')
print('A következő állatokkal lehet játszani majd:')
for animal in animals:
    print_animal(animal)