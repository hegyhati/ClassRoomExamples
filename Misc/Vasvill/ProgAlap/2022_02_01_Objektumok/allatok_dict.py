def allat_kiir(allat):
    print(allat['nev'],"<3 "*allat['elet'], "/ "*allat['tamadas'] )

def allat_megut(tamado:dict,vedekezo):
    vedekezo['elet'] -= tamado['tamadas']

lo = {
    'nev' : 'Roach',
    'elet' : 5,
    'tamadas' : 2
}

macska = {
    'nev' : 'Cirmi',
    'elet' : 9,
    'tamadas' : 4 
}

allat_kiir(lo)
allat_kiir(macska)
allat_megut(lo,macska)
allat_kiir(lo)
allat_kiir(macska)

