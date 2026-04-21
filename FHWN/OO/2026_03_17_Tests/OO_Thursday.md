## Wahr oder falsch? - 2 Punkte

- Typannotationen für Argumente werden bei jedem Aufruf vom Interpreter geprüft.
- `dict` kann in `dict` als Wert abgelegt werden.
- Einrückung ist nur eine stilistische Entscheidung in Python.
- `dict` ist immutable.

## Wie lautet das Ergebnis dieser Ausdrücke? - 2 Punkte

 - `[-1,[-1,[-1,[-1,[-1]]]]] [-1][-1][-1]`
 - `'Man lernt nie aus.'[-10:-1]`
 - `'2' * 2 ** 2`
 - `'1' in [1,'11',["1"]]`

## Was macht die Funktion? - 3 Punkte

Ist die Funktion syntaktisch korrekt? Wenn nicht, wie würdest du sie korrigieren? Beschreibe ihren Zweck in einem Satz.

```py
def f(l1,l2)
    l = []
    for i in l1+l2
        if i not in l
            l.append(i)
    return l
```

Wie lautet die Ausgabe für diese Aufrufe?
 - `f([1,2,3],[2,3,4])`
 - `f([1,1,1,2,2], [3,1])`


## Schreibe eine Funktion... - 3 Punkte
die zwei `str`‑Argumente erhält und zurückgibt, wie oft der zweite String im ersten vorkommt (einschließlich überlappender Vorkommen). Die Verwendung der Methode `str.count` ist **NICHT** erlaubt.

Beispiel-Ausgaben:

```py
>>> count( "A bissl wos geht immer.", "s")
3
>>> count( "Python", "Ohne Fleiß kein Preis." )
0
>>> count( "Na, na, na, na, na, na, Batman!", "na" )
5
>>> count( "Na, na, na, na, na, na, Batman!", "na, na, na" )
3
```




