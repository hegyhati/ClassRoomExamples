"""
def factorial(number):
    factorial = 1
    for multiplier in range(1,number+1):
        factorial *= multiplier
    return factorial
"""

def factorial(number):
    #if number==0: return 1
    #else: return number * factorial(number-1)
    return 1 if number==0 else number * factorial(number-1)

def binom(n,k):
    return factorial(n)//factorial(k)//factorial(n-k)

depth = int(input())

for row in range(depth):
    for column in range(row+1):
        print(binom(n=row, k=column), end=' ')
    print()