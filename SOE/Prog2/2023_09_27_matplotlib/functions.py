import matplotlib.pyplot as plt

fig,ax = plt.subplots()

x = list(x / 10 for x in range(-10,11))
ax.plot(x, [i for i in x])
ax.plot(x, [i**2 for i in x])
ax.plot(x, [i**3 for i in x])

fig.savefig("functions.png")
