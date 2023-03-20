from building import Building
from person import Person

gt = Building("GT")
gt.new_office(capacity = 2)
gt.new_office(capacity = 3)
gt.new_office(capacity = 1)

people = [
    Person("Varga Jozsef"),
    Person("Szabo Lajos", chitchat=True),
    Person("Nagy Jozsef"),
    Person("Kiss Jozsef", chitchat=True),
    Person("Toth Jozsef", chitchat=True),
    Person("Kovacs Jozsef"),
    Person("Varga Tamas"),
    Person("Varga Laszlo", chitchat=True)
]

for person in people:
    gt.sit_down(person)

gt.print_offices()