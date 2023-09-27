from random import randint
from typing import Dict, List
from sys import argv
import matplotlib.pyplot as plt

def roll() -> int:
    return randint(1,6)

def experiment(count:int) -> List[int]:
    return sum([roll() for _ in range(count)])

def get_histogram(experimentcount:int, sumcount:int) -> Dict[int, int]:
    data = [experiment(sumcount) for _ in range(experimentcount)]
    return {
        x : data.count(x)
        for x in range(sumcount,6*sumcount+1)
    }



experimentcount = int(argv[1])
sumcount = [ int(x) for x in argv[2:] ]

fig,axs = plt.subplots(2,2, figsize=(10,10), dpi=200)
fig.suptitle("Distribution of sum of dicerolls")
for i in range(4):
    hist_data = get_histogram(experimentcount, sumcount[i])
    axs[i%2][i//2].bar(hist_data.keys(), hist_data.values())
    axs[i%2][i//2].set_title(f"Sum of {sumcount[i]} dice rolls")
fig.savefig("diceroll.png")



