import random
import matplotlib.pyplot as plt

attackers = 20
defenders = 20

attackers_size = [attackers]
defenders_size = [defenders]

while attackers > 0 and defenders > 0:
    attacker_roll = random.randint(1,6)
    defender_roll = random.randint(1,6)

    print( f"Attacker({attackers}): {attacker_roll}, Defender({defenders}): {defender_roll}")
    if defender_roll >= attacker_roll: attackers -= 1
    else: defenders -= 1
    
    attackers_size.append(attackers)
    defenders_size.append(defenders)
    

if attackers > 0:
    print(f"Attackers({attackers}) win the battle.")
else:
    print(f"Defenders({defenders}) win the battle.")

plt.plot(attackers_size, label="attackers")
plt.plot(defenders_size, label="defenders")
plt.legend()
plt.savefig("1v1_single_battle.png")