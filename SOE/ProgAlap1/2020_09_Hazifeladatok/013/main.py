"""
Tovabbfejlesztjuk az elozo dolgot. 

Most atirjuk a kiirato fuggvenyt ugy, hogy kap egy dictionary-t is, amiben benne van a jatekos karakterunk a kovetkezo modon:

character = {
    "name" : "Dark Wanderer",
    "position" : {
        "x" : 4 ,
        "y" : 2 
    }
}


Az eredmenye a kiiratasnak a korabbi peldaterkepen igy nezne ki:

████████████████████████████
██░░░░░░░░░░░░██████████████
██░░░░░░🧙‍░░░░██████░░░░░░██
██░░░░██████████████░░██░░██
██░░░░██░░░░░░░░░░██░░██░░██
██░░░░░░░░░░░░██░░██░░██░░██
██████████░░░░██░░██░░██░░██
██░░░░░░░░░░░░██░░░░░░██░░░░
████████████████████████████

Ket dolog valtozott meg:
 - Az eddigi █ es ░ karaktereket mindig duplan rajzoljuk ki, hogy korulbelul negyzet alaku legyen egy mezo.
 - A karakterunk helyere 🧙‍-t irunk ki.



"""

def initialize_map (width, height):
    # ide masold be a helyes megoldasodat a multkorirol

def pretty_map_print(map, character):
    # Ide masold be a multkorit, a fenti modositasokkal. 
    # Ha a karakter pozicioja a palyan kivul lenne, egyszeruen ne jelenjen meg


###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


def initialize_character():
    x=int(input())
    y=int(input())
    return {"name": "Placeholder name", "position" : {"x":x,"y":y} }

width=int(input())
height=int(input())
map=initialize_map(width,height)

character=initialize_character()

pretty_map_print(map,character)
