from CFG import CFG

G_json = CFG("json.json")

with open("json.txt") as f:
    s = f.read()
print(G_json.accept_BFS(s))