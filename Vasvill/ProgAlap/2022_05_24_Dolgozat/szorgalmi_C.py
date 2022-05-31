# C csoport 
#  nyissa meg ujra, es irja ki, hogy ki futott a legtobb km-t, ha tobben is, akkor mindegyik nevet irja ki. 


def km(futasok, futo):
    tav = 0
    for futas in futasok:
        if futo in futas['runners']:
            tav += futas['distance']
    return tav

def osszes_futo(futasok):
    futok = []
    for futas in futasok:
        futok+=futas['runners']
    return list(set(futok))

import json
import random


#fajlnev = input("Kerem adja meg a fajlt: ")
fajlnev = 'futok.json'
try:
    with open(fajlnev) as f:
        futasok = json.load(f)    
except FileNotFoundError:
    print("Sorry, nincs ilyen fajl.")
    exit()

for futas in futasok:
    futas['distance'] = random.uniform(5.5,20)    

with open(fajlnev, "w") as f:
        json.dump(futasok,f)    

with open(fajlnev,) as f:
    futasok = json.load(f)

futok = osszes_futo(futasok)
print("Az osszes futo: ", futok)

tavok = []
for futo in futok:
    tavok.append(km(futasok,futo))

legnagyobb = 0
for futo in futok:
    if legnagyobb < km(futasok,futo):
        legjobb = futo
        legnagyobb = km(futasok, futo)

print(legjobb, legnagyobb)
