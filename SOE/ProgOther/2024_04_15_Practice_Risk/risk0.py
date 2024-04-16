import random

attacker = random.randint(1,6)
defender = random.randint(1,6)

print( f"Attacker: {attacker}, Defender: {defender}")
if defender >= attacker:
    print("defender wins")
else:
    print("attacker wins")