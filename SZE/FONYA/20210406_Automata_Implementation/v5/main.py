import json

f = open("bab.json","rt")
dfa = json.load(f)

word = input()

state = dfa["s"]
for c in word:
    if c in dfa["delta"][state].keys():
        state=dfa["delta"][state][c]
    else:
        state=dfa["delta"][state]["_"]

print("Elfogadva" if state in dfa["F"] else "Nem elfogadva")


