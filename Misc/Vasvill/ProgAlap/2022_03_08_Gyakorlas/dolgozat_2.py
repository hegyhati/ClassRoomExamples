import json


def van_ismetlodo_karakter_1(szo):
    for bal_idx in range(len(szo)):
        for jobb_idx in range(bal_idx+1, len(szo)):
            if szo[bal_idx] == szo[jobb_idx]:
                return True
    return False

def van_ismetlodo_karakter_2(szo):
    volt_mar = []
    for betu in szo:
        if betu not in volt_mar:
            volt_mar.append(szo)
        else:
            return True
    return False

def van_ismetlodo_karakter_3(szo):
    for betu in szo:
        if szo.count(betu) > 1:
            return True
    return False

def van_ismetlodo_karakter_4(szo):
    return len(set(szo)) < len(szo)


with open('szavak.json') as f:
    szavak = json.load(f)

for szo in szavak:
    if not van_ismetlodo_karakter_4(szo):
        print(szo)

