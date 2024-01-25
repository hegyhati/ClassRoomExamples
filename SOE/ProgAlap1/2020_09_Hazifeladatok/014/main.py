"""
Ideje mozgatni a hosunket :-)

A bemenetek lekezeleset elintezi a foprogram, Nektek csak egy move fuggvenyt kell megirni, ami megprobalja a megadott iranyba mozgatni a hosunket. 

Ez az irany lehet "up", "down", "left", "right".

Hogy ne egy unalmas ures palyan mozogjunk, a foprogram most fixen az alabbi helyzetbol indit: 

████████████████████████████
██🧙░░░░░░░░░░██████████████
██░░░░░░░░‍░░░░██████░░░░░░██
██░░░░██████████████░░██░░██
██░░░░██░░░░░░░░░░██░░██░░██
██░░░░░░░░░░░░██░░██░░██░░██
██████████░░░░██░░██░░██░░██
██░░░░░░░░░░░░██░░░░░░██░░██
████████████████████████████

A szabaly a mozgasra nyilvan a kovetkezo: ha val van, nem tudunk oda menni. A palyarol feltetelezhetjuk, hogy zart, azaz nem lehet rola lemenni, ezt kulon nem kell vizsgalni.

"""

def pretty_map_print(map, character):
    # Ide masold be a multkorit, modositas nem szukseges

def move(map,character,direction):
    # fentiek alapjan, direction lehet "up", "down", "left", "right"



###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


character={"name":"The wizard", "position":{"x":1,"y":1}}
map = [
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","░","░","░","█"],
    ["█","░","░","█","█","█","█","█","█","█","░","█","░","█"],
    ["█","░","░","█","░","░","░","░","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","█","░","█","░","█"],
    ["█","█","█","█","█","░","░","█","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","░","░","█","░","█"],
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"]
]

while True:
    pretty_map_print(map,character)
    command = input()
    if command=="end": break
    print ("Moving "+command+" is "+ 
        ("successful" if move(map,character,command) else "impossibru")
    )
