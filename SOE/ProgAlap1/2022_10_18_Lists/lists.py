depth = int(input("Milyen mely legyen a Pascal haromszog? "))

pascal_triangle = []

for d in range(depth):
    pascal_triangle.append([])
    if d == 0:
        pascal_triangle[-1].append(1)
    else:
        pascal_triangle[-1].append(1)
        for idx in range(1, d):
            value = pascal_triangle[-2][idx-1] + pascal_triangle[-2][idx]
            pascal_triangle[-1].append(value)
        pascal_triangle[-1].append(1)
print(pascal_triangle)


for row in pascal_triangle:
    print(row)


for idx,row  in enumerate(pascal_triangle):
    print(" "*(depth-idx), end='')
    for value in row:
        print(value, end=' ')
    print()

