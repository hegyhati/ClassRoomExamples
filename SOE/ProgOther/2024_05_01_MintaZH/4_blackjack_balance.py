"""
Rozsi hasonlo modon jatszik, mint Peti, csak batrabb, meg 8-nal is dob egyet. Elkezdnek egymas ellen jatszani. Minden korben mindkettejuk reszerol 1 Ft a tet. Ha:
 - mindketten vesztnek, akkor a bank viszi el a 2 Ft-ot. 
 - egyikojuk veszit, akkor a masik viszi el a 2 Ft-ot.
 - egyik sem veszit, de valamelyikojuk kozelebb van a 11-hez, az viszi a 2 forintot
 - egyikojuk sem veszit, es ugyanannyival allnak meg, visszakapjak az 1-1 forintjukat

 - **a)** Irj egy programot, mely egyetlen jatekot szimulal, es leirja, hogy a fenti 4 kozul mi lett a vegeredmeny.
 - **b)** Irj programot, mely a fenti jatekot 100x lejatsza egymas utan, majd egy vonaldiagrammon abrazolja Peti, Rozsi es a bank egyenleget. (mindegyik 0-rol indul).

"""

import random

from matplotlib import pyplot as plt


peti_balance = 0
rozsi_balance = 0
bank = 0

peti_history = [peti_balance]
rozsi_history = [rozsi_balance]
bank_history = [bank]

for _ in range(100):
    peti_balance -= 1
    rozsi_balance -= 1
    
    peti_sum = 0
    while peti_sum <= 7: 
        peti_sum += random.randint(1,6)
    rozsi_sum = 0
    while rozsi_sum <= 8: 
        rozsi_sum += random.randint(1,6)
    
    if peti_sum > 11 and rozsi_sum > 11: bank += 2
    elif peti_sum > 11: rozsi_balance += 2
    elif rozsi_sum > 11: peti_balance += 2
    elif peti_sum > rozsi_sum: peti_balance += 2
    elif rozsi_sum > peti_sum: rozsi_balance += 2
    else:
        peti_balance += 1
        rozsi_balance += 1
    
    peti_history.append(peti_balance)
    rozsi_history.append(rozsi_balance)
    bank_history.append(bank)


plt.plot(peti_history, label="Peti egyenlege")
plt.plot(rozsi_history, label="Rozsi egyenlege")
plt.plot(bank_history, label="Bank")

plt.show()
