# Example Test

## Wahr oder falsch?

- `int` und `str` sind mutable
- Eine list, die als Funktionsargument übergeben wird, wird immer kopiert.
- Der maximale Wert, der in einem int gespeichert werden kann, ist 2**63‑1.
- Listen können in Dictionaries als Werte abgelegt werden.

## Wie lautet das Ergebnis dieser Ausdrücke?

 - `4 ** 0.5`
 - `"Hausaufgabe"[-5] * 3`
 - `[[1,2],[2,3]][-1][-1]`
 - `'Man lernt nie aus.'[2:3:10]`

## Was macht die Funktion? 

Ist die Funktion syntaktisch korrekt? Wenn nicht, wie würdest du sie korrigieren? Beschreibe ihren Zweck in einem Satz.


### f1

```py
def f1(l,x):
    for i in l:
        if i < x:
        print(i)
```

Wie lautet die Ausgabe für diese Aufrufe?
 - `f1([1,6,5,8,3,5,2,7,5,6], 4)`
 - `f1([1.2, 3.4, 5.6, 7.8], 9.0)`


### f2

```py 
def f2(l):
    d = {}
    for i in l:
        if i in d:
            d[i]++
        else:
            d[i] = 0
    return d


```
Wie lautet der Rückgabewert für diese Aufrufe?
 - `f2(["a","b","c","a","b","a","b","a","b"])`
 - `f2([1,2,3,4,5,6,7,8,9,8,7,6,7,8,9,8,7,8,9])`

## Was ist die Ausgabe?

```py

def g(l:list[int], x:int) -> int:
    if x >= 1 and x < len(l)-1:
        return (l[x-1]+l[x]+l[x+1])//3

def f(l:list[int]) -> list[list[int]]:
    l2 = []
    for idx in range(1,len(l)-1):
        l2.append(g(l),idx)
    l = l2
    print(l)

my_list = [8,13,21,34,55]
f(my_list)
print(my_list)
```

## Schreibe eine Funktion...
die eine Liste von Strings und einen String erhält. 
Danach gibt sie die Anzahl der Listenelemente zurück, die mit dem übergebenen String beginnen.

Beispiel-Ausgaben:

```py
>>> count_with_prefix( ["a", "ab", "ba", "aaa", "abba"], "a")
4
>>> count_with_prefix( ["a", "ab", "ba", "aaa", "abba"], "ab")
2
>>> count_with_prefix( ["a", "ab", "ba", "aaa", "abba"], "bab")
0
```




