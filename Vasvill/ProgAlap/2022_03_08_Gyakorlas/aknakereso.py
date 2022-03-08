def kirajzol(tablazat): 
    for sor in tablazat:
        for mezo in sor:
            if mezo:
                print(f"{mezo:5}", end='')
            else:
                print("???? ", end='')
        print()

def ures_tabla(sorszam, oszlopszam):
    tablazat = []
    for sor in range(sorok_szama):
        tablazat.append([])
        for oszlop in range(oszlopok_szama):
            tablazat[-1].append(None)
    return tablazat

import random
def bombat_lepakol(tablazat):
    sor = random.randrange(len(tablazat))
    oszlop = random.randrange(len(tablazat[0]))
    tablazat[sor][oszlop] = 'Bomb'


sorok_szama = int(input('Sorok szama: '))
oszlopok_szama = int(input('Oszlopok szama: '))
bombak_szama = int(input('Oszlopok szama: '))

tabla = ures_tabla()
for _ in range(bombak_szama):
    bombat_lepakol(tabla)

kirajzol(tabla)