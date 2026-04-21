## Wahr oder falsch? - 2 Punkte

- `list` kann in `dict` als Schlüssel abgelegt werden.
- Ein `dict`, die als Funktionsargument übergeben wird, wird immer kopiert.
- `list` ist mutable.
- Type‑Annotationen beeinflussen, wie der Code ausgeführt wird.

## Wie lautet das Ergebnis dieser Ausdrücke? - 2 Punkte

 - `2 * 2 ** 2`
 - `'1' in [1,"1",['1,1']]`
 - `[1,[1,[1,[1,[1]]]]] [1][1][1]`
 - `'Man lernt nie aus.'[1:10]`

## Was macht die Funktion? - 3 Punkte

Ist die Funktion syntaktisch korrekt? Wenn nicht, wie würdest du sie korrigieren? Beschreibe ihren Zweck in einem Satz.

```py
def f(l1,l2):
    l = {}
    for i in l1:
        if i in l2 and i not in l:
            l.append(i)
    return l
```

Wie lautet die Ausgabe für diese Aufrufe?
 - `f([1,2,3],[2,3,4])`
 - `f([1,1,1,2,2], [3,1])`


## Schreibe eine Funktion... - 3 Punkte
die zwei `str` erhält und ihr längstes gemeinsames Präfix zurückgibt. 
Du kannst annehmen, dass die beiden Strings die gleiche Länge haben.

Beispiel-Ausgaben:

```py
>>> longest_common_prefix( "Montag", "Monday" )
'Mon'
>>> longest_common_prefix( "Astrology", "Science!!" )
''
>>> longest_common_prefix( "school", "Schule" )
''
>>> longest_common_prefix( "foobar", "foobar" )
'foobar'
```




