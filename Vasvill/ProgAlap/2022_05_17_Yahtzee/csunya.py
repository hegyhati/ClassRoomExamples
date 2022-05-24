import random

dobasok = []
for _ in range(5):
    dobasok.append(random.randint(1,6))
print(dobasok)

ujradobasok = input("Melyik kockakkal szeretnel ujradobni? ") #1, 3, 4
ujralista = ujradobasok.split(',') # ["1", " 3", " 4"]
for idx in range(len(ujralista)):
    ujralista[idx] = int(ujralista[idx])
for kocka_idx in ujralista:
    dobasok[kocka_idx-1] = random.randint(1,6)
print(dobasok)

ujradobasok = input("Melyik kockakkal szeretnel ujradobni? ")
ujralista = ujradobasok.split(',')
for idx in range(len(ujralista)):
    ujralista[idx] = int(ujralista[idx])
for kocka_idx in ujralista:
    dobasok[kocka_idx-1] = random.randint(1,6)
print(dobasok)
