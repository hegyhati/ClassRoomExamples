from time import time
import matplotlib.pyplot as plt

def factorial_loop(n):
    fact = 1
    for num in range(1,n+1):
        fact *= num
    return fact


def factorial_recursive(n):
    return 1 if n == 0 else n * factorial_recursive(n-1)

def performance_test():
    cases = list(range(0,1000,10))
    for_ciklusos = []
    rekurziv = []

    for n in cases:

        start = time()
        factorial_loop(n)
        end = time()
        for_ciklusos.append(end-start)

        start = time()
        factorial_recursive(n)
        end = time()
        rekurziv.append(end-start)

    fig,ax = plt.subplots()
    ax.plot(cases, for_ciklusos, label="For loop")
    ax.plot(cases, rekurziv, label="Recursive")
    fig.legend()
    fig.savefig("factorial.png")

if __name__ == "__main__":
    performance_test()
