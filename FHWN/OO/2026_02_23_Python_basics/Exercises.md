# Alter -> Milch / Almdudler / Bier

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Frage nach dem Alter und gib aus, ob die Person Milch, Almdudler oder Bier trinken sollte.
</div>

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
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Frage nach einer Startzahl und setze dann die [Collatz-Folge](https://de.wikipedia.org/wiki/Collatz-Problem) fort, bis `1` erreicht ist.
</div>

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

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Frage nach der Breite und der Höhe eines Rechtecks und zeichne es mit `#`.
</div>

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
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Dasselbe, aber mache das Rechteck hohl.
</div>


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
> [!tip]
> Versuche herauszufinden, wann sich dieser Code falsch verhält. 
 
Eine gute Lösung mit einer `match`‑Anweisung:

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
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Frage nach dem Radius und zeichne dann den rechten unteren Viertelkreis.
</div>

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
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Mach den ganzen Kreis.
</div>

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

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Frage nach einer ganzen Zahl `n`. Dann gib die ersten `n` Elemente der Fibonacci-Folge aus.
</div>

```py
n = int(input("n: "))
if n < 0:
    print("Fehler: n sollte mindestens 0 sein.")
    exit(1)
if n == 0:
    print()
elif n == 1:
    print("1")
elif n == 2:
    print("1, 1")
else:
    print("1, 1", end="")
    remaining = n-2
    smaller = 1
    larger = 1
    while remaining > 0:
        tmp = larger + smaller
        smaller = larger
        larger = tmp
        print(f", {larger}", end="")
        remaining -= 1
    print()
```
Eine etwas kürzere Version mit for-Schleifen und Tupelzuweisung:

```py
n = int(input("n: "))

if n < 0:
    print("Fehler: n sollte mindestens 0 sein.")
    exit(1)

if n == 0:
    print()
    exit(0)

print("1", end="")
smaller = 0
larger = 1
for _ in range(n-1):
    larger,smaller = larger+smaller,larger
    print(f", {larger}", end="")
print()
```

# Logo

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Erstelle einen vereinfachten [LOGO](https://en.wikipedia.org/wiki/Logo_(programming_language))-Interpreter. Die Schildkröte startet bei Position `0`,`0` und schaut nach Norden.

Es gibt drei Befehle, die die Schildkröte akzeptieren soll: 

 - **FD** bewegt die Schildkröte einen Schritt nach vorne.
 - **RT** dreht sie 90 Grad im Uhrzeigersinn.
 - **EXIT** beendet das Programm. 
 
Vor jedem Befehl soll die Position und die Richtung der Schildkröte ausgegeben werden.

Beispielausführung des Programms:

```
Position: (0,0), Richtung: ↑
Befehl (FD/RT/EXIT): FD

Position: (0,1), Richtung: ↑
Befehl (FD/RT/EXIT): FD

Position: (0,2), Richtung: ↑
Befehl (FD/RT/EXIT): RT

Position: (0,2), Richtung: →
Befehl (FD/RT/EXIT): FD

Position: (1,2), Richtung: →
Befehl (FD/RT/EXIT): EXIT
```
</div>


```py
pos_x = 0
pos_y = 0
direction = "n"

while True:
    print(f"Position: ({pos_x},{pos_y}), Richtung: ", end="")
    if direction == "n":
        print("↑")
    elif direction == "e":        
        print("→")
    elif direction == "s":
        print("↓")
    elif direction == "w":
        print("←")

    command = input("Befehl (FD/RT/EXIT): ")

    if command == "EXIT":
        exit()

    elif command == "FD":
        if direction == "n":
            pos_y += 1
        elif direction == "e":
            pos_x += 1
        elif direction == "s":
            pos_y -= 1
        elif direction == "w":
            pos_x -= 1
        
    elif command == "RT":
        if direction == "n":
            direction = "e"
        elif direction == "e":
            direction = "s"            
        elif direction == "s":
            direction = "w"
        elif direction == "w":
            direction = "n"

    else:
        print("Falscher Befehl.")
```

Eine kürzere, trickreichere Lösung.
Es ist eine gute Übung, herauszufinden und zu verstehen, wie es funktioniert.

```py
pos_x, pos_y, direction = 0,0,0
while True:
    print(f"Position: ({pos_x},{pos_y}), Richtung: {"↑→↓←"[direction]}")
    command = input("Befehl (FD/RT/EXIT): ")
    match command:
        case "EXIT":
            exit()
        case "FD":
            if direction % 2 == 0: pos_x -= direction - 1
            else: pos_y -= direction - 2
        case "RT":
            direction = (direction + 1) % 4
        case _: 
            print("Falscher Befehl.")
```

