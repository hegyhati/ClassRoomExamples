import random

def feladat1():
    a = random.randint(1,1000)
    b = random.randint(1,1000)

    if a > b:
        if a % b == 0:
            print(f"{b} osztoja {a}-nak.")
        else:
            print("Nem osztoja.")
    else:
        if b % a == 0:
            print(f"{a} osztoja {b}-nak.")
        else:
            print("Nem osztoja.")


def feladat1_2():
    a = random.randint(1,1000)
    b = random.randint(1,1000)
    smaller = min(a,b)
    larger = max(a,b)
    if larger % smaller == 0:
        print(f"{smaller} osztoja {larger}-nak.")
    else:
        print("Nem osztoja.")

def feladat2():
    maganhangzok = ['a','á','e','é','i','í','o','ó','ö','ő','ü','ű','u','ú']
    maganhangzok = 'aáeéiíoóuúöőüű'
    szavak = input().split(',')
    for szo in szavak:
        if szo.strip()[-1] in maganhangzok:
            print(szo.strip())

import json
def more_diligent(futo1, futo2):
    with open('futok.json') as f:
        futasok = json.load(f)
    hanyszor1 = 0
    for futas in futasok:
        if futo1 in futas['runners']:
            hanyszor1 += 1
    hanyszor2 = 0
    for futas in futasok:
        if futo2 in futas['runners']:
            hanyszor2 += 1
    if hanyszor1 == 0 or hanyszor2 == 0:
        raise ValueError
    if hanyszor1 >= hanyszor2:
        return futo1
    else:
        return futo2

def count_runs(futo):
    with open('futok.json') as f:
        futasok = json.load(f)
    hanyszor = 0
    for futas in futasok:
        if futo in futas['runners']:
            hanyszor += 1
    return hanyszor


def more_diligent_2(futo1, futo2):
    hanyszor1 = count_runs(futo1)
    hanyszor2 = count_runs(futo2)
    if hanyszor1 == 0 or hanyszor2 == 0:
        raise ValueError
    return futo1 if hanyszor1 >= hanyszor2 else futo2
    

for r1 in ['D', 'O', 'G']:
    for r2 in ['C','A','M','X']:
      try:
        print(f"{r1} és {r2} közül { more_diligent(r1,r2) } futott többször.")
      except ValueError:
        print(f"{r1} és {r2} közül valaki egyszer sem futott.")
