def factorial(number):
    fact = 1
    for multiplier in range(1, number+1):
        fact *= multiplier
    return fact


def binom(n, k):
    return factorial(n) // factorial(k) // factorial(n-k)


def draw_sierpinsky(depth):
    for row in range(depth):
        print(" "*(depth-row), end='')
        for column in range(row+1):
            if binom(row, column) % 2 == 1:
                print("██", end='')
            else:
                print("  ", end='')
        print()


depth = int(input("How big should the Sierpinsky triangle be? "))
draw_sierpinsky(depth)
