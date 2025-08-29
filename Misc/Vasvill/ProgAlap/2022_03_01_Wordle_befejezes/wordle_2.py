import json
import random

zold   = '\033[1;37;42m'
sarga  = '\033[1;30;43m'
normal = '\033[0;37;40m'

def eredmeny_kiiras(sikeresseg, lepesszam):
    if sikeresseg:
        print(f'Gratulalok, nyertel {lepesszam} lepesbol')
    else:
        print('Vesztettel, legkozelebb.')

def helyes_tipp_beker():
    valasz = input(f'Kerem a kovetkezo tippet: ')
    while valasz not in szolista: 
        valasz = input('Ez nem jo, ertelmes 5 hosszu magyar szonak kell lennie! Adj ujat: ')
    return valasz

def visszajelzes(tippelt_szo, kitalalando_szo):
    for idx in range(len(tippelt_szo)):
        if tippelt_szo[idx] == kitalalando_szo[idx]:
            print(zold + tippelt_szo[idx] + normal, end='')
        elif tippelt_szo[idx] in kitalalando_szo:
            print(sarga + tippelt_szo[idx] + normal, end='')
        else:
            print(tippelt_szo[idx], end='')
    print()

nyelv = input('Milyen nyelven jatszanal? en/hu')

with open(f'wordlist_{nyelv}.json') as f:
    szolista = json.load(f)

titkos = random.choice(szolista)
print(titkos)
sikerult = False
hanyadikra = 0

while hanyadikra < 6:
    tipp = helyes_tipp_beker()
    visszajelzes(tipp,titkos)
    hanyadikra += 1
    if tipp==titkos:
        sikerult = True
        break

eredmeny_kiiras(sikerult,hanyadikra)

