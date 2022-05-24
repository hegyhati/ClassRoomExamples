import random

def k6():
    return random.randint(1,6)

def kezdodobas():
    return [ k6() for _ in range(5) ]

def ujradobas(dobasok):
    for ujdobas in input("Melyikekkel szeretnel ujradobni? ").split(','):
        dobasok[int(ujdobas)-1] = k6()

def van_par(dobasok):
    return dobasok[0] == dobasok[1] or dobasok[0] == dobasok[2] or dobasok[0] == dobasok[3] or dobasok[0] == dobasok[4] or dobasok[1] == dobasok[2] or dobasok[1] == dobasok[3] or dobasok[1] == dobasok[4] or dobasok[2] == dobasok[3] or dobasok[2] == dobasok[4] or dobasok[3] == dobasok[4]

def van_par_2(dobasok):
    for i in range(5):
        for j in range(i+1,5):
            if dobasok[i] == dobasok[j]:
                return True
    return False

def van_par_3(dobasok):
    for dobas in dobasok:
        if dobasok.count(dobas) >= 2:
            return True
    return False

def van_par_4(dobasok):
    return len(set(dobasok)) < 5

def van_drill_2(dobasok):
    for i in range(5):
        for j in range(i,5):
            for k in range(j,5):
                if dobasok[i] == dobasok[j] and dobasok[j]== dobasok[k]:
                    return True
    return False

def van_drill_3(dobasok):
    for dobas in dobasok:
        if dobasok.count(dobas) >= 3:
            return True
    return False

def van_poker(dobasok):
    return dobasok[0] == dobasok[1] and dobasok[0] == dobasok[2] and dobasok[0] == dobasok[3] and dobasok[0] == dobasok[4] 

def van_poker_2(dobasok):
    for idx in range(1,5):
        if dobasok[0] != dobasok[idx]:
            return False
    return True

def van_poker_3(dobasok):
    return dobasok.count(dobasok[0]) == 5

def van_poker_4(dobasok):
    return len(set(dobasok)) == 1

def van_poker_5(deobasok):
    return min(dobasok) == max(dobasok)
    
dobasok = kezdodobas()
print(dobasok)
for _ in range(2):
    ujradobas(dobasok)
    print(dobasok)



if van_par(dobasok): print("Elfogadtathatod parnak.")

