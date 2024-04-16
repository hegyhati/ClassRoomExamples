import random

attackers = 20
defenders = 20

while attackers > 0 and defenders > 0:
    attacker_count = min(attackers, 3) # Tamado tamad amennyivel tud, de max 3
    defender_count = max(1, min(defenders, attacker_count-1)) # vedekezo vedekezik amennyivel tud, de max tamado-1, kiveve ha az 1-nel kevesebb, akkor 1.
    # Leegyszerusitve lehet 3-2, 3-1 (ha csak 1 vedekezo van), 2-1 (ha mar csak ket tamado van), 1-1 (ha mar csak 1 tamado van)
    
    attacker_rolls = []
    defender_rolls = []
    
    for i in range(attacker_count):
        attacker_rolls.append(random.randint(1,6))
    for i in range(defender_count):
        defender_rolls.append(random.randint(1,6))
    
    attacker_rolls.sort(reverse=True)
    defender_rolls.sort(reverse=True)
    
    for i in range(min(attacker_count,defender_count)):
        if attacker_rolls[i] > defender_rolls[i]:
            defenders -= 1
        else:
            attackers -= 1
    
if attackers > 0:
    print(f"Attackers({attackers}) win the battle.")
else:
    print(f"Defenders({defenders}) win the battle.")
    