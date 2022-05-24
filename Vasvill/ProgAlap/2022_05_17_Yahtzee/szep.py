import random

def k6():
    return random.randint(1,6)

def kezdodobas():
    return [ k6() for _ in range(5) ]

def ujradobas(dobasok):
    for kocka_idx in input("Melyik kockakkal szeretnel ujradobni? ").split(','):
        dobasok[int(kocka_idx)-1] = k6()


dobasok = kezdodobas()
print(dobasok)
for _ in range(2):
    ujradobas(dobasok)
    print(dobasok)