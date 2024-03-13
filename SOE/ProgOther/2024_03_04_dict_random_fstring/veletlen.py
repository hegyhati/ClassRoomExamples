import random
import matplotlib.pyplot as plt

hanyszor = [0] * 18

for _ in range(1_000_000):
    kocka = random.randint(1,6)
    kocka2 = random.randint(1,6)
    kocka3 = random.randint(1,6)
    hanyszor[kocka+kocka2+kocka3-1] += 1

for potty in range(1,7):
    print(f"{potty}-et {hanyszor[potty-1]} alkalommal dobtunk.")

plt.bar(range(1,19), hanyszor)
plt.show()