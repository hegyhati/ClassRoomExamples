# Binomialkoeffizienten sind wunderbar

## `factorial(n)` 
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Erstelle eine Funktion, die eine ganze Zahl erwartet und deren Fakultät zurückgibt.
</div>

## `binom(n,k)`
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Erstelle eine Funktion, die nach 2 Zahlen fragt und den entsprechenden Binomialkoeffizienten zurückgibt.
</div>


## `pascal_triangle(depth)`
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Erstelle eine Funktion, die die Tiefe erwartet und das [Pascalsche Dreieck](https://en.wikipedia.org/wiki/Pascal%27s_triangle) mit dieser Tiefe ausgibt.
</div>

## `sierpinski_triangle(depth)`
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Erstelle eine Funktion, die die Tiefe erwartet und das [Sierpiński Dreieck](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle) mit dieser Tiefe ausgibt.
</div>

# `greatest_common_divider(n,m)`
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Erstelle eine Funktion, die den größten gemeinsamen Teiler von zwei ganzen Zahlen zurückgibt.
</div>

# Statistic
<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">
Frage nach Zahlen, bis 0 eingegeben wird. 
Dann gib den Durchschnitt, den maximalen und den minimalen Wert aus.
</div>


## Code-Organisation

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Teile das Obige in 4 Funktionen, `main` sollte sein:

```py
my_list : list[int] = input_list()
print(my_list)
print(f"Min: {minimum(my_list)}, Max: {maximum(my_list)}, Average: {average(my_list)})
```
</div>

# [Differential Manchester Encoding](https://en.wikipedia.org/wiki/Differential_Manchester_encoding)

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Erstelle eine Funktion, die eine Folge von `0`,`5` (Volt)-Werten in eine andere Folge von `0` (kein Wechsel) und `1` (Wechsel) umwandelt.

Einige Beispiele:
```
>>> diff_machester_encode([0,0,0,0,0])
[0, 0, 0, 0]
>>> diff_machester_encode([0,5,0,0,5])
[1, 0, 0, 1]
>>> diff_machester_encode([0,5,0,5,0,5,0,5,0,5])
[1, 1, 1, 1, 1, 1, 1, 1, 1]
```
</div>

# LOGO 2.0

<div style="border:5px solid #3b82f6; border-left:20px solid #3b82f6;padding:12px; margin-bottom:30px; border-radius:6px;">

Schreibe den Code von letzter Woche so um, dass die Schildkrötenposition in einem `dict` gespeichert wird und jeder kleine Teil in Funktionen ausgelagert ist.

`main` sollte sein:

```py
turtle = initial_position()
while True:
    command = input_command()
    match command:
        case "EXIT": exit(0)
        case "FD": move_forward(turtle)
        case "RT": turn_right(turtle)
```
</div>

