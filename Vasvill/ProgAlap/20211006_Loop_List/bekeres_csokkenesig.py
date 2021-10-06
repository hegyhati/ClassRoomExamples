previous = float(input())
current = float(input())
while current > previous:
    previous = current
    current = float(input())
print("Highest value:",previous)