nem_valaszok = ["nem", "nincs", "nope", "nah"]
igen_valaszok = ["igen", "ja", "van van", "aha"]

while True:
    valasz = input("Van-e meg hallgato?").strip().lower()
    if valasz in nem_valaszok:
        break
    elif valasz in igen_valaszok:
        pass
    else:
        print("Csak igen-t es nem-et fogadok el.")