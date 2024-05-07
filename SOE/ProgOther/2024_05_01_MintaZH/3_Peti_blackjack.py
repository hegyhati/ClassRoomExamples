"""

## 3. Peti "blackjackezik"
Peti egy blackjack szeru jatekot jatszik dobokockaval. A jatek lenyege, hogy a jatekos dobokockaval dob, es a dobott szamok osszege minel kozelebb kell legyen 11-hez, de alulrol. Ha tullepi, akkor automatikusan vesztett. 

Peti strategiaja, hogy dob addig, amig az eddigi osszeg 7 vagy az alatt van, es "megall" ha atlepte. Nehany elofordulo scenario:
 - Elso dobas 6, masodik dobas 2, Peti megall 8-cal.
 - Elso dobas 2, masodik dobas 5, harmadik dobas 3, Peti megall 10-zel.
 - Elso dobas 6, masodik dobas 6, Peti vesztett.

Irj programot, ami lejatszik 1000 jatekot, majd egy torta diagrammon abrazolja, hogy hanyszor vesztett Peti. 

"""

import random
import matplotlib.pyplot as plt

total = 1000
lose = 0

for _ in range(total):
    sum = 0
    while sum <= 7:
        sum += random.randint(1,6)
    if sum > 11: lose += 1

plt.pie([lose, total-lose], labels=["Peti vesztett", "Peti \"idoben megallt\""])
plt.show()
