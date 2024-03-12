import matplotlib.pyplot as plt

# plt.bar(["EMK", "FMK", "LKK", "BPK"],[330,80,100,0])

sorok = {
    "Soproni" : 380,
    "Soproni IPA" : 450,
    "Kobanyai" : 290,
    "Edelweiss" : 500,
    "Kozel dark" : 450,
    "Arany Aszok" : 310,
    "Dreher bak" : 420,
    "Sommersby" : 999
}

plt.bar(sorok.keys(), sorok.values())
plt.show()