from time import time

from matplotlib import pyplot as plt
import factorial
from sys import argv


def binom_loop(n,k):
    return factorial.factorial_loop(n) // factorial.factorial_loop(n-k) // factorial.factorial_loop(k)

def binom_recursive(n,k):
    return factorial.factorial_recursive(n) // factorial.factorial_recursive(n-k) // factorial.factorial_recursive(k)

def print_pascal(type, depth):
    if "dynamic" in type:
        row = [1]
        if "silent" not in type: print(row)
        for r in range(1,depth):
            newrow = [1]
            for idx in range(len(row)-1):
                newrow.append(row[idx] + row[idx+1])
            newrow.append(1)
            if "silent" not in type:  print(newrow)
            row = newrow

    else:
        for row in range(depth):
            for column in range(row+1):
                if type == "rec":
                    print(binom_recursive(row,column), end=" ")
                elif type == "loop":
                    print(binom_loop(row,column), end=" ")
                elif type == "silentrec":
                    binom_recursive(row, column)
                elif type == "silentloop":
                    binom_loop(row,column)
            if "silent" not in type: print()


#         argv[0]   argv[1]  argv[2]
# python3 pascal.py rec      15
# print_pascal(argv[1], int(argv[2]))


if __name__ == "__main__":
    types = ["silentdynamic", "silentloop", "silentrec"]
    depths = [ i*100 for i in range(10)]
    results = { type: [] for type in types } 
    for depth in depths:
        for type in types:
            print(f"Running {type} for depth {depth}...", end="")
            start = time()
            print_pascal(type, depth)
            end = time()
            results[type].append(end-start)  
            print(f" [DONE] - {end-start}")
    fig,ax = plt.subplots()
    for type in types:
        ax.plot(depths,results[type],label = type)
    fig.legend()
    fig.savefig("pascal.png")     
