from random import randrange, choice, sample, randint
from json import dump
from string import ascii_uppercase

with open("data.json", "w") as f:
    dump([{
            "train_id" : id,
            "seat_resevation" : choice([True,False]),
            "departure" : f"{randrange(24):02}:{randrange(60):02}",
            "stations" : sorted(sample(ascii_uppercase, k = randint(5,15)))
        }
        for id in range(randrange(100))
    ], f, indent=2)

