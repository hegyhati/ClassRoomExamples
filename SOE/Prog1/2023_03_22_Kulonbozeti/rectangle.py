width  = int(input("width="))
height = int(input("height="))

for row in range(height):
    for column in range(width):
        print("x", end='')
    print("")

print()

for row in range(height):
    print("x"*width)

