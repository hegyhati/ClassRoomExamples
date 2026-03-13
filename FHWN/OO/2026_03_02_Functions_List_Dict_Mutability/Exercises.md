# Binomialkoeffizienten sind wunderbar

## `factorial(n)` 
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Erstelle eine Funktion, die eine ganze Zahl erwartet und deren Fakultät zurückgibt.
</div>

```py
def fact(n:int) -> int:
    prod = 1
    for mul in range(2,n+1):
        prod *= mul
    return prod

def fact_rec(n:int) -> int:
    return 1 if n < 2 else n * fact_rec(n-1)
```


## `binom(n,k)`
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Erstelle eine Funktion, die nach 2 Zahlen fragt und den entsprechenden Binomialkoeffizienten zurückgibt.
</div>

```py
def binom(n:int, k:int) -> int:
    return fact(n) // fact(k) // fact(n-k) 
```


## `pascal_triangle(depth)`
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Erstelle eine Funktion, die die Tiefe erwartet und das [Pascalsche Dreieck](https://en.wikipedia.org/wiki/Pascal%27s_triangle) mit dieser Tiefe ausgibt.
</div>

```py
def print_pascal_triangle(depth:int) -> None:
    for line in range(depth):
        for column in range(line+1):
            print(binom(line, column), end=" ")
        print()
```

Mit einer etwas schöneren Ausgabe:

```py
def print_pascal_triangle(depth:int) -> None:
    for line in range(depth):
        print("  " * (depth-line), end="")
        for column in range(line+1):
            print(f"{binom(line, column):^4}", end="")
        print()
```


## `sierpinski_triangle(depth)`
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Erstelle eine Funktion, die die Tiefe erwartet und das [Sierpiński Dreieck](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle) mit dieser Tiefe ausgibt.
</div>

```py
def print_sierpinski_triangle(depth:int) -> None:
    for line in range(depth):
        print(" " * (depth-line), end="")
        for column in range(line+1):
            print("  " if binom(line,column) % 2 == 0 else "██", end="")
        print()
```

Sehr schneller:

```py
def print_sierpinski_triangle_fast(depth:int) -> None:
    line = []
    while depth > 0:
        line.append(True)
        for idx in range(len(line)-2, 0, -1):
            line[idx] ^= line[idx-1]
        print(depth * " ", end="")
        for item in line:
            print("██" if item else "  ", end="")
        print()
        depth -= 1
```


# `greatest_common_divider(n,m)`
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Erstelle eine Funktion, die den größten gemeinsamen Teiler von zwei ganzen Zahlen zurückgibt.
</div>

Einfach aber langsam:

```py
def gcd(n:int, m:int) -> int:
    for d in range(n,0,-1):
        if n%d == 0 and m%d == 0:
            return d
```

Euklidischer Algorithmus:

```py
def gcd_eucledian(n:int, m:int) -> int:
    while m != 0:
        n,m = m,n%m
    return n
```



# Statistic
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Frage nach Zahlen, bis 0 eingegeben wird. 
Dann gib den Durchschnitt, den maximalen und den minimalen Wert aus.
</div>


## Code-Organisation

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Teile das Obige in 4 Funktionen, `main` sollte sein:

```py
data = input_numbers_until_0()
print(f"Numbers: {data}")
print(f"Average: {average_of_list(data)}")
print(f"Min: {min_of_list(data)}")
print(f"Max: {max_of_list(data)}")
```
</div>

```py
def input_numbers_until_0() -> list[int]:
    numbers = []
    while True:
        n = int(input("Nächste Zahl: "))
        if n == 0:
            return numbers
        else:
            numbers.append(n)

def min_of_list(numbers:list[int]) -> int:
    min = numbers[0]
    for item in numbers:
        if item < min:
            min = item
    return min

def max_of_list(numbers:list[int]) -> int:
    max = numbers[0]
    for item in numbers:
        if item > max:
            max = item
    return max

def average_of_list(numbers:list[int]) -> float:
    sum = 0
    for item in numbers:
        sum += item
    return sum / len(numbers)

data = input_numbers_until_0()
print(f"Numbers: {data}")
print(f"Average: {average_of_list(data)}")
print(f"Min: {min_of_list(data)}")
print(f"Max: {max_of_list(data)}")
```

Aber Python hat diese tatsächlich als eingebaute Methoden.

```py
data = input_numbers_until_0()
print(f"""
    Numbers: {data}
    Average: {sum(data)/len(data)}
    Min: {min(data)}
    Max: {max(data)}
""")
```

# [Differential Manchester Encoding](https://en.wikipedia.org/wiki/Differential_Manchester_encoding)

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Erstelle eine Funktion, die eine Folge von `0`,`5` (Volt)-Werten in eine andere Folge von `0` (kein Wechsel) und `1` (Wechsel) umwandelt.

Einige Beispiele:
```
>>> diff_machester_encode([0,0,0,0,0])
[0, 0, 0, 0]
>>> diff_machester_encode([0,5,0,0,5])
[1, 1, 0, 1]
>>> diff_machester_encode([0,5,0,5,0,5,0,5,0,5])
[1, 1, 1, 1, 1, 1, 1, 1, 1]
```
</div>


```py
def diff_machester_encode(signal:list[int]) -> list[int]:
    output = []
    for idx in range(len(signal)-1):
        output.append(0 if signal[idx]==signal[idx+1] else 1)
    return output
```

# LOGO 2.0

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Schreibe den Code von letzter Woche so um, dass die Schildkrötenposition in einem `dict` gespeichert wird und jeder kleine Teil in Funktionen ausgelagert ist.

`main` sollte sein:

```py
turtle = initialize_turtle()
while True:
    print(turtle)
    command = input("Befehl (FD/RT/EXIT): ")
    match command:
        case "EXIT": exit(0)
        case "FD": move_forward_1(turtle)
        case "RT": turn_right_90(turtle)
        case _ : print("Falscher Befehl.")
```
</div>

```py
def initialize_turtle():
    return {
        "x" : 0,
        "y" : 0,
        "deg" : 90
    }

def move_forward_1(turtle):
    match turtle["deg"]:
        case 0:
            turtle["x"] += 1
        case 90:
            turtle["y"] += 1
        case 180:
            turtle["x"] -= 1
        case 270:
            turtle["y"] -= 1

def turn_right_90(turtle):
    turtle["deg"] -= 90
    if turtle["deg"] < 0:
        turtle["deg"] += 360

turtle = initialize_turtle()
while True:
    print(turtle)
    pretty_print(turtle)
    command = input("Befehl (FD/RT/LT/EXIT): ")
    match command:
        case "EXIT": exit(0)
        case "FD": move_forward_1(turtle)
        case "RT": turn_right_90(turtle)
        case _ : print("Falscher Befehl.")
```

Eine etwas fortgeschrittenere Version:

```py
def initialize_turtle():
    return {
        "x" : 0,
        "y" : 0,
        "deg" : 90
    }

def move_forward(turtle, distance=1):
    match turtle["deg"]:
        case 0:
            turtle["x"] += distance
        case 90:
            turtle["y"] += distance
        case 180:
            turtle["x"] -= distance
        case 270:
            turtle["y"] -= distance

def turn(turtle, angle):
    turtle["deg"] += angle
    turtle["deg"] %= 360

def turtle_string(turtle):
    return "🐢" + {
        0   : "↦",
        90  : "↥",
        180 : "↤",
        270 : "↧",
    }[turtle["deg"]]

def pretty_print(turtle, size=10):
    for y in range(size,-size-1,-1):
        for x in range(-size,size+1):
            if x == turtle["x"] and y == turtle["y"]:
                print(turtle_string(turtle), end="")
            elif y==0 and x==0: 
                print("━╋━", end="")
            elif x==0: 
                print(" ┃ ", end="")
            elif y==0: 
                print("━━━", end="")
            else:
                print("   ", end="")
        print()



turtle = initialize_turtle()
while True:
    pretty_print(turtle)
    command = input("Befehl (FD/BK/RT/LT/EXIT): ")
    match command:
        case "EXIT": exit(0)
        case "FD": move_forward(turtle)
        case "RT": turn(turtle, -90)
        case "LT": turn(turtle, +90)
        case _ : print("Falscher Befehl.")
```

# LOGO 2.0

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Schreibe ein Programm, das eine Reihe von Experimenten ausführt und die Statistik in einem Histogramm ausgibt.
Das Experiment besteht darin, nnn sechsseitige Würfel zu werfen und die Augensumme zu bestimmen.

`main` sollte sein:

```py

dices = int(input("Wie viele Würfel? "))
repcount = int(input("Wie viele Experimente? "))
width = int(input("Wie breit soll das Histogramm sein? "))
count : list[int] = make_experiment(dices, repcount)
histogram(count, width)

```
Beispiel-Ausgabe:

```
Wie viele Würfel? 9
Wie viele Experimente? 1000000
Wie breit soll das Histogramm sein? 80
   9  0
  10  1
  11  3
  12  20
  13  50
  14  117
  15  297
  16  611
  17 █ 1195
  18 ██ 2342
  19 ████ 3819
  20 ██████ 6241
  21 ██████████ 9797
  22 ███████████████ 14572
  23 █████████████████████ 20520
  24 ████████████████████████████ 27452
  25 █████████████████████████████████████ 35674
  26 ██████████████████████████████████████████████ 44395
  27 ████████████████████████████████████████████████████████ 53496
  28 ████████████████████████████████████████████████████████████████ 61709
  29 ████████████████████████████████████████████████████████████████████████ 68739
  30 ████████████████████████████████████████████████████████████████████████████ 73260
  31 ███████████████████████████████████████████████████████████████████████████████ 75972
  32 ████████████████████████████████████████████████████████████████████████████████ 76242
  33 █████████████████████████████████████████████████████████████████████████████ 73845
  34 ███████████████████████████████████████████████████████████████████████ 68130
  35 ████████████████████████████████████████████████████████████████ 61622
  36 ███████████████████████████████████████████████████████ 52865
  37 ██████████████████████████████████████████████ 44088
  38 █████████████████████████████████████ 35832
  39 ████████████████████████████ 27626
  40 █████████████████████ 20388
  41 ███████████████ 14635
  42 ██████████ 9737
  43 ██████ 6204
  44 ████ 3901
  45 ██ 2280
  46 █ 1201
  47  626
  48  284
  49  134
  50  57
  51  21
  52  0
  53  0
  54  0
```
</div>


```py
import random

def diceroll() -> int:
    return random.randint(1,6)

def make_experiment(dicecount:int, repetition:int = 10**6) -> list[int]:
    count = [0]*(1+6*dicecount)
    for _ in range(repetition):
        sum = 0
        for _ in range(dicecount):
            sum += diceroll()
        count[sum] += 1
    return count

def histogram(count:list[int], width:int = 60) -> None:
    onehashmark = max(count) // width
    for idx,value in enumerate(count):
        if idx >= len(count) // 6: 
            blocks = value//onehashmark
            print(f"{idx:4} {"█" * blocks} {value}")

dices = int(input("Wie viele Würfel? "))
repcount = int(input("Wie viele Experimente? "))
width = int(input("Wie breit soll das Histogramm sein? "))
count : list[int] = make_experiment(dices, repcount)
histogram(count, width)
```

Die Darstellung als grafisches Diagramm mit `matplotlib`:
```py
import matplotlib.pyplot as plt
plt.barh(range(dices, 6*dices+1),count[dices:])
plt.show()
```