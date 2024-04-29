people = [
    {
        "name" : "Akos",
        "height" : 181,
        "weight": 106
    },
    {
        "name" : "Adrian",
        "height" : 155,
        "weight": 196
    },
    {
        "name" : "Lori",
        "height" : 186,
        "weight": 94
    },
    {
        "name" : "Dani",
        "height" : 178,
        "weight": 65
    }
]

def bmi(person):
    return person["weight"]  / (person["height"] / 100) ** 2 


import matplotlib.pyplot as plt

fig,axs = plt.subplots(2)

axs[0].bar(x = [ p["name"] for p in people], height=[ p["height"] for p in people ] )
# set title to height
axs[0].set_title("Height")


axs[1].barh(y = [ p["name"] for p in people], width=[ bmi(p) for p in people ] )
axs[1].set_title("BMI")

plt.tight_layout()



fig.savefig("boys.png")
