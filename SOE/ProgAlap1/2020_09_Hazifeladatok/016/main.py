"""
A terkepre most mar kikerulnek taposoaknak is. Ha a hosunk ralep egyre, akkor befejezodott a jatek. Ezt a logikat lekezeli a foprogram megfelelo resze. 

Nektek most egy olyan fuggvenyt kell megirni, ami egy karaktert es egy aknalistat kap (lasd a foprogramot peldanak) es visszater igaz/hamis ertekkel attol fuggoen, hogy valamelyikre ralepett-e a hosunk, vagy sem.

Ezen kivul meg a pretty print fuggvenyen kell annyit modositani, hogy ne fixen a 🧙 karaktert rajzolja ki a hozunknek, hanem annak az icon adattagjat. (Lasd forprogram)

"""

def pretty_map_print(map, character):
    # A multkorit kell kicsit megpofozni

def move(map,character,direction):
    # ide csak masold be a multkorit, nem kell pofozni

def stepped_on_mine(character,mines):
    # ide kell megirni az uj fuggvenyt a fentiek szerint.

"""
Helyes megvalositas eseten peldaul egy jobbra, majd ketto lefele lepes eseten ez a helyes kimenet:


████████
██🧙░░██
██░░░░░░
██░░░░██
Moving right is successful
██████████
██░░🧙████
██░░░░░░░░
██░░░░██░░
Moving down is successful
██████████
██░░░░████
██░░🧙░░░░
██░░░░██░░
████████░░
Moving down is successful
The wizard stepped on a mine and died.
██░░░░████
██░░░░░░░░
██░░💀██░░
████████░░
██░░░░░░░░

"""

###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################

character={"name":"The wizard", "icon": "🧙", "position":{"x":1,"y":1},"vision":2}

landmines=[
    {"name": "mine 1", "position" : {"x":1,"y":2}},
    {"name": "mine 2", "position" : {"x":2,"y":3}},
    {"name": "mine 3", "position" : {"x":4,"y":3}},
]

map = [
    ["█","█","█","█","█","█"],
    ["█","░","░","█","█","█"],
    ["█","░","░","░","░","█"],
    ["█","░","░","█","░","█"],
    ["█","█","█","█","░","█"],
    ["█","░","░","░","░","█"],
    ["█","█","█","█","█","█"]
]


while True:
    if stepped_on_mine(character,landmines):
        character["icon"] = "💀"
        print(character["name"],"stepped on a mine and died.")
        pretty_map_print(map,character)
        break
    pretty_map_print(map,character)
    command = input()
    if command=="end": break
    print ("Moving "+command+" is "+ 
        ("successful" if move(map,character,command) else "impossibru")
    )
