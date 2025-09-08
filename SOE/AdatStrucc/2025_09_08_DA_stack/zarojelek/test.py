from timeit import timeit
from sys import argv

def nested(size): return "(" * size + ")" * size

def test(foo:str):
    open_braces = []
    for c in foo:
        if c in "({[":
            open_braces.append(c)
        else:
            if len(open_braces) == 0: return False
            if c == ")" and open_braces[-1] == "(" or c == "]" and open_braces[-1] == "[" or c == "}" and open_braces[-1] == "{": open_braces.pop()
            else: return False
    return len(open_braces) == 0

def test2(foo:str):
    open_braces = []
    for c in foo:
        if c in "({[":
            open_braces.insert(0,c)
        else:
            if len(open_braces) == 0: return False
            if c == ")" and open_braces[-1] == "(" or c == "]" and open_braces[-1] == "[" or c == "}" and open_braces[-1] == "{": del open_braces[0]
            else: return False
    return len(open_braces) == 0

print(timeit(lambda:test(nested(int(argv[1]))), number=1))
print(timeit(lambda:test2(nested(int(argv[1]))), number=1))