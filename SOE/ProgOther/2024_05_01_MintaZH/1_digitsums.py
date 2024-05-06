"""

## 1. Szamjegy osszegek
 - **a)** Keszits programot, mely beolvas egy szamot, es kiirja a szamjegyeinek az osszeget.
 - **b)** Egeszitsd ki a programot azzal, hogy ha negativ szamot adnak meg, akkor kerjen addig ujra, amig nemnegativ egeszet nem kap. (Arra nem kell felkesziteni a programot, hogy tortek, nem szamok esetet lekezelje.)
 - **c)** Miutan kiszamolta a szamjegyek osszeget a pogram, ismetelje ezt addig, amig egyjegyu szamhoz nem jutunk, es kozben irja is ki ezeket. Pl.: 2024 -> 8, vagy 1989 -> 27 -> 9
 
"""
number = -1

while number < 0:
    number = int(input("Adj egy nemnegativ egesz szamot: "))

while True: 
    print(number)
    digitsum = 0
    for digit in str(number):
        digitsum += int(digit)
    if digitsum == number:
        break
    else:
        number = digitsum