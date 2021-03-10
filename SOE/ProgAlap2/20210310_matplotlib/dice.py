import random as rand
import matplotlib.pyplot as plt

def diceroll():
    return rand.randint(1,6)

rollcount = int(input("Hany dobas osszeget nezzuk?"))
testcount = int(input("Hany dobassorozatot csinaljunk?"))

values = list(range(rollcount*6))
count = [0] * 6 * rollcount

for i in range(testcount):
    rollsum = 0
    for roll in range(rollcount):
        rollsum += diceroll()
    count[rollsum-1] += 1

f,a = plt.subplots()
a.plot(values,count)
f.savefig('dicerolls.png')
