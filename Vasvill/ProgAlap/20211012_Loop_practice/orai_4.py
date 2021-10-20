#  4. Kerjunk be `n`-t es csinaljunk listatt az elso `n` [Fibonacci](https://hu.wikipedia.org/wiki/Fibonacci-sz%C3%A1mok) szambol. Pl.: `8` ⟶ `[1, 1, 2, 3, 5, 8, 13, 21]`

n = int(input("Hany elemet irjam ki a Fibonnacci sorozatnak? "))

fibonacci = [1,1]

for _ in range(n-2):    
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

print(fibonacci)
