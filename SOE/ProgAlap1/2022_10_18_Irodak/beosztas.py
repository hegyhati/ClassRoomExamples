import json


with open("irodak.json") as f:
    irodak = json.load(f)

with open("beosztas.json") as f:
    beosztas = json.load(f)

ember = input("Kit akarsz leultetni?")

for iroda in irodak:
    if len(beosztas[iroda]) < irodak[iroda]:
        beosztas[iroda].append(ember)
        print(f"{ember} sikeresen leultetve {iroda} irodaba.")
        break
else:
    print("Sorry, minden iroda tele, rugj ki valakit.")

with open("beosztas.json", "w") as f:
    json.dump(beosztas, f)
    