import random


def delete_pairs_iteratively(sequence:str):
    while "()" in sequence:
        pos = sequence.find("()")
        sequence = sequence[:pos] + sequence[pos+2:]
    return sequence == ""

def count_open_close(sequence:str):
    counter = 0
    for p in sequence:
        if p == "(" : counter += 1
        elif counter == 0: return False
        else: counter -= 1
    return counter == 0

def get_test_string(size):
    generator = ["(", ")"] * size
    random.shuffle(generator)
    return "".join(generator)

if __name__ == "__main__":
    for c in range(20):
        print(f"Test case {c+1}:... ", end="")
        s = get_test_string(100000)
        r1 = delete_pairs_iteratively(s)
        r2 = count_open_close(s)
        if r1 != r2: 
            print("NOK!!!!", s)
        else:
            print("OK")
