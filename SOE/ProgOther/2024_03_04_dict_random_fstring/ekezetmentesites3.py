tabla = {
    "ö": "o",
    "ő": "o",
    "ó": "o",
    "ú": "u",
    "ü": "u",
    "ű": "u",
    "á": "a",
    "é": "e",
    "í": "i"
}
tabla["ä"] = "a"
tabla["ß"] = "ss"

nev = input()
nev = nev.lower()

for mit, mire in tabla.items():
    nev = nev.replace(mit, mire)

nev = nev.title()

print(nev)