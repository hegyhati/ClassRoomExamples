
from timeit import timeit

print(
timeit("s.pop()", setup = "from LLStack2 import Stack; s=Stack(10**6);", number = 10 ** 6)
)