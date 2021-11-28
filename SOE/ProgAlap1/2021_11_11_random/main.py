import random

szin = ["makk", "piros", "zold", "tok"]
szam = ["VII", "VIII", "IX", "X", "also", "felso", "kiraly", "asz"]

pakli = [ (x,y) for x in szin for y in szam]

pakli = list(range(10))

print(pakli)

random.shuffle(pakli)

print(pakli)
