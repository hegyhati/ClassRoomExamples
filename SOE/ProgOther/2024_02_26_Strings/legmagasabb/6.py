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
        magassag = input("Milyen magas? ")
        magassagok.append(magassag)
    else:
        print("Csak igen-t es nem-et fogadok el.")

print(", ".join(hallgatok))
print(", ".join(magassagok))
