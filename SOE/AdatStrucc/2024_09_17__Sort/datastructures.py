

class PriorityQueue:
    def __init__(self, max_queue:bool = True) -> None:
        self._data = []
        self.max_queue = max_queue
    def push(self, number:int) -> None: # O(n)
        for idx, item in enumerate(self._data): # O(n)
            if self.max_queue and number < item or not self.max_queue and number > item:
                self._data.insert(idx,number) # O(n)
                break
        else:
            self._data.append(number)
    def pop_max(self) -> int:
        return self._data.pop()
    def is_empty(self) -> bool:
        return len(self._data) == 0