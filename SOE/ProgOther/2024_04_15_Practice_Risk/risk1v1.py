import random

attackers = 20
defenders = 20

while attackers > 0 and defenders > 0:
    attacker_roll = random.randint(1,6)
    defender_roll = random.randint(1,6)

    print( f"Attacker({attackers}): {attacker_roll}, Defender({defenders}): {defender_roll}")
    if defender_roll >= attacker_roll: attackers -= 1
    else: defenders -= 1

if attackers > 0:
    print(f"Attackers({attackers}) win the battle.")
else:
    print(f"Defenders({defenders}) win the battle.")
    