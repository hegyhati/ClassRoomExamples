# Dolgozat 3 - A csoport
2022.03.22.

A dolgozat első feladata papíros, erre 5-10 perc áll rendelkezésre. A programozós feladatokra így 35-40 perc marad.

## Mit ír ki az alábbi program? (5p)
```python
def foo(a,b=1):
    for _ in range(a):
        print(b)

for x in [1,4,5,2]:
    foo(x,1-x)
```

## Programozás (8p)

Írj programot, mely egyetlen bekéréssel beolvas három vesszővel elválasztott egész számot, majd kiírja, hogy pithagoraszi számhármasok-e. (Az egyik négyzete megegyezik-e a másik kettő négyzetösszegével, pl: 3,4,5). A három szám nincs feltétlenül növekvő sorrendben. A főprogram használja rendeltetésszerűen a kért függvényt.

```python
def pithagoraszi_szamharmas(a,b,c):
    # ide ird a kodot, ami visszater True-val, ha a 3 szam pithagoraszi szamharmas, False-szla ha nem.
    pass

# Ide ird a kodot, ami beolvas harom vesszovel elvalasztott szamot, majd a fenti fuggveny segitsegevel kiirja, hogy "Pithagoraszi szamharmasok" vagy "Nem pithahoraszi szamharmasok".
```

## Kódjavítás (6p)

Az alábbi program szóközökkel elválasztott szavakat kér be, majd elkezdi őket kiírni, de csak azokat, amik az összes előzőnél hosszabbak. Tehát `a b abc bc vb qwert`-re a kimenetben csak `a`, `abc` és `qwert` szerepel. Viszont több helyen hibás a program, ezeket a hibákat kell kijavítani. Pythontutort lehet (és érdemes) használni.


```python
words_with_spaces = input()
words = words_with_commas.split(' ')

longest = 0
for word in words:
    if word > len(longest):
        print(word)
        longest = len(word)
```

