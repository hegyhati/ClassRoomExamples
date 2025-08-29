import json
import random

sarga = '\033[1;30;43m'
zold = '\033[1;30;42m'
normal ='\033[0;37;40m'

def eredmeny_kiiras(sikeresseg, lepesszam):
    if sikeresseg:
        print(f'Gratulalok, nyertel {lepesszam} lepesbol')
    else:
        print('Vesztettel, legkozelebb.')

def helyes_tipp_beker():
    valasz = input(f'Kerem a kovetkezo tippet: ')
    while valasz not in szolista: 
        valasz = input('Ez nem jo, 5 hosszu ertelmes magyar szonak kell lennie! Adj ujat: ')
    return valasz



def visszajelzes(tippelt_szo, kitalalando_szo):
    for i in range(5):
        if tippelt_szo[i] == kitalalando_szo[i]:
            print(zold + tippelt_szo[i], end=normal)
        elif tippelt_szo[i] in kitalalando_szo:
            print(sarga + tippelt_szo[i], end=normal)
        else:
            print(tippelt_szo[i], end='')
    print()

nyelv = input('Milyen nyelven jatszanal? en/hu ')
while nyelv.lower not in ['hu', 'en']:
    nyelv = input('Nem supportalt nyelv! en/hu ')

with open(f'wordlist_{nyelv.lower()}.json', encoding='utf8') as szo_fajl:
    szolista = json.load(szo_fajl) 

titkos = random.choice(szolista)
print("Megfejtendo: ", titkos)

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