def Kollatz_next (n):
    if n%2==1:
        return 3*n+1
    else:
        return n//2

n=int(input())
while n!=1:
    print(n)
    n=Kollatz_next(n)
