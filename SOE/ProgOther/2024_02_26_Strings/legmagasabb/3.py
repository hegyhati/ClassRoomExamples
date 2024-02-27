nem_valaszok = ["nem", "nincs", "nope", "nah"]


while True:
    valasz = input("Van-e meg hallgato?").strip().lower()
    if valasz in nem_valaszok:
        break