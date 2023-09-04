from timeit import timeit
import matplotlib.pyplot as plt

sizes = [a * 10 ** b for b in range(5) for a in range(1,10)]
running_times_initialize = [timeit(f"l = [1] * {size}", number=1) for size in sizes]
running_times_append = [timeit("l.append(1)", setup="l=[]", number=size) for size in sizes]
running_times_insert = [timeit("l.insert(0,1)", setup="l=[]", number=size) for size in sizes]

plt.scatter(sizes, running_times_initialize)
plt.scatter(sizes, running_times_append)
plt.scatter(sizes, running_times_insert)
plt.show()

