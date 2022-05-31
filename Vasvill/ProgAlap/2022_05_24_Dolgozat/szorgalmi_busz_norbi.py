"""
Irj programot, mely generalja perc buszmegallo menetrendjet.

A mukodeshez valositsd meg az alabbi fuggvenyt, ami visszaadja azoknak az idopontoknak a listajat, amikor elmperc ott a busz.
Harom parametert kap:
 - perc lista, amiben az indulasi idok vannak a lenti mintanak megfelelo modon.
 - perc szotar, amiben minden megallohoz adott, hogy mennyi ido alatt er oda a busz.
 - a megallo neve
"""

indulas = [ '8:10', '8:40', '9:20' , '10:00']
megallok = { 'Sopron' : '0:00', 'Banfalva': '0:10', 'Gorbehalom': '0:25', 'Brennbergbanya': '0:35' }

def idopontok(indulas, megallok, megallo):
    erkezesek = []
    okes = []
    for indul in indulas:
        indul = indul.split(':')
        indul = list(map(int, indul))
        megallok1 = megallok[megallo]
        megallok1 = megallok1.split(':')
        megallok1 = list(map(int, megallok1))
        ora = indul[0] + megallok1[0]
        if  indul[1] + megallok1[1] < 60:
          perc = indul[1] + megallok1[1]
        else:
          perc = indul[1] + megallok1[1]
          perc -= 60
          ora += 1
        erkezesek.append(ora)
        erkezesek.append(perc)
    
    erkezesek = list(map(str, erkezesek))    
    for idx in range(len(erkezesek)):
        if len(erkezesek[idx]) < 2 :
            erkezesek[idx] = '0' + erkezesek[idx]
    x = 0
    for i in range(len(indulas)):
        okes.append(erkezesek[x]+':'+erkezesek[x+1])
        x += 2
    return okes
        


for megallo in megallok:
  print(f"{megallo}: {idopontok(indulas, megallok, megallo)}")


 
"""
A kimenet ilyesmi:
Sopron: [ '8:10', '8:40', '9:20' ]
Banfalva: [ '8:20', '8:50', '9:30' ]
Gorbehalom: [ '8:35', '9:05', '9:45' ]
Brennbergbanya: [ '8:45', '9:15', '9:55' ]
"""

