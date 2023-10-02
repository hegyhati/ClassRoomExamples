from random import sample

SIZE = 2 * 10 ** 4

base = list(range(SIZE * 100))

numbers = set(sample(base, k=SIZE))

count = 0

print("Kezdodik")
for a in numbers:
    for b in numbers:
        if a != b:
            d = b-a
            if  a + 2 * d in numbers and a + 3 * d in numbers and  a + 4 * d in numbers and  a + 5 * d in numbers: 
                count += 1
print(count)
    
                
