class PriorityList:
    def __init__(self) -> None:
        self._data = []
    def push(self, item:int) -> None:
        idx = 0
        while idx < len(self._data):
            if self._data[idx] > item:
                self._data.insert(idx,item)
                return
            idx += 1
        self._data.append(item)
    def get_max(self) -> int:
        return self._data.pop()
    
class LazyPriorityList:
    def __init__(self) -> None:
        self._data = []
    def push(self, item:int) -> None:
        self._data.append(item)
    def get_max(self) -> int:
        maxidx = 0
        for idx in range(len(self._data)):
            if self._data[idx] > self._data[maxidx]:
                maxidx = idx
        return self._data.pop(maxidx)

from collections import deque
class PriorityDequeue:
    def __init__(self) -> None:
        self._data = deque()
    def push(self, item:int) -> None:
        for idx, num in enumerate(self._data):
            if num > item:
                self._data.insert(idx, item)
                return 
        self._data.append(item)
    def get_max(self) -> None:
        return self._data.pop()


import queue
class PriorityQueue:
    def __init__(self) -> None:
        self._data = queue.PriorityQueue()
    def push(self, item:int) -> None:
        self._data.put(-item)
    def get_max(self) -> int:
        return -self._data.get()
        