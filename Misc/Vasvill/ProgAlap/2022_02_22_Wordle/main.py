def eredmeny_kiiras(sikeresseg, lepesszam):
    if sikeresseg:
        print(f'Gratulalok, nyertel {lepesszam} lepesbol')
    else:
        print('Vesztettel, legkozelebb.')

def helyes_tipp_beker():
    valasz = input(f'Kerem a kovetkezo tippet: ')
    while len(valasz) != 5: 
        valasz = input('Ez nem jo, 5 hosszunak kell lennie! Adj ujat: ')
    return valasz

titkos = 'thorn'
sikerult = False
hanyadikra = 0

while hanyadikra < 6:
    tipp = helyes_tipp_beker()
    hanyadikra += 1
    if tipp==titkos:
        sikerult = True
        break

eredmeny_kiiras(sikerult,hanyadikra)

