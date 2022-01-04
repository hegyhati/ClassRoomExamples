# Írj programot, mely kiírja a 42-nél nagyobb számokat a `my_list` listából. A megadott kódrészletet ne módosítsd, az csak csinál egy véletlenszerű listát, hogy ne kelljen a bemenetről bekérni.


import random

def feladat1():
    my_list = [ random.randint(1,100) for _ in range(random.randint(5,10)) ]
    print(my_list)
    # Ide ird a kododat

    for i in my_list:
        if i > 42:
            print(i)


#Írj egy `once_if_repeated` függvényt, mely egy szót vár, és 
# - ha a szó úgy néz ki, hogy egy szó megismételve kétszer, akkor térjen vissza a felével
# - különben térjen vissza az eredeti szóval

def once_if_repeated(szo):
    felhossz = len(szo)//2
    if szo[:felhossz] == szo[felhossz:]:
        return szo[:felhossz]
    else:
        return szo

print( once_if_repeated('blabla') ) # bla
print( once_if_repeated('rotor') ) # rotor
print( once_if_repeated('xyxyx') ) # xyxyx
print( once_if_repeated('xyxy') )  # xy