import json
import time
import sorting
import matplotlib.pyplot as plt


configurations = {
    'bubble' : [100,1000,10000,20000,30000],
    'bubble2' : [100,1000,10000,20000,30000],
    'insertion' : [100,1000,10000,20000,30000],
    'insertion_inplace' : [100,1000,10000,20000,30000],
    'merge' : [100,1000,10000,20000,30000,100000],
    'quick' : [100,1000,10000,20000,30000,100000,1000000]
}

fig,ax = plt.subplots()

ax.set_yscale('log')
ax.set_xscale('log')

for a in configurations:
    times = []
    for s in configurations[a]:
        with open(f"testcases/{s}_random.json") as f:
            data = json.load(f)
        start = time.time()
        sorting.__dict__[f"{a}_sort"](data)
        end = time.time()
        times.append(float(end-start))
    ax.plot(configurations[a],times,label=a)

fig.legend()
fig.savefig("Results.png")

