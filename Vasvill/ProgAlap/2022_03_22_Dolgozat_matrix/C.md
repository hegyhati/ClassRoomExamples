# Dolgozat 3 - C csoport
2022.03.22.

A dolgozat első feladata papíros, erre 5-10 perc áll rendelkezésre. A programozós feladatokra így 35-40 perc marad.

## Mit ír ki az alábbi program? (5p)
```python
def foo(a,b):
    print( 'a'*(b%a) )

for x in [3,2,4]:
    foo(x,10-x)
```

## Programozás (8p)

Írj programot, mely egyetlen bekéréssel beolvas néhány vesszővel elválasztott egész számot, majd kiírja a nemnegatívak összegét. Feltételezhető, hogy legalább egy szám meg lett adva, ha mindegyik negatív, akkor az összeg 0. A program használja rendeltetésszerűen a kért függvényt.

```python
def nemnegativokra_szures(szamlista):
    # ide ird a kodot, ami szamok egy listajat varja, es visszaad egy masikat, amiben mar csak a nemnegativak vannak
    pass

# Ide ird a kodot, ami beolvassa a vesszovel elvalasztott szamokat, majd kiirja a nemnegativak osszeget.
```

## Kódjavítás (6p)

Az alábbi program szóközökkel elválasztott szavakat kér be, majd kiírja azokat, amik ugyanolyan hosszúak, mint az első. Tehát `qwer ppppp poiu a bb cvbn`-re a kimenetben csak `qwer`, `poiu` és `cvbn` szerepel. Viszont több helyen hibás a program, ezeket a hibákat kell kijavítani. Pythontutort lehet (és érdemes) használni.


```python
words_with_spaces = read()
word_list = words_with_spaces.strip(' ')

length = len(word_list[1])
for word in word_list:
    if len(word) = longest:
        print(word)
```

