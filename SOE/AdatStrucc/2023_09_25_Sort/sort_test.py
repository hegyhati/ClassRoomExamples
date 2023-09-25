from timeit import timeit
from random import shuffle

size = 10**4

from sys import setrecursionlimit
setrecursionlimit(10**5)

sorts = [
    "max_selection_sort", 
    "bubble_sort", "not_so_clever_bubble_sort", "not_so_genius_bubble_sort",
    "lazy_quick_sort", "quick_sort"
]
t = list(range(size))
shuffle(t) 
testcases = {
        "increasing": list(range(size)), 
        "random": t ,
        "decreasing": list(range(size))[::-1]
}

for s in sorts:
    for n,t in testcases.items():
        print(
            f"{s} on {size} elements with {n} order: ",
            timeit(
                f"{s}(t)",
                setup = f"from sorts import {s}; t = {str(t)}",
                number = 1
            )
        )
for n,t in testcases.items():
    print(
        f"built in list sort on {size} elements with {n} order: ",
        timeit(
            f"t.sort()",
            setup = f"from sorts import {s}; t = {str(t)}",
            number = 1
        )
    )