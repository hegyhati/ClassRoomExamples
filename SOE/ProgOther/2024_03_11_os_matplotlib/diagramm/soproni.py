from matplotlib import pyplot as plt


arak = {
    1990 : 50,
    1995 : 60,
    2000 : 80,
    2005 : 100,
    2010 : 180,
    2015 : 230,
    2020 : 280,
    2025 : 450    
}

plt.plot(arak.keys(), arak.values())
plt.show()