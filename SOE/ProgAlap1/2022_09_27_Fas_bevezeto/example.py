x = int(input())
y = int(input())

while x > 0:
    if x == y:
        print("Osztoja")
        exit()
    else:
        x = x + y

print("Nem osztoja")
