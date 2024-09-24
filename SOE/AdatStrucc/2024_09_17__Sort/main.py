import random
from sys import argv
from timeit import timeit
from sorts import *
import matplotlib.pyplot as plt

max_range = int(argv[1])

testcases = [ i*10**n for n in range(max_range) for i in range(1,10)]

sort_algorithms = {
    # "Insertion (inplace)" : insertion_sort,
    # "Insertion (copy)":     wasteful_insertion_sort,
    # "Bubble":               bubble_sort,
    # "Bubble (tricky)":      bubble_sort_tricky,
    # "Selection":            selection_sort,
    "Merge":                merge_sort,
    "Quick (copy)":         wasteful_quick_sort,
    "Quick (Lomuto)":       quick_sort_lomuto,
    "Quick (Hoare)":        quick_sort_hoare,
    "Heap":                 heap_sort,
    "Counting":             counting_sort
    
}
times = {
    sort_name : []
    for sort_name in sort_algorithms
}


for testcase in testcases:
    print(testcase, end=" ")
    test = list(range(testcase))
    random.shuffle(test)
    
    for name,sort_function in sort_algorithms.items():
        print(name, end=" ")
        testcopy = test.copy()
        time = timeit(lambda: sort_function(testcopy), number=1)
        times[name].append(time)
    print()

for name in sort_algorithms:
    plt.plot(testcases, times[name],label=name)
plt.legend()
plt.savefig(f"{10**max_range}.png")

