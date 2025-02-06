def couple_finder(input: str) -> bool:
    while input != "":
        pos = input.find("()")
        if pos == -1: return False
        input = input[:pos]+input[pos+2:]
    return True

def depth_counter(input: str) -> bool:
    count = 0
    for c in input:
        if c == ")":
            if count == 0: return False
            else: count -= 1
        else:
            count += 1
    return count == 0


def nested_input(size:int) -> str:
    return "(" * size + ")" * size

def sequence_input(size:int) -> str:
    return "()" * size
