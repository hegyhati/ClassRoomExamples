nem_valaszok = ["nem", "nincs", "nope", "nah"]
igen_valaszok = ["igen", "ja", "van van", "aha"]

hallgatok = []
magassagok = []

while True:
    valasz = input("Van-e meg hallgato? ").strip().lower()
    if valasz in nem_valaszok:
        break
    elif valasz in igen_valaszok:
        hallgato = input("Hogy hivjak a hallgatot? ")
        hallgatok.append(hallgato)
        while True:
            magassag = input("Milyen magas? ")
            if magassag.isnumeric():
                magassag = float(magassag)
                if magassag > 0: # todo: isnumeric negativat eleve nem fogad el.
                    magassagok.append(float(magassag))
                    break
                else:
                    print("Negativ szamot nem fogadok el.")
            else:
                print("Csak szamot fogadok el.")
    else:
        print("Csak igen-t es nem-et fogadok el.")

print(", ".join(hallgatok))
max_magassag = max(magassagok)
idx = magassagok.index(max_magassag)
print("A legmagasabb " + hallgatok[idx] + " (" + str(magassagok[idx]) +" cm)")
