from collections import deque
from sys import argv
from timeit import timeit

from matplotlib import pyplot as plt

class List_XIFO:
    def __init__(self, size = 0) -> None:
        self.__data = [0] * size
    def push_back(self,item:int) -> None:
        self.__data.append(item)
    def push_front(self,item:int) -> None:
        self.__data.insert(0,item)
    def pop_back(self) -> int:
        return self.__data.pop()
    def pop_front(self) -> int:
        return self.__data.pop(0)

class Deck_XIFO:
    def __init__(self, size = 0) -> None:
        self.__data = deque(0 for _ in range(size))
    def push_back(self,item:int) -> None:
        self.__data.append(item)
    def push_front(self,item:int) -> None:
        self.__data.appendleft(item)
    def pop_back(self) -> int:
        return self.__data.pop()
    def pop_front(self) -> int:
        return self.__data.popleft()
    

def push_test(container, count:int, back = True):
    push = container.push_back if back else container.push_front
    for i in range(count): 
        push(i)

def pop_test(container, count:int, back = True):
    pop = container.pop_back if back else container.pop_front
    for _ in range(count):
        pop()
    



sizes = [ x * 10**n for n in range(int(argv[1])) for x in range(1,10) ]


fig,axs = plt.subplots(2,2)
fig.suptitle("List vs. Deck")

axs[0,0].set_title("Front insertion")
axs[0,0].plot(sizes, [timeit(lambda: push_test(List_XIFO(),size,False), number=1) for size in sizes], label="List")
axs[0,0].plot(sizes, [timeit(lambda: push_test(Deck_XIFO(),size,False), number=1) for size in sizes], label="Deck")
axs[0,0].legend()
axs[0,1].set_title("Back insertion")
axs[0,1].plot(sizes, [timeit(lambda: push_test(List_XIFO(),size), number=1) for size in sizes], label="List")
axs[0,1].plot(sizes, [timeit(lambda: push_test(Deck_XIFO(),size), number=1) for size in sizes], label="Deck")
axs[0,1].legend()
axs[1,0].set_title("Front removal")
axs[1,0].plot(sizes, [timeit(lambda: pop_test(List_XIFO(size),size,False), number=1) for size in sizes], label="List")
axs[1,0].plot(sizes, [timeit(lambda: pop_test(Deck_XIFO(size),size,False), number=1) for size in sizes], label="Deck")
axs[1,0].legend()
axs[1,1].set_title("Back removal")
axs[1,1].plot(sizes, [timeit(lambda: pop_test(List_XIFO(size),size), number=1) for size in sizes], label="List")
axs[1,1].plot(sizes, [timeit(lambda: pop_test(Deck_XIFO(size),size), number=1) for size in sizes], label="Deck")
axs[1,1].legend()


fig.tight_layout()
fig.savefig("results.png")