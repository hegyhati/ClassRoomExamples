"""

## 2. Szamjegyosszeg statisztika
Irj programot, mely 0-tol 10<sup>6</sup>-ig minden szamra vegrehajtja az 1. feladatban leirt algoritmust, es feljegyzi, hogy hany sorozat vegzodott 0-ban, 1-ben, .., 9-ben. Ez legyen egy oszlopdiagrammon abrazolva, melyet `digitsums.png` neven mentse el a program.

"""

count = [0] * 10

for number in range(1, 10**6+1):
    while True: 
        digitsum = 0
        for digit in str(number):
            digitsum += int(digit)
        if digitsum == number: break
        else: number = digitsum
    count[number] += 1

import matplotlib.pyplot as plt

plt.bar(height=count, x=range(10))

plt.savefig("digitsums.png")