import json
from operator import index
import random

normal = '\033[0;37;40m'
szurke = '\033[1;30;47m'
zold   = '\033[1;30;42m'
sarga  = '\033[1;30;43m'

def eredmeny_kiiras(sikeresseg, lepesszam):
    if sikeresseg:
        print(f'Gratulalok, nyertel {lepesszam} lepesbol')
    else:
        print('Vesztettel, legkozelebb.')

def helyes_tipp_beker():
    valasz = input(f'Kerem a kovetkezo tippet: ')
    while valasz not in szolista: 
        valasz = input('Ez nem jo, helyes 5 hosszu szonak kell lennie! Adj ujat: ')
    return valasz

def kozos_karakterek(egyik, masik):
    mindkettoben = []
    for betu in egyik:
        if betu in masik:
            mindkettoben.append(betu)
    return mindkettoben

def azonos_karakter_indexek(egyik, masik):
    indexek = []
    for idx in range(min(len(egyik),len(egyik))):
        if egyik[idx]==masik[idx]:
            indexek.append(idx)
    return indexek

def fancy_kiir(szo,sargak,zold_indexek):
    for idx in range(len(szo)):
        if idx in zold_indexek:
            print(zold+szo[idx], end='')
        elif szo[idx] in sargak:
            print(sarga+szo[idx],end='')
        else:
            print(f"{szurke}{szo[idx]}",end='')
    print(normal)

with open('wordlist_hu.json') as file:
    szolista = json.load(file)

titkos = random.choice(szolista)
print("Titkos szó: ", titkos)
sikerult = False
hanyadikra = 0

while hanyadikra < 6:
    tipp = helyes_tipp_beker()
    kozos = kozos_karakterek(tipp,titkos)
    johelyen = azonos_karakter_indexek(tipp, titkos)
    fancy_kiir(tipp,kozos,johelyen)
    hanyadikra += 1
    if tipp==titkos:
        sikerult = True
        break

eredmeny_kiiras(sikerult,hanyadikra)

