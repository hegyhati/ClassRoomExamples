import logic

def exit_program():
    print("Koszi, hogy velunk tanultal, gyere maskor is. bb")
    exit()

def add_new_word():
    hu = input("Kerlek add meg a magyar szot: ")
    en = input("Kerlek add meg az angol megfelelojet: ")
    if logic.has_word(hu):
        response = input(f"A {hu} szerepel a szotarban {logic.translate(hu)} jelentessel, le akarod cserelni? ")
        if response == "igen" : logic.update_with_word(hu, en)
    else: logic.update_with_word(hu, en)

def look_up_word():
    hu = input("Kerlek add meg a leforditando magyar szot: ")
    if logic.has_word(hu):
        print(f"A {hu} angol megfeleloje {logic.translate(hu)}.")
    else: 
        print("Nem ismerem ezt a szot.")
    
def not_implemented_message():
    print("Ez a funkcio meg nincs implementalva, gyere vissza holnap.")

def menu():
    while True:
        response = int(input (""" Mit szeretnel csinalni?
        1) Uj szo hozzaadasa a szotarhoz
        2) Egy szo kikeresese a szotarbol
        3) Egy szoveg leforditasa
        4) Kilepes
        """))

        if response == 4: exit_program()
        elif response == 1: add_new_word()        
        elif response == 2: look_up_word()
        elif response == 3: not_implemented_message()