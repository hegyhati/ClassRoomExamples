#!/usr/bin/python3  

import os

os.chdir('save')
saves = os.listdir()

print("Melyik mentest toltsuk be?")
for save in saves:
    if os.path.isfile(save) and os.path.splitext(save)[1] in [".yasff" , ".txt"]:
        print(" - {}".format(save))

selected = input()

if os.path.exists(selected) and os.path.isfile(selected):
    file = open(selected)
    name = file.read()
    file.close()

    print("Hello {}".format(name))
else:
    print("Nincs ilyen mentes, bb")
