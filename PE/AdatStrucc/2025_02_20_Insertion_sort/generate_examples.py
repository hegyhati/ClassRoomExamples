from random import shuffle

RANGE = 7

def export(data:list[int], suffix:str):
    with open(f"examples/{len(data):010}_{suffix}.txt","w") as f:
        f.write(f"{len(data)}\n")
        f.write(" ".join(str(num) for num in data))
        f.write("\n")

sizes = [k*10**n for n in range(RANGE) for k in range(1,10)]

for size in sizes:
    data = list(range(size))
    export(data,"increasing")
    data.reverse()
    export(data, "decreasing")
    shuffle(data)
    export(data, "random_1")
    shuffle(data)
    export(data, "random_2")
    shuffle(data)
    export(data, "random_3")
    shuffle(data)
    export(data, "random_4")
    shuffle(data)
    export(data, "random_5")