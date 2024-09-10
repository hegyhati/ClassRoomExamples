from collections import deque
from sys import argv
from timeit import timeit

from matplotlib import pyplot as plt


def push_back(container, count:int):
    for i in range(count):
        container.append(i)

def push_front(container, count:int):
    if isinstance(container,list):
        for i in range(count):
            container.insert(0,i) # n times O(n)
    elif isinstance(container,deque):
        for i in range(count):
            container.appendleft(i)

def pop_back(container, count:int):
    if isinstance(container, list):
        container = list(range(count))
    else:
        container = deque(range(count))
    for _ in range(count):
        container.pop()

def pop_front(container, count:int):
    if isinstance(container, list):
        container = list(range(count))
        for _ in range(count):
            container.pop(0)
    else:
        container = deque(range(count))
        for _ in range(count):
            container.popleft()

    

testfunction = pop_front

sizes = []
deck_plot = []
dynarray_plot = []


for magnitude in range(int(argv[1])):
    for i in range(1,10):
        size = i* 10**magnitude
        sizes.append(size)
        print(" ", size, end = " ")        
        deck = deque()
        deck_time = timeit(lambda: testfunction(deck, size), number=1)
        print(deck_time, end = " ")
        deck_plot.append(deck_time)
        dynarray = list()
        dynarray_time = timeit(lambda: testfunction(dynarray, size), number=1)
        print(dynarray_time)
        dynarray_plot.append(dynarray_time)


plt.plot(sizes, deck_plot, label="Deck")
plt.plot(sizes, dynarray_plot, label="Dynarray")
plt.legend()
plt.show()

