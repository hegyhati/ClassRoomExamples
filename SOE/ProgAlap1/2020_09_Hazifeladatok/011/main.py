"""
Ez a program nem fog mast csinalni, mint inicializal nekunk egy "terkepet", ami nem lesz mas, mint egy listakbol allo lista. 

A kovetkezo terkep:

██████████████
█░░░░░░███████
█░░░░░░███░░░█
█░░███████░█░█
█░░█░░░░░█░█░█
█░░░░░░█░█░█░█
█████░░█░█░█░█
█░░░░░░█░░░█░░
██████████████


peldaul igy lenne eltarolva egy listakbol allo listaban:

terkep = [
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","░","░","░","█"],
    ["█","░","░","█","█","█","█","█","█","█","░","█","░","█"],
    ["█","░","░","█","░","░","░","░","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","█","░","█","░","█"],
    ["█","█","█","█","█","░","░","█","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","░","░","█","░","░"],
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"]
]

Tehat a terkep[0][0] a terkep bal felso sarkat tartalmazza, a terkep[0][1] a tole jobbra levo mezot, stb. A lista jobb felso sarka most a terkep[0][13], a jobb also pedig a terkep[8][13].

Ez egy "felulnezet" egy epuletre, ahol █ reprezentalj a falakat, es ░ a szabadon bejarhato teruletet.

Elso alkalommal most az a feladat, hogy irjatok egy olyan fuggvenyt, ami visszaad egy ilyen terkepet.
"""


def initialize_map (width, height):
    # Ide irjatok meg a kodotokat. Mindket argumentum egy int, es a sorok/oszlopok szamat fogja megadni.
    # A fuggveny ugy mukodjon, egy egy teglalap alaku terkepet adjon vissza a megfelelo sor es oszlopszammal, de ugy, hogy a szelso mezok falak (es csak azok)
    # Feltetelezheto, hogy mindket ertek legalabb 2


"""
peldaul az initialize_map(3,4) a kovetkezo listat adja vissza:
[["█","█","█"],["█","░","█"],["█","░","█"],["█","█","█"]]

Ami nem mas, mint:
[
    ["█","█","█"],
    ["█","░","█"],
    ["█","░","█"],
    ["█","█","█"]
]

Egy kicsit nagyobb pelda: initialize_map(10,6) eredmenye:
[
    ["█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","░","░","░","░","░","░","░","░","█"],
    ["█","█","█","█","█","█","█","█","█","█"]
]
"""


###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


width=int(input())
height=int(input())
print(initialize_map(width,height))
