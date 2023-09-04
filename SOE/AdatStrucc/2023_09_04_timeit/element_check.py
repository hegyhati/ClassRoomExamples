from timeit import timeit
import matplotlib.pyplot as plt

sizes = [a * 10 ** b for b in range(5) for a in range(1,10)]
running_times_list_in_front = [timeit(f"0 in l", setup = f"l=list(range({size}))", number=1) for size in sizes]
running_times_list_in_end = [timeit(f"0 in l", setup = f"l=list(range({size}))[::-1]", number=1) for size in sizes]
running_times_set_in = [timeit(f"0 in l", setup = f"l=set(range({size}))", number=1) for size in sizes]

plt.scatter(sizes, running_times_list_in_front, label="list in front")
# plt.scatter(sizes, running_times_list_in_end, label="list in end")
plt.scatter(sizes, running_times_set_in, label="set in")
plt.legend()
plt.show()

