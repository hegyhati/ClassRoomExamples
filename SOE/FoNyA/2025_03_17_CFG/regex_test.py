from CFG import CFG

G_RE = CFG("regex.json")

while True:
    print(G_RE.accept_DFS(input()))