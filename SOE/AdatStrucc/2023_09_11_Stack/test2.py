from timeit import timeit
from  collections import deque

size = 10 ** 7
print (
    timeit(f"data[{size}//2]", setup=f"from collections import deque; data = deque(range({size}))", number=100)
)
print (
    timeit(f"data[{size}//2]", setup=f"data = list(range({size}))", number=100)
)