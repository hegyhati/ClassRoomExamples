import random


pilots = [
    {
        "firstname" : "Max",
        "lastname" : "Verstappen",
        "age" : 23,
        "wins" : [ "2023", "2022", "2021"]
    },
    {
        "firstname" : "Michael",
        "lastname" : "Schumacher",
        "wins" : [ "1994", "1995", "2000", "2001", "2002", "2003", "2004"]
    }
]

for pilot in pilots:
    print( pilot["firstname"] + " " + pilot["lastname"] + " had won Formula 1 in years " + ", ".join(pilot["wins"]) + ".")
    print("{} {} had won Formula 1 in years {}.".format(
        pilot["firstname"],
        pilot["lastname"],
        ", ".join(pilot["wins"])
    ))
    print(f'{pilot["firstname"]} {pilot["lastname"]} had won Formula 1 in years {", ".join(pilot["wins"])}.')
    
print("Random pilota:")
pilot = random.choice(pilots)
print(pilot)