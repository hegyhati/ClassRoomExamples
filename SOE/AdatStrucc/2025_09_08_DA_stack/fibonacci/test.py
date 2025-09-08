from timeit import timeit

def egyik(size):
    l = [1,1]
    for _ in range(size):
        l.append(l[-1]+l[-2])
        a = 4

def masik(size):
    l = [1]*(size+2)
    for idx in range(2,size+2):
        l[idx] = l[idx-1]+l[idx-2]

size = int(input())

print(timeit(lambda: masik(size), number=1))
print(timeit(lambda: egyik(size), number=1))