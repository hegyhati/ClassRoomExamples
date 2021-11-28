def faktor (szam):
    faktorialis=1
    for szorzo in range(1,szam):
        faktorialis*=szorzo
    return faktorialis

def binom (n,k):
    return faktor(n) // (faktor(k)*faktor(n-k))

for n in range(int(input())):
    for k in range(n+1):
        print(binom(n,k), end=' ')    
    print()
