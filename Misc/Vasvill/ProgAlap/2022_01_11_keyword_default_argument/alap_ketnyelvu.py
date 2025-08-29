nyelv = input("EN/HU?")

if nyelv == "HU":
    print("Szia!")
    nev = input("Hogy hivnak? ")
    print(f"Szia {nev}!")
    fantasy = input("Szereted a fantasy filmeket? ")
    film = input("LotR vagy Twillight? ")
    if film == "LotR":
        kor = int(input("Hany eves vagy? "))
        if kor >= 18:
            print("Igyunk meg egy sort!")
        else:
            print("Vendegem vagy egy bambira.")
    else:
        print("Letagadom, hogy ismerlek.")
elif nyelv == "EN":
    print("Hi!")
    nev = input("Hogy hivnak? ")
    print(f"Hello {nev}!")
    film = input("LotR or Twillight? ")
    if film == "LotR":
        kor = int(input("How old are you? "))
        if kor >= 18:
            print("Let's drink a beer!")
        else:
            print("Let me invide you for a soda.")
    else:
        print("I'm ashamed of knowing you.")
else:
    print(":/")
