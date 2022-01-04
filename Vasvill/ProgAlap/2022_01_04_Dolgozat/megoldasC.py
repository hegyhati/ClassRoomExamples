

import random

def feladat1():
    # Írj programot, mely kiírja a negatív számokat a `my_list` listából. A megadott kódrészletet ne módosítsd, az csak csinál egy véletlenszerű listát, hogy ne kelljen a bemenetről bekérni.

    my_list = [ random.randint(-100,100) for _ in range(random.randint(5,10)) ]
    print(my_list)
    # Ide ird a kododat
    for x in my_list:
        if x < 0:
            print(x)


# Írj egy `strip_repeated_front_letter` függvényt, mely egy szót vár, és visszaadja úgy, hogy ha az elején ugyanaz a karakter volt ismételve többször, akkor csak egy maradjon belőle.

def strip_repeated_front_letter_1(szo):
    while len(szo) > 1 and szo[0] == szo[1]:
        szo = szo[1:]
    return szo

def strip_repeated_front_letter_2(szo):
    return szo[0] + szo.lstrip(szo[0])

def strip_repeated_front_letter_3(szo):
    idx=0
    while idx+1 < len(szo) and szo[idx] == szo[idx+1]:
        idx+=1
    return szo[idx:]

def feladat2():
    print( strip_repeated_front_letter('nnnno') ) # no
    print( strip_repeated_front_letter('rRrRrR') ) # rRrRrR
    print( strip_repeated_front_letter('...') ) # .
    print( strip_repeated_front_letter('vege') )  # vege
