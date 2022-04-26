a = None
while not a:
    try:
        a = int(input('a= '))
    except ValueError:
        print("Nem egesz szamot adtal meg.")

b = None
while not b:
    try:
        b = int(input('b= '))
    except ValueError:
        print("Nem egesz szamot adtal meg.")

print(a+b)