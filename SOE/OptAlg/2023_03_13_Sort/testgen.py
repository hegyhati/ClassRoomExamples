import json
import random


for size in [20000,30000,40000,50000]:
    l = list(range(size))
    with open(f"testcases/{size}_increasing.json", "w") as f:
        json.dump(l,f)
    l = l[::-1]
    with open(f"testcases/{size}_decreasing.json", "w") as f:
        json.dump(l,f)
    random.shuffle(l)
    with open(f"testcases/{size}_random.json", "w") as f:
        json.dump(l,f)
    
    