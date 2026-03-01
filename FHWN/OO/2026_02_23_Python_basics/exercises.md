# Alter -> Milch / Almdudler / Bier

Frage nach dem Alter und gib aus, ob die Person Milch, Almdudler oder Bier trinken sollte.

```py
age = int(input("Alter: "))

if age < 0: 
    print("Fehler: Das Alter kann nicht kleiner als 0 sein.")
elif age < 6:
    print("Milch.")
elif age < 18:
    print("Almdudler.")
else:
    print("Bier.")
```

# Collatz

Frage nach einer Startzahl und setze dann die [Collatz-Folge](https://de.wikipedia.org/wiki/Collatz-Problem) fort, bis 1 erreicht ist.

```py
number = int(input("Startzahl: "))

print(number, end="")

while number != 1:
    if number % 2 == 0:
        number //= 2
    else:
        number = 3*number + 1
    print(f" → {number}", end="")
print()
```

# Formen in ASCII

## Rechteck

Frage nach der Breite und der Höhe eines Rechtecks und zeichne es mit `#`.


Mit `while`-Schleifen:

```py
height = int(input("Höhe: "))
width = int(input("Breite: "))

h = 0
while h < height:
    w = 0
    while w < width:
        print("#", end = "")
        w += 1
    h += 1
    print()
```

Mit `for`-Schleifen:

```py
height = int(input("Höhe: "))
width = int(input("Breite: "))

for _ in range(height):
    for _ in range(width):
        print("#", end = "")
    print()
```

Mit `str`-Operatoren:

```py
height = int(input("Höhe: "))
width = int(input("Breite: "))

print( ("#" * width + "\n") * height, end="")
```

Python ist Unicode-fähig:

```py
BLOCK = "██"

height = int(input("Höhe: "))
width = int(input("Breite: "))

print( (BLOCK * width + "\n") * height, end="")
```

## Nur Rahmen des Rechtecks

```py
BLOCK = "██"
HOLE = "░░"

height = int(input("Höhe: "))
width = int(input("Breite: "))

for h in range(height):
    if h==0 or h==height-1:
        print(BLOCK*width)
    else:
        print(BLOCK + HOLE*(width-2) + BLOCK)
```

Versuche herauszufinden, wann sich dieser Code falsch verhält. Eine gute Lösung mit einer `match`‑Anweisung:

```py
BLOCK = "██"
HOLE = "░░"

height = int(input("Höhe: "))
width = int(input("Breite: "))

match height,width:
    case 1,1: print(BLOCK)
    case 1,w: print(BLOCK*w)
    case h,1: print( (BLOCK+"\n") * h, end="")
    case h,w: 
        print(BLOCK*w)
        print( (h-2) * (BLOCK + HOLE*(w-2) + BLOCK + "\n"), end="")
        print(BLOCK*w)
```

## Viertelkreis

Frage nach dem Radius und zeichne dann den rechten unteren Viertelkreis.

```py
BLOCK = "██"

radius = int(input("Radius: "))

for x in range(radius+1):
    for y in range(radius+1):
        if x**2 + y**2 < radius**2:
            print(BLOCK, end="")
    print()
```

## Kreis

```py
BLOCK = "██"
HOLE = "░░"

radius = int(input("Radius: "))

for x in range(-radius,radius+1):
    for y in range(-radius, radius+1):
        if x**2 + y**2 < radius**2:
            print(BLOCK, end="")
        else:
            print(HOLE, end="")
    print()
```

Mit dem ternären Operator:

```py
BLOCK = "██"
HOLE = "░░"

radius = int(input("Radius: "))

for x in range(-radius,radius+1):
    for y in range(-radius, radius+1):
        print(BLOCK if x**2 + y**2 < radius**2 else HOLE, end="")
    print()
```
# Fibonacci

# Robot

