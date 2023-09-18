class Stack_Interface:
    def push(self, item:str) -> None:
        pass
    def pop(self) -> str:
        pass
    def top(self) -> str:
        pass
    def empty(self) -> bool:
        pass

class Stack_with_List(Stack_Interface):
    pass

class Stack_with_Deque(Stack_Interface):
    pass

class Brace_Checker:
    def __init__(self, stack_cls) -> None:
        self._checker = stack_cls()
    def is_correct(input:str) -> bool:
        pass

checkers = {
    "List checker" : Brace_Checker(Stack_with_List),
    "Deque checker" : Brace_Checker(Stack_with_Deque)
}

for (name, checker) in checkers.items():
    # Iterate over all example files
    # Check the correctness of the input
    # log the output and execution time in "testresults_{datetime}.[json|csv]"
