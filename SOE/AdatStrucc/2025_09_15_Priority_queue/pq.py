class PriorityQueue1:
    numbers: list[int]
    def __init__(self):
        self.numbers = []
    def put(self, x:int) -> None:
        for idx in range(len(self.numbers)):
            if x < self.numbers[idx]:
                self.numbers.insert(idx, x)
                return
        self.numbers.append(x)

    def pop_min(self) -> int:
        return self.numbers.pop(0)
    
class PriorityQueue2:
    numbers: list[int]
    def __init__(self):
        self.numbers = []
    def put(self, x:int) -> None:
        for idx in range(len(self.numbers)):
            if x > self.numbers[idx]:
                self.numbers.insert(idx, x)
                return
        self.numbers.append(x)

    def pop_min(self) -> int:
        return self.numbers.pop()
    
class PriorityQueue3:
    numbers: list[int]
    def __init__(self):
        self.numbers = []
    def put(self, x:int) -> None:
        self.numbers.append(x)
    def pop_min(self) -> int:
        minidx = 0
        for idx in range(len(self.numbers)):
            if self.numbers[idx] < self.numbers[minidx]:
                minidx = idx
        return self.numbers.pop(minidx)

class PriorityQueueHeap:
    # TODO
    pass