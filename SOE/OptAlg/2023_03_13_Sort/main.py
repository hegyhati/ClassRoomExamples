import json
import time
from sys import argv
import sorting

if len(argv) != 4:
    print("algorithm size [increasing|decreasing|random]")
    exit()

with open(f"testcases/{argv[2]}_{argv[3]}.json") as f:
    data = json.load(f)

start = time.time()
sorting.__dict__[f"{argv[1]}_sort"](data)
end = time.time()
print(end-start)

#print(data)