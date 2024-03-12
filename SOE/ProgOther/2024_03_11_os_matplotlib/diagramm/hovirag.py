from matplotlib import pyplot as plt


hoviragok = [
    {
        "x" : 5,
        "y" : 4,
        "db" : 15
    },
    {
        "x" : 9,
        "y" : 26,
        "db" : 45
    },{
        "x" : 3,
        "y" : 12,
        "db" : 1
    },{
        "x" : 5,
        "y" : -4,
        "db" : 5
    },{
        "x" : 25,
        "y" : 14,
        "db" : 115
    }
]

x = [meres["x"] for meres in hoviragok]
y = [meres["y"] for meres in hoviragok]
db = [meres["db"] for meres in hoviragok]

plt.scatter(x,y,db)

plt.show()