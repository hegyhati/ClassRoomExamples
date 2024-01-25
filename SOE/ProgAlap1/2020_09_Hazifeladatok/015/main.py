"""
A hosunk nem lat el a vegtelensegig. X-Ray vision megvan, mint Supermannek, amiatt nem kell aggodni, de van mostantol egy "vision" tulajdonsaga, ami megmondja, hogy mekkora "korben" (negyzet valojaban) lat. Ha mondjuk a vision 3, akkor egy 7x7-es negyzetet lat, mert 3-nyit lat el balra jobbra, fel le. Tehat mondjuk a korabbi peldanal maradva a kezdoallapot:

██████████
██🧙░░░░░░
██░░░░░░░░
██░░░░████
██░░░░██░░

Balra itt nem lat el 3-at, meg felfele, mert nincs annyi a palyabol ugye. Egy jobbra lepes utan:
████████████
██░░🧙░░░░░░
██░░░░░░░░░░
██░░░░██████
██░░░░██░░░░
majd lefele:
████████████
██░░░░░░░░░░
██░░🧙░░░░░░
██░░░░██████
██░░░░██░░░░
██░░░░░░░░░░
meg 3x le, aztan jobbra:
██░░░░░░░░░░░░
██░░░░████████
██░░░░██░░░░░░
██░░░░🧙░░░░░░
██████████░░░░
██░░░░░░░░░░░░
██████████████
Es akkor itt most mar "teljesen kihasznalja" a latasat. 


A bemenetek lekezeleset elintezi a foprogram, eloszor beker egy ilyen "vision" erteket, majd utana a mozgasokat ugy, ahogy mult heten.

Terkepnek a korabbit hasznalja, es ugyanugy a bal felso ficakbol indulunk.

"""

def pretty_map_print(map, character):
    # A multkorit kell kicsit megpofozni

def move(map,character,direction):
    # ide csak masold be a multkorit, nem kell pofozni



###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


vision=int(input())
character={"name":"The wizard", "position":{"x":1,"y":1},"vision":vision}
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
