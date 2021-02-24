def gcd(x,y):
    if x==y: return y
    else: return gcd(y,x%y)

print(gcd(123,34))
