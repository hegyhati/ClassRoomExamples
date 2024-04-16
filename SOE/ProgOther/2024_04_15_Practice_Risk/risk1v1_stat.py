import random
import matplotlib.pyplot as plt


attacker_wins = 0
defender_wins = 0


for _ in range(100):

    attackers = 20
    defenders = 20

    while attackers > 0 and defenders > 0:
        attacker_roll = random.randint(1,6)
        defender_roll = random.randint(1,6)
        if defender_roll >= attacker_roll: attackers -= 1
        else: defenders -= 1

    if attackers > 0: attacker_wins += 1
    else: defender_wins +=1 


plt.bar(height=[attacker_wins, defender_wins], x=["attacker win", "defender win"])
plt.savefig("1v1_stat.png")

    