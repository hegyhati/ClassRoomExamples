ekezetes =     ["á", "é", "í", "ö", "ü", "ó", "ő", "ú", "ű", "ä"]
ekezetmentes = ["a", "e", "i", "o", "u", "o", "o", "u", "u", "a"]

nev = input()
nev = nev.lower()

for idx in range(len(ekezetes)):
    nev = nev.replace(ekezetes[idx], ekezetmentes[idx])

nev = nev.title()

print(nev)