def factorial (number):
    result=1
    for i in range(1,number+1):
        result*=i
    return result

def binom (n, k):  
    return factorial(n) // (factorial(k) * factorial(n-k))

def pascal(row_count):
    for n in range(row_count):
        print(" "*(row_count-n), end='')
        for k in range(n+1): 
            print(binom(n,k)  , end=' ')    
        print()

def sierpinsky(row_count):
    for n in range(row_count):
        print(" "*(row_count-n), end='')
        for k in range(n+1): 
            print("X" if binom(n,k)%2==1 else " ", end=' ')
        print()

print(factorial(row_count))
pascal(row_count)
sierpinsky(row_count)


