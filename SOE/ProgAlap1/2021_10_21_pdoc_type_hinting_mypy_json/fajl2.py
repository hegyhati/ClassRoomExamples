with open("szamok.txt") as fajl:
    szamok = fajl.readline()[:-1]

print(szamok)

szamlista = szamok.split(",")

print(szamlista)

szamlista2 = [int(szam) for szam in szamlista]

print(szamlista2)
