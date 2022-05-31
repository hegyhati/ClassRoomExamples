import json
import random

def lazy_runners(date,runners):
    with open('futok.json') as f:
        runs = json.load(f)

    present_runners = None
    for run in runs:
        if run['date'] == date:
            present_runners = run['runners']
    if present_runners == None:
        raise ValueError

    #lazy = []
    #for runner in runners:
    #    if runner not in present_runners:
    #        lazy.append(runner)
    
    lazy = set(runners) - set(present_runners)    
    return list(lazy)

def feladat_3():
    runners = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ]

    for _ in range(5):
        test = random.sample(runners, k=5)
        for date in ['2018.11.27', '2018.11.28']:
            try:
                print(f"A {date}-i futáson a következő futók nem voltak ott: { lazy_runners(date,test) } .")
            except ValueError:
                print(f"{date}: nem volt aznap futás.")

def feladat_2():
    szo_lista = input().split(',')
    for idx in range(len(szo_lista)):
        szo_lista[idx] = szo_lista[idx].strip()
    for szo in szo_lista:
        if szo == szo[::-1]:
            print(szo)

def feladat_2_2():
    szo_lista = input().split(',')
    for szo in szo_lista:
        szo = szo.strip()
        if szo == szo[::-1]:
            print(szo)

def feladat_2_2():
    szo_lista = [ szo.strip() for szo in input().split(',') ]
    for szo in szo_lista:
        if szo == szo[::-1]:
            print(szo)

def feladat_2_2():
    print([ szo.strip() for szo in input().split(',') if szo.strip() == szo.strip()[::-1] ])