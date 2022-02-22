import json

with open('wordlist.json', encoding='utf8') as f:
    szavak = json.load(f)

othosszuak = []
for szo in szavak:
    if len(szo) == 5:
        othosszuak.append(szo)

with open('wordlist5.json','w', encoding='utf8') as f:
    json.dump(othosszuak,f,ensure_ascii=False)