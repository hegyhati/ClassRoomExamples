def get_sequence(number:int) -> list[int]:
    l = [number]
    while l[-1] != 1:
        if l[-1] % 2 == 1:
            l.append(l[-1]*3+1)
        else:
            l.append(l[-1]//2)
    return l

cache = {1: [1]}

def get_sequence_cached(number:int) -> list[int]:
    l = [number]
    while True:
        if l[-1] in cache:
            for idx, item in enumerate(l):
                cache[item] = l[idx:-1]+cache[l[-1]]
            return cache[l[0]]
        elif l[-1] % 2 == 1:
            l.append(l[-1]*3+1)
        else:
            l.append(l[-1]//2)