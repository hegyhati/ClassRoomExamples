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

Einige Beispiele für zwei immutable Typen (`int`, `str`) und einen mutable Typ (`list`):

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
<tr>
<td>Mutation<br>andere Variable</td>
<td style="vertical-align: top;">

Keine Änderung möglich für `int`.

</td><td style="vertical-align: top;">

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
</td><td style="vertical-align: top;">

```py
>>> l = [1,2,3]
>>> l2 = l
>>> l2[1]=222222222
>>> l
[1, 222222222, 3]
>>> l2
[1, 222222222, 3]

```
</td>
</tr>
<tr>
<td>Mutation<br>Funktionargumente</td>
<td style="vertical-align: top;">

Keine Änderung möglich für `int`.

</td><td style="vertical-align: top;">

Keine Änderung möglich für `str`.

</td><td style="vertical-align: top;">

```py
>>> def append_size(l:list[int]) -> None:
...     l.append(len(l))
...     
>>> my_list = [11,22,33]
>>> append_size(my_list)
>>> my_list
[11, 22, 33, 3]

```
</td>
</tr>
</table>


## `for`-Schleifen

## `dict`

### Operatoren

### Methoden
