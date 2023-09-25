from collections import deque

class Stack:
    def __init__(self, size = 0) -> None:
        self.data = deque()
        for _ in range(size):
            self.push(0)
    def push(self, item:int) -> None:
        self.data.appendleft(item)
    def pop(self) -> int:
        self.data.popleft()
    def empty(self) -> bool:
        return len(self.data) == 0
 

if __name__ == "__main__":
    my_stack = Stack()

    my_stack.push(3)
    my_stack.push(4)
    a = my_stack.pop()
    print(a)
    a = my_stack.pop()
    print(a)
    if my_stack.empty():
        print("Empty")