import random

darab = [0] * 13

for _ in range(50000):
    dobas1 = random.randint(1, 6)
    dobas2 = random.randint(1, 6)
    darab[dobas1+dobas2] += 1

for dobas in range(len(darab)):
    print( dobas,": ",darab[dobas],"alkalommal dobtuk.")
