# Nützliche Werkzeuge

## Zwei weitere Containertypen: `tuple`, `set`

Ein `tuple` ist eine unveränderliche Liste und kann auch als Schlüssel in einem Dictionary verwendet werden.

```py
>>> my_tuple = (1,2,3)
>>> my_tuple[1]
2
>>> my_tuple[:2]
(1, 2)
>>> my_tuple[1] = 2
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    my_tuple[1] = 2
    ~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> my_tuple.append(4)
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    my_tuple.append(4)
    ^^^^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'append'
>>> 
```

`str` ist eine Menge, oder ein `dict` ohne Werte. 
Die Reihenfolge der Elemente ist nicht relevant; jedes Element kann nur einmal hinzugefügt werden.

```py
>>> empty_set = set()
>>> my_set = {1,2,3}
>>> my_set.add(4)
>>> my_set
{1, 2, 3, 4}
>>> my_set.add(2)
>>> my_set
{1, 2, 3, 4}
>>> 
```


## Einige `str` Methoden

```py
>>> "   foobar      ".strip()
'foobar'
>>> "Dies ist ein Satz".split()
['Dies', 'ist', 'ein', 'Satz']
>>> "1,2,3".split()
['1,2,3']
>>> 
```

## Comprehensions

Comprehensions sind nicht notwendig, können den Code aber deutlich verkürzen:

Statt:
```py
comma_separated_numbers = input()
numbers_as_str_in_list = comma_separated_numbers.split(",")
number_list = []
for num in numbers_as_str_in_list:
    number_list.append(int(num))
print(number_list)
```
kann man auch machen:
```py
number_list = [int(n) for n in input().split(",")]
print(number_list)
```

Comprehensions eignen sich auch gut zum Filtern.

```py
numbers = [int(n) for n in input().split(",")]
even_numbers = [n for n in numbers if n%2 == 0]
print(number_list)
```

## `match`-`case`

`match`‑`case` ist wie ein `switch`‑`case` aus C, aber mit mächtigem Pattern Matching (und ohne notwendige breaks):

```py
match numbers:
    case []: 
        print("Keine Zahlen.")
    case [x]: 
        print(f"Nur eine Zahl: {x}.")
    case [x, *rest]:
        print(f"{len(rest)+1} Zahlen beginnend mit {x}.")
```

## List sortieren `list.sort` with lambdas as well

`list.sort` sortiert die Elemente aufsteigend, oder mit `reverse=True` absteigend:

```py
>>> l = [3,5,1,7,2,9]
>>> l.sort()
>>> l
[1, 2, 3, 5, 7, 9]
>>> l.sort(reverse=True)
>>> l
[9, 7, 5, 3, 2, 1]
>>> 
```

Falls wir eine Liste von `dict`s oder Objekten haben, können wir ein `lambda` verwenden, um den Sortierwert zu erzeugen bzw. auszuwählen:

```py
>>> l = [ {"cost": 4, "benefit": 3}, {"cost": 5, "benefit":5}, {"cost": 12, "benefit": 13} ]
>>> l.sort(key=lambda d: d["cost"]) # sort by cost ascending
>>> l
[{'cost': 4, 'benefit': 3}, {'cost': 5, 'benefit': 5}, {'cost': 12, 'benefit': 13}]
>>> l.sort(key=lambda d: d["benefit"]/d["cost"], reverse=True) # sort by cost-benefit ratio descending
>>> l
[{'cost': 12, 'benefit': 13}, {'cost': 5, 'benefit': 5}, {'cost': 4, 'benefit': 3}]
>>> 
```

## Öffnen von (JSON-) Dataien

Textdatei öffnen und lesen:

```py
file = open("filename.txt")

for line in file:
    print(line)

file.close()
```

Besser (`close` automatisch):

```py
with open("filename.txt") as file:
    for line in file:
        print(line)
```

In eine Datei schreiben:

```py
with open("filename.txt", "w") as file:
    for num in range(10)
        file.write(f"{num}\n")
```

Dies überschreibt dieselbe Datei, wenn es zweimal ausgeführt wird. Um stattdessen anzuhängen:

```py
with open("filename.txt", "a") as file:
    new_line = input()
    file.write(new_line + "\n")
```

Wir können JSON‑Dateien jetzt als verschachtelte `list`/`dict` Strukturen (mit `str`, `int` usw.) betrachten, die in einer Datei gespeichert sind.

Aber:
 - keine `str` oder `tuple`
 - Dictionary‑Schlüssel müssen Strings sein
 - `true` / `false` statt `True` / `False`
 - `null` statt `None`

Sum Beispiel: [`marvel.json`](marvel.json)

Wir können diese JSON‑Datei öffnen, sie in eine Variable laden, mit einer Comprehension filtern und anschließend in eine andere Datei schreiben:

```py
import json

with open("marvel.json") as f:
    movies = json.load(f) # load file content into movies 

ironman_movies = [m for m in movies if "Ironman" in m["characters"]]

with open("ironman.json", "w") as f:
    movies = json.dump(ironman_movies,f) # save the filtered list to "ironman.json"
```