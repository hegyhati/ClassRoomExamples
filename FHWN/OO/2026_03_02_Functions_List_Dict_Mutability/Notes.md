# Python Grundlagen 2

## Funktionen

Funktionen haben wir in C schon verwendet. 
Es gibt eigentlich (mindestens) zwei wichtige Gründe, warum es gut ist, Code in mehrere Funktionen aufzuteilen:
 - Vermeidung der Codewiederholungen.
 - Aufteilung des Codes in kleinere Teile, die unabhängig entwickelt, überprüft und getestet werden können.

Beide sind nützlich, um das Fehlerrisiko zu minimieren.

Hier gibt es einige einfache Funktionen mit C-Äquivalenten:

<table><tr><th style="width: 50%;">C</th><th style="width: 50%;">Python</th></tr><tr><td style="vertical-align: top;">

```c
int smaller(int num1, int num2) {
    return num1 < num2 ? num1 : num 2;
}
```

</td><td style="vertical-align: top;">

```python
def smaller(num1,num2):
    return num1 if num1 < num2 else num 2
```

</td></tr><tr><td style="vertical-align: top;">

```c
bool isPrime(int number) {
    int i = 2;
    while (i*i < number) {
        if (number % i == 0)
            return false
        ++i;
    }
    return true;
}
```

</td><td style="vertical-align: top;">

```python
def is_prime(number):
    i = 2
    while i**2 < number:
        if number % i == 0:
            return False
        i += 1
    return True
```

</td></tr><tr><td style="vertical-align: top;">

```c
bool isPerfect(int number) {
    int dividerSum = 0;
    for (int i = 1; i <= number/2; ++i) 
        if (number % i == 1)
            dividerSum += i;
    return number == dividerSum;
}
```

</td><td style="vertical-align: top;">

```python
def is_perfect(number):
    divider_sum = 0
    for i in range(n//2 + 1):
        if number % i == 0:
            divider_sum += i
    return number == divider_sum
```

</td></tr></table>

### Typ

Im Allgemeinen ist es eine gute Idee, den Typ der Argumente und der Rückgabe zu annotieren.
Das hilft, z.B., solche Fehler zu vermeiden:

```py
def larger(num1, num2):
    return num1 if num1 > num2 else num2

x = input("Bitte eine Zahl eingeben: ")
y = input("Bitte noch eine Zahl eingeben: ")
print(f"{larger(x,y)} ist größer.")
```

Lass uns das testen:

```
$ python3 larger_number.py
Bitte eine Zahl eingeben: 3
Bitte noch eine Zahl eingeben: 5
5 ist größer.
$ 
```

Alles gut, ja? Nein, ein Test ist kein Test.

```
$ python3 larger_number.py
Bitte eine Zahl eingeben: 8
Bitte noch eine Zahl eingeben: 5
8 ist größer.

$ python3 larger_number.py
Bitte eine Zahl eingeben: 11
Bitte noch eine Zahl eingeben: 5
5 ist größer.

$ python3 larger_number.py
Bitte eine Zahl eingeben: 44444444444444
Bitte noch eine Zahl eingeben: 5
5 ist größer.

$ python3 larger_number.py
Bitte eine Zahl eingeben: 66
Bitte noch eine Zahl eingeben: 55555
66 ist größer.
```

Ich hoffe, dass der Fehler jetzt klar ist. 
Wir haben noch einmal vergessen, dass input einen `str` statt eines `int` zurückgibt.
Ohne Annotation warnt sogar mypy nicht vor dem Problem:

```
$ python3 -m mypy larger_number.py
Success: no issues found in 1 source file
```

Aber wenn wir die Annotation so hinzufügen...

```py
def larger(num1:int, num2:int) -> int:
    return num1 if num1 > num2 else num2
```

...dann meldet mypy die Probleme:

```
$ python3 -m mypy larger_number.py
larger_number.py:6: error: Argument 1 to "larger" has incompatible type "str"; expected "int"  [arg-type]
larger_number.py:6: error: Argument 2 to "larger" has incompatible type "str"; expected "int"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
```

> [!TIP]
> Als eine Faustregel: Versuche, immer Typannotationen zu Funktionen hinzuzufügen und `mypy` regelmäßig auszuführen, um solche Fehler zu erkennen.

Das größte Problem bei solchen versteckten Fehlern ist, dass das Programm ohne Warnung weiterläuft, sich aber falsch verhält.


### Pass-by-?

C ist eine Pass-by-Value-Sprache. Das bedeutet, dass wenn eine Variable als Argument an eine Funktion übergeben wird, ihr Wert in einen neuen Speicherbereich der Funktion kopiert wird.
Deshalb ist die Ausgabe dieses Codes 1 und nicht 2:

```c
void makedouble(int x){
    x *= 2;
}

int main() {
    number = 1;
    makedouble(number);
    printf("%d\n", number);
}
```

Die Ausgabe des Python-Äquivalents ist ebenfalls 1:

```py
def makedouble(x)
    x *= 2

number = 1
makedouble(number)
print(number)

```

Aber was im Hintergrund passiert, ist etwas anderes. Tatsächlich sind alle Variablen in Python Zeiger, also Referenzen.
Wenn eine Variable übergeben wird, wird diese Referenz kopiert und zeigt auf denselben Speicherbereich.
Aber `x *= 2` ist nur `x = x * 2`, bei dem zuerst der neue Wert `x*2` berechnet wird und dann die Referenz `x` auf einen neuen Speicherbereich zeigt, in dem dieser doppelte Wert gespeichert ist.

TODO: gif animation

## `list`

Python stellt einige eingebaute Containertypen bereit. 
Der einfachste ist die `list`, die am ehesten C‑Arrays ähnelt, aber es gibt wesentliche Unterschiede:

| | C Array | Python `list` |
| --- | --- | ---|
| Größe | **statisch** <br> feste Größe | **dynamisch** <br> veränderbare Größe |
| Typ der Elemente | **homohen**  <br> gleicher Typ | **inhomogen** <br> verschiedene Typen möglich |

Eine leere Liste können wir einfach erstellen:

```py
>>> my_list = []
>>> prinit(my_list)
[]
>>>
```

Wir können die Ausgangselemente ebenso einfach auflisten:
```
>>> my_list = [1,1,2,3,5,8]
>>> print(my_list)
[1, 1, 2, 3, 5, 8]
>>> dont_do_this_even_if_possible = [1, 2.0, "three", 4+0j, True, [6]]
>>> dont_do_this_even_if_possible
[1, 2.0, 'three', (4+0j), True, [6]]
>>> 
```

> [!TIP]
> Auch wenn es möglich ist, ist es normalerweise eine schlechte Idee, Variablen unterschiedlichen Typs in eine Liste zu setzen.
> (Polymorphismus wird später im Semester eine Ausnahme darstellen.)

Aber wir packen oft Listen in Listen, meistens um Matrizen zu modellieren.

```py
>>> laplacian_kernel = [
... [0, 1, 0],
... [1, -4, 1],
... [0, 1, 0]
... ]
>>> laplacian_kernel
[[0, 1, 0], [1, -4, 1], [0, 1, 0]]
>>> 
```

### Operatoren

Viele Operatoren arbeiten genauso wie für str:
 - `list + list`, `list += list`
 - `list * int`, `list *= int`
 - `list[int]`, `list[int:int:int]`
 - kein Operator, aber `len(list)` 

> [!tip]
> Probier das Verhalten dieser Operatoren – und vielleicht auch anderer, die wir nicht erwähnt haben – einfach aus.

`in` kann verwendet werden, um Elemente zu testen:

```py 
>>> 1 in [1,2,3]
True
>>> "apple" in ["banana", "potato"]
False
>>> 1 in [[1,2],[3,4]]
False
>>> "a" in ["apple", "ananas", "apricot"]
False
>>> 
```
Um ein Element nach Index zu löschen, kann der Operator `del` verwendet werden.

```py
>>> l = [1,2,3,4]
>>> del l[2]
>>> l
[1, 2, 4]
```

`del` funktioniert auch mit Slices:

```py
>>> l = [0,1,2,3,4,5,6,7,8,9]
>>> del l[1:7:2]
>>> l
[0, 2, 4, 6, 7, 8, 9]
```

### Methoden

`list` hat auch [viele nützliche Methoden](https://docs.python.org/3/tutorial/datastructures.html), wir werden jetzt nur einige kennenlernen.

> [!note] 
> Methoden sind Funktionen, die an eine "Variable" gebunden sind. 
Wir werden in der nächsten Einheit mehr darüber lernen.

`append` fügt ein neues Element am Ende der Liste ein (und erhöht die Größe um 1):

```py
>>> l = [1,2]
>>> l.append(3)
>>> l
[1, 2, 3]
```

Falls wir an einem Index ein neues Element einfügen möchten, brauchen wir `.insert(idx, value)`:

```py
>>> l = [1,2]
>>> l.insert(0,1000)
>>> l
[1000, 1, 2]
>>> l.insert(5555555555,0)
>>> l
[1000, 1, 2, 0]
```

Um ein Element nach Wert zu entfernen, können wir `remove` benutzen:

```py
>>> l = [1,2,1,3,1,4]
>>> l
[1, 2, 1, 3, 1, 4]
>>> l.remove(1)
>>> l
[2, 1, 3, 1, 4]
>>> l.remove(1)
>>> l
[2, 3, 1, 4]
>>> l.remove(1)
>>> l
[2, 3, 4]
>>> l.remove(1)
Traceback (most recent call last):
  File "<python-input-46>", line 1, in <module>
    l.remove(1)
    ~~~~~~~~^^^
ValueError: list.remove(x): x not in list
```

> [!tip]
> Schreib eine einfache Funktion, die alle Vorkommen eines Werts entfernt:
>
> ```py
> def remove_all(list_to_change:list[int], value:int) -> None
>    pass
>    ```

Um eine Liste zu leeren, kann `clear` aufgerufen werden:

```py
>>> l = [1,2,1,3,1,4]
>>> l
[1, 2, 1, 3, 1, 4]
>>> l.clear()
>>> l
[]
```

### `range`, `random.choices`

`range` ist eine Funktion, die eine „Liste“ von Zahlen einfach erzeugen kann. 
Eigentlich ist die Zurückgabe aber keine Liste, sondern etwas anderes, das sich jedoch leicht in eine Liste von int umwandeln lässt.

Die Argumente für `range` verhalten sich ähnlich wie bei Slices:

```py
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10,21))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> list(range(100,0,-1))
[100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
```

Falls wir eine zufällige Liste brauchen, kann die choices‑Funktion aus dem Modul random verwendet werden:

```py
>>> coin_flips = random.choices(["head", "tail"], k=10)
>>> coin_flips
['head', 'head', 'tail', 'head', 'head', 'tail', 'head', 'head', 'head', 'head']
>>> dice_rolls = random.choices(range(1,7), k=5)
>>> dice_rolls
[4, 2, 1, 6, 1]
```

`shuffle` ist auch nützlich:

```py
>>> l = list(range(20))
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> random.shuffle(l)
>>> l
[2, 16, 10, 13, 19, 6, 9, 17, 15, 8, 3, 7, 1, 0, 14, 4, 11, 5, 12, 18]
>>> random.shuffle(l)
>>> l
[18, 11, 0, 2, 17, 1, 4, 8, 3, 12, 16, 6, 9, 10, 7, 13, 19, 14, 15, 5]
>>> random.shuffle(l)
>>> l
[8, 10, 11, 3, 6, 1, 13, 17, 19, 12, 9, 18, 15, 2, 5, 14, 16, 0, 7, 4]
```

### (Im)mutability

Es gibt einen sehr wichtigen Unterschied zwischen all den anderen Typen, die wir bisher gelernt haben, und `list`:

>[!IMPORTANT]
> `int`, `float`, `bool` usw. sind **immutable**, aber `list` ist **mutable**.

Mutable bedeutet, dass der Inhalt verändert werden kann. 

#### 💬 Aber haben wir die Werte von `int` nicht auch schon verändert?

Nein, wir haben die `int`‑Variablen nur **reassigned** (neu zugewiesen).

Der unterschied zwischen **reassignment** und **mutation** (Wertänderung) ist sehr wesentlich!

Einige Beispiele mit Reassignment für zwei immutable Typen (`int`, `str`) und einen mutable Typ (`list`):

<table>
<tr>
    <th></th>
    <th><code>int</code></th>
    <th><code>str</code></th>
    <th><code>list</code></th>
</tr>
<tr>
<td>Reassignment</td>
<td style="vertical-align: top;">

```py
>>> a = 1
>>> a = 2
>>> a
2
```
</td><td style="vertical-align: top;">

```py
>>> s = "foo"
>>> s = "bar"
>>> s
'bar'
```
</td><td style="vertical-align: top;">

```py
>>> l = [1,2,3]
>>> l = []
>>> l
[]
```
</td>
</tr>
<tr>
<td>Reassignment<br>andere Variable</td>
<td style="vertical-align: top;">

```py
>>> a = 1
>>> b = a
>>> b = 2
>>> a
1
```
</td><td style="vertical-align: top;">

```py
>>> s = "foo"
>>> s2 = s
>>> s2 = "bar"
>>> s
'foo'
```
</td><td style="vertical-align: top;">

```py
>>> l = [1,2,3]
>>> l2 = l
>>> l2 = []
>>> l
[1, 2, 3]
```
</td>
</tr>
<tr>
<td>Reassignment<br>Funktionargumente</td>
<td style="vertical-align: top;">

```py
>>> def double(x:int):
...     x = x * 2
...     
>>> a = 2
>>> double(a)
>>> a
2

```
</td><td style="vertical-align: top;">

```py
>>> def double(s:str):
...     s = s * 2
...     
>>> s = "foo"
>>> double(s)
>>> s
'foo'
```
</td><td style="vertical-align: top;">

```py
>>> def double(l:list):
...     l = l * 2
...     
>>> l = [1,2]
>>> double(l)
>>> l
[1, 2]

```
</td>
</tr>
</table>

Mutation is nicht möglich für `int`, `float`, usw.

Auch keine Änderung möglich für `str`.:

```py
>>> s = "foo"
>>> s2 = s
>>> s2[2] = "r"
Traceback (most recent call last):
  File "<python-input-81>", line 1, in <module>
    s2[2] = "r"
    ~~^^^
TypeError: 'str' object does not support item assignment
```

Eine `list` kann aber verändert werden:

```py
>>> l = [1,2,3]
>>> l[1]=222222222
>>> l
[1, 222222222, 3]
```

Wenn zwei Listenvariablen derselben Liste zugewiesen sind, wirkt sich eine Veränderung/Mutation über die eine natürlich auch auf die andere aus:

```py
>>> l = [1,2,3]
>>> l2 = l
>>> l2[1]=222222222
>>> l
[1, 222222222, 3]
>>> l2
[1, 222222222, 3]
```
Das passiert auch, wenn eine Listenvariable als Argument an eine Funktion übergeben wird:

```py
>>> def append_size(l:list[int]) -> None:
...     l.append(len(l))
...     
>>> my_list = [11,22,33]
>>> append_size(my_list)
>>> my_list
[11, 22, 33, 3]

```

Beobachte den Unterschied im Verhalten zwischen einer Reassignment und einer Veränderung/Mutation:

```py
>>> l = [1,2,3]
>>> l2 = l      # Andere Variable derselbe Liste zugewiesen
>>> l2 = []     # Reassignment für l2
>>> l2          #   l2 erzeugt eine neue Liste... 
[]              #   ... die nichts enthält.
>>> l           # Aber l1 zeigt weiterhin auf die ursprüngliche Liste.
[1, 2, 3]       
>>> l2 = l      # l2 ist wieder derselbe Liste zugewiesen
>>> l2
[1, 2, 3]
>>> l2[1] = 222 # Zweite Element der Liste ist bei l2 verändert = Mutation
>>> l2          
[1, 222, 3]     # Die Veränderung ist in l2 natürlich sichtbar...
>>> l
[1, 222, 3]     # ... aber auch in l, weil sowohl l als auch l2 auf dieselbe Liste zeigen.
```

## `for`-Schleifen

For‑Schleifen werden verwendet, wenn wir etwas mit jedem Element einer Liste machen möchten:

```py
l = [1,1,2,3,5,8]
for number in l:
    print("f{number} ist {'gerade' if number%2==0 else 'ungerade'}.")
```

Damit ist die For‑Schleife eigentlich eine For‑Each‑Schleife und nicht so ähnlich wie die For‑Schleife in C.

Falls man [etwas](https://youtu.be/wjOfQfxmTLQ?si=Wp1zdoX1j65vOOMX) `n`-mal ausführen möchte, erzeugt man eine n‑Elemente‑Liste (meistens mit `range`) und benutzt die Schleifenvariable im Schleifenrumpf nicht:

```py
for _ in range(100):
    print("Romani ite domum")
```

aber man könnte auch:

```py
for bart in ["simpson"] * 100:
    print("I will not burp in class.")
```
> [!Note]
> `_` ist nichts Besonderes, nur ein Variablenname wie jeder andere. 
> Aber es ist eine Konvention, `_` zu verwenden, wenn keine Absicht besteht, die Schleifenvariable zu benutzen.

> [!Important]
> Reassignment der Schleifenvariable ändert die List-Elemente nicht!
> ```py
> l = [1, 2, 3]
> for number in l:
>     number = 5
> print(l) # Ausgabe ist [1,2,3], nicht [5,5,5]
> ```

Wenn man die Listelemente tauschen (reassignen) möchte, sollte man das über den Index machen:

```py
l = ["apfel", "banana", "erdbeere"]
for idx in [0,1,2]:
    l[idx] = "obst"
print(l) # Ausgabe ist ["obst", "obst", "obst"]
```

`[0, 1, 2]` sind die gültigen Indizes für `l`. 
Aber normalerweise wissen wir nicht, wie viele Elemente `l` hat, also möchten wir dynamisch die Liste `[0, 1, …, len(l) – 1]` erzeugen. 
Das kann man mit `range(len(l))` machen:

```py
l = [1,2,3]
for idx in range(len(l)):
    l[idx] *= 2
print(l) # Ausgabe ist [2,4,6]
```

Manchmal braucht man einfachen Zugriff sowohl auf den Wert als auch auf den Index. 
Dann kann man die Funktion `enumerate` verwenden:

```py
l = ["Eins", "zwei", "Polizei"]
for idx,value in enumerate(l):
    print(f"l[{idx}]: {value})
```

## `dict`

Listen sind wunderbar, wenn man Werte ähnlicher Natur zusammenfassen möchte.

Aber sie sind nicht wirklich nützlich, wenn man Werte unterschiedlicher Natur in einer Datenstruktur gruppieren möchte. 
Ein Job hat zum Beispiel vielleicht eine Deadline, eine Priorität, eine Liste von Aufgaben usw. 
Erst, diese Werte haben untershiedliche Typen. 
Außerdem möchten wir in diesem Fall nicht per Index auf diese Daten zugreifen, da sie nicht das n-te Vorkommen derselben Sache sind. 
Vielmehr haben sie unterschiedliche semantische Bedeutungen, sodass wir meistens per Namen, also per `str`, auf sie zugreifen möchten. 

In Python können Dictionaries/Wörterbücher diesen Zweck erfüllen.
Eigentlich ist ein `dict` nur eine Menge von Schlüssel‑Wert‑Paaren.

```py
agelimits = {"beer" : 16, "cigarette" : 18, "Kinder egg" : 6}

job : dict = {
    "deadline" : "2026-04-26",
    "client" : "OBB",
    "priority" : 1,
    "tasks" : [
        "requirements analysis',
        "system design",
        "module design",
        "development",
        "testing",
        "deployment",
        "maintenance"
    ]
}
```

> [!NOTE]
> Nicht nur die Werte, sondern auch die Schlüssel können unterschiedliche Typen haben, solange sie immutable sind. 
> Allerdings sind in den meisten Fällen alle Schlüssel Strings. 
> Diese ist ebenfalls möglich, aber es gibt praktisch keinen Grund, es so zu machen:
> ```py
> dont_do_this_even_if_syntactically_correct  = {
>     "foo" : "bar",
>     True: False,
>     1 : True,
>     1.0 : 4+3j,    
> }
> ```

### Operatoren


Auf den Wert zu einem Schlüssel zuzugreifen oder ihn neu zuzuweisen, ist genauso einfach wie mit Indizes bei `list`:

```py
date = {
    "year" : 2026,
    "month" : 3,
    "day" 26
}

print(date['year']) # Wert zu Schlüssel "year" zugreifen
date["month"] += 1  # Neuen Wert zu Schlüssel "month" zuweisen 
```

`del` kann verwendet werden, um ein Schlüssel‑Wert‑Paar zu entfernen:

```py
ages = {
    "Anna" : 12,
    "Bob" : 34,
    "Cecil" : 56 
}
del ages["Anna"]
print(ages) # Ausgabe: {"Bob": 34, "Cecil": 56}
```

`in` gibt zurück, ob ein Schlüssel in einem Dict verfügbar ist:

```py
>>> d = {"a": 1, "b": 2}
>>> "a" in d
True
>>> "A" in d
False
>>> "b" not in d
False
```

Schließlich gibt `len` die Anzahl der Schlüssel‑Wert‑Paare zurück:

```py
>>> len({"a": 1, "b": [1,2,3,4]})
2
```

### Methoden

Ähnlich wie `list` hat auch `dict` die Methode `clear()`. 
Schlüssel und Werte können mit `keys()` und `values()` zurückgegeben werden.
Um eine Liste von Schlüssel‑Wert‑Paaren zu erhalten, kann `items()` verwendet werden.
Natürlich gibt es noch [andere Methoden](https://docs.python.org/3/library/stdtypes.html#dict).

### Schleifen

for `x in my_dict` iteriert über die Schlüssel. 
Wenn man die Werte oder sowohl die Schlüssel als auch die Werte braucht, sollte man die oben genannten Methoden verwenden:

```py
>>> countries = {"AT":"Austria", "HU":"Hungary", "DE": "Germany"}
>>> for code in countries:
        print(code)

AT
HU
DE
>>> for name in countries.values():
        print(country)

Austria
Hungary
Germany
>>> for code, name in countries.items():
        print(code, name)
AT Austria
HU Hungary
DE Germany
```

### Nesting lists and dictionaries

Hierarchische Daten können einfach in einer verschachtelten Listen‑Dict‑Datenstruktur gespeichert werden.

Einige Beispiele:

```py
hutten = [
    {
        "name" : "Edelweißhütte",
        "osm" : "https://www.openstreetmap.org/way/132613067",
        "web" : "https://www.alpenverein.at/edelweisshuetteamschneeberg/",
        "wiki" : "https://de.wikipedia.org/wiki/Edelweissh%C3%BCtte_%28Rax-Schneeberg-Gruppe%29"
        "position" : {
            "longitude": "15° 48′ 54″ O", 
            "latitude": "47° 47′ 31″ N",
            "altitude": 1235
        }, 
        "contact" : {
            "phone" : [
                "+43 2636 3616",
                "+43 2636 3616"
            ],
            "email" : ["info@edelweishuette.at"]
        },
        "services" : {
            "food" : {
                "Gulasch" : 12.50,
                "Kaiserschmarrn" : 8.75,
                "Apfelstrudel" : 6.50,
                "Wiener Schnitzel" : 14.00
            }, 
            "accomodation" : [
                {
                    "name": "Doppelzimmer",
                    "capacity": 2,
                    "price_per_night": 45.00
                },
                {
                    "name": "Einzelzimmer",
                    "capacity": 1,
                    "price_per_night": 28.00
                },
                {
                    "name": "Mehrbettzimmer",
                    "capacity": 4,
                    "price_per_night": 75.00
                }
            ]                
        }
    },
    {
        "name" : "Ohlschutzhuette",
        "osm" : "https://www.openstreetmap.org/way/...",
        "web" : "https://www.alpenverein.at/ohlschutzhuette/",
        "wiki" : "https://de.wikipedia.org/wiki/Ohlschutzhuette",
        "position" : {
            "longitude": "15° 45′ 00″ O", 
            "latitude": "47° 45′ 00″ N",
            "altitude": 1200
        }, 
        "contact" : {
            "phone" : ["+43 2636 789"],
            "email" : ["info@ohlschutzhuette.at"]
        },
        "services" : {
            "food" : {
                "Gulasch" : 12.00,
                "Kaiserschmarrn" : 8.50,
                "Apfelstrudel" : 6.00,
                "Wiener Schnitzel" : 13.50
            }, 
            "accomodation" : [
                {
                    "name": "Doppelzimmer",
                    "capacity": 2,
                    "price_per_night": 40.00
                },
                {
                    "name": "Einzelzimmer",
                    "capacity": 1,
                    "price_per_night": 25.00
                }
            ]                
        }
    },
    {
        "name" : "Hengsttalhuette",
        "osm" : "https://www.openstreetmap.org/way/...",
        "web" : "https://www.alpenverein.at/hengsttalhuette/",
        "wiki" : "https://de.wikipedia.org/wiki/Hengsttalhuette",
        "position" : {
            "longitude": "15° 50′ 00″ O", 
            "latitude": "47° 50′ 00″ N",
            "altitude": 1400
        }, 
        "contact" : {
            "phone" : ["+43 2636 234"],
            "email" : ["info@hengsttalhuette.at"]
        },
        "services" : {
            "food" : {
                "Gulasch" : 13.00,
                "Kaiserschmarrn" : 9.00,
                "Apfelstrudel" : 7.00,
                "Wiener Schnitzel" : 15.00
            }, 
            "accomodation" : [
                {
                    "name": "Doppelzimmer",
                    "capacity": 2,
                    "price_per_night": 50.00
                },
                {
                    "name": "Einzelzimmer",
                    "capacity": 1,
                    "price_per_night": 30.00
                },
                {
                    "name": "Mehrbettzimmer",
                    "capacity": 4,
                    "price_per_night": 80.00
                }
            ]                
        }
    }
]
```
(Die Daten sind teilweise von einem LLM generiert und sollten nicht exakt übernommen werden.)
