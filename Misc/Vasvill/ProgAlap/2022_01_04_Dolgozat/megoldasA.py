# Írj programot, mely kiírja a páros számokat a `my_list` listából. A megadott kódrészletet ne módosítsd, az csak csinál egy véletlenszerű listát, hogy ne kelljen a bemenetről bekérni.

import random

def feladat1():
    my_list = [ random.randint(1,100) for _ in range(random.randint(5,10)) ]
    print(my_list)
    # Ide ird a kododat
    for i in my_list:
        if i%2 == 0:
            print(i)

#Írj egy `strip_if_same` függvényt, mely egy szót vár, és 
# - visszaadja ezt a szót, ha nem egyezik meg az első és utolsó karaktere
# - visszaadja az első és utolsó karakter lecsípéséből álló szót, ha azok megegyeznek.


def strip_if_same(szo):
    if szo[0] == szo[-1]:
        szo = szo[1:-1]
    return szo

def feladat2():
    print( strip_if_same('alma') )  # lm
    print( strip_if_same('almak') ) # almak
    print( strip_if_same(' alma') ) #  alma
    print( strip_if_same('kerek') )  # ere
    print( strip_if_same("aaaaaaaaaaaaaaaaaaaaaala")) # aaaaaaaaaaaaaaaaaaaaal