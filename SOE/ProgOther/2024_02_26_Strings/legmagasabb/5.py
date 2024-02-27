nem_valaszok = ["nem", "nincs", "nope", "nah"]
igen_valaszok = ["igen", "ja", "van van", "aha"]

hallgatok = []

while True:
    valasz = input("Van-e meg hallgato?").strip().lower()
    if valasz in nem_valaszok:
        break
    elif valasz in igen_valaszok:
        hallgato = input("Hogy hivjak a hallgatot? ")
        hallgatok.append(hallgato)
    else:
        print("Csak igen-t es nem-et fogadok el.")

print(", ".join(hallgatok))