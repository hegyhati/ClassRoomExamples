import os
from sys import argv

targynev = argv[1]

if os.path.exists(targynev):
    print("Ezzel a nevvel mar van konyvtar (vagy file), nem lehet letrehozni.")
    exit()
    
os.mkdir(targynev)
os.mkdir(os.path.join(targynev,"Jegyzetek"))
os.mkdir(os.path.join(targynev,"Korabbi zh-k"))
os.mkdir(os.path.join(targynev,"Cheat sheets"))
os.mkdir(os.path.join(targynev,"Hazifeladatok"))
os.mkdir(os.path.join(targynev,"Felvetelek"))
os.mkdir(os.path.join(targynev,"Felvetelek","eloadasok"))
os.mkdir(os.path.join(targynev,"Felvetelek","gyakorlatok"))
os.mkdir(os.path.join(targynev,"Felvetelek","egyeb"))


