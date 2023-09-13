from time import time

def measure_cpu(func, *args, **kargs):
    print(f"Exectution of {func} with {args} and {kargs} starts now.")
    start = time()
    func(*args, **kargs)
    print(f"Execution ended in {time()-start}.")


def foobar(n:int):
    foo = 0
    for _ in range(n):
        foo += n ** n ** n

def foobar2(n:int):
    foo = 0
    for _ in range(n ** n ** n):
        foo += n


measure_cpu(foobar, n=8)
measure_cpu(foobar2, 8)