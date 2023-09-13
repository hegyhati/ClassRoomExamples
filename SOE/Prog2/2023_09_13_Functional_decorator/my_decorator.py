from time import time

def generate_function_with_cpu_measure(func):
    def foo(*args, **kargs):
        print(f"Exectution of {func} with {args} and {kargs} starts now.")
        start = time()
        func(*args, **kargs)
        print(f"Execution ended in {time()-start}.")
    return foo

@generate_function_with_cpu_measure
def foobar(n:int):
    foo = 0
    for _ in range(n):
        foo += n ** n ** n

# foobar = generate_function_with_cpu_measure(foobar)
# Ez ekvivalens a @-ozassal

for n in range(8):
    foobar(n)
