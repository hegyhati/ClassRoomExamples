import matplotlib.pyplot as plt

beer_consumptions = {
    "medard": [2,0,0,1,2,0,2],
    "gergo" : [7,0,7,0,7,0,7],
    "kitti" : [0,1,2,3,4,5,6],
    "iza"   : [6,5,4,3,6,5,4]
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

fig,ax = plt.subplots()
bottom = [0] * len(days)
for student, beers in beer_consumptions.items():
    ax.barh(days,beers,label=student, left=bottom)
    bottom = [bottom[i] + beers[i] for i in range(len(days))]
ax.legend()
fig.savefig("beers.png")


