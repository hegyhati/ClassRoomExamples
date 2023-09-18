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

def check_braces(input:str, stack:Stack_Interface) -> bool:
    pass
    # implement brace correctness checking with the provided stack object


# Iterate over all example files
    # Check the correctness of the input with both stack implementation
    # log the output and execution time in "testresults_{datetime}.[json|csv]"
