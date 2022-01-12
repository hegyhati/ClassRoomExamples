nyelv = input("EN/HU?")


def greeting(language="HU"):
    if language == "HU":
        return "Szia!"
    elif language == "EN":
        return "Hi!"


def ask_for_name(language="HU"):
    if language == "HU":
        return "Hogy hivnak?"
    elif language == "EN":
        return "What is your name?"


def greeting_with_name(nev, language="HU"):
    if language == "HU":
        return "Szia "+nev+"!"
    elif language == "EN":
        return "Hey "+nev+"!"


def film_selection(language="HU"):
    if language == "HU":
        return "LotR vagy Twillight?"
    elif language == "EN":
        return "LotR or Twillight?"


def ask_for_age(language="HU"):
    if language == "HU":
        return "Hany eves vagy?"
    elif language == "EN":
        return "How old are you?"


def drink_beer(language="HU"):
    if language == "HU":
        return "Igyunk meg egy korso sort!"
    elif language == "EN":
        return "Let's drink a beer!"


def drink_soft_drink(language="HU"):
    if language == "HU":
        return "Igyunk egy bambit!"
    elif language == "EN":
        return "Come, drink some soda?"


def idiot(language="HU"):
    if language == "HU":
        return "Letagadom, hogy ismerlek."
    elif language == "EN":
        return "I don't know you, never had."


print(greeting())
nev = input(ask_for_name() + " ")
print(greeting_with_name(nev))
film = input(film_selection() + " ")
if film == "LotR":
    kor = int(input(ask_for_age() + " s"))
    if kor >= 18:
        print(drink_beer())
    else:
        print(drink_soft_drink())
else:
    print(idiot())
