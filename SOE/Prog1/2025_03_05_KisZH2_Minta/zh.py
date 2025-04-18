"""
Írj programot, amely beolvassa a json tartalmát, majd bekéri az indulás óráját (egész szám),
és kiírja azon állomások neveit, amiket érint legalább egy olyan vonat, ami a megadott órában indul.
Minden érintett állomást csak egyszer írjon ki, tetszőleges sorrendben.
Ha nincs ilyen állomás, akkor írja ki, hogy "No trains at this time.".

Példák:

Hour of departure? 8
Destinations:
Bicske
Sopron
Fertoszentmiklos
Komarom
Tata

Hour of departure? 14
No trains at this time.
"""

import json

hour = int(input())

with open("data.json") as f:
    trains = json.load(f)

stations = set()

for train in trains:
    if hour == int(train["departure"][:2]):
        stations.update(train["stations"])

print(stations if len(stations) != 0 else "No train there.")
