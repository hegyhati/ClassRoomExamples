import json

with open("szamok2.json") as file:
    szamlista = json.load(file)

szamlista.append(333)
print (szamlista)

with open("szamok.json","wt") as file:
    file.write(json.dumps(szamlista)+"\n")
