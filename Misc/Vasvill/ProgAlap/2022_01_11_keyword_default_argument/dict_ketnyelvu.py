nyelv = input("EN/HU?")

szovegek = {
    "greeting": {
        "HU": "Szia!",
        "EN": "Hi!"
    },
    "ask_for_name": {
        "HU": "Hogy hivnak?",
        "EN": "What is your name?"
    },
    "film_selection": {
        "HU": "LotR vagy Twillight?",
        "EN": "LotR or Twillight?"
    },
    "ask_for_age": {
        "HU": "Hany eves vagy?",
        "EN": "How old are you?"
    },
    "drink_beer": {
        "HU": "Igyunk meg egy korso sort!",
        "EN": "Let's drink a beer!"
    },
    "drink_soft_drink": {
        "HU": "Igyunk egy bambit!",
        "EN": "Come, drink some soda?"
    },
    "idiot": {
        "HU": "Letagadom, hogy ismerlek.",
        "EN": "I don't know you, never had."
    }
}


language = input("EN/HU")
print(szovegek["greeting"])
nev = input(szovegek["ask_for_name"] + " ")
film = input(szovegek["film_selection"] + " ")
if film == "LotR":
    kor = int(input(szovegek["ask_for_age"] + " s"))
    if kor >= 18:
        print(szovegek["drink_beer"])
    else:
        print(szovegek["drink_soft_drink"])
else:
    print(szovegek["idiot"])
