# Dolgozat 3 - B csoport
2022.03.22.

A dolgozat első feladata papíros, erre 5-10 perc áll rendelkezésre. A programozós feladatokra így 35-40 perc marad.

## Mit ír ki az alábbi program? (5p)
```python
def foo(a,b=1):
    for _ in range(b):
        print(a)

for x in [1,4,5,2]:
    foo(x,1+x)
```

## Programozás (8p)

Írj programot, mely egyetlen bekéréssel beolvas néhány vesszővel elválasztott egész számot, majd kiírja, hogy párosból vagy páratlanból volt-e több. Feltételezhető, hogy legalább egy szám meg lett adva. A program használja rendeltetésszerűen a kért függvényt.

```python
def paros_darab(szamlista):
    # ide ird a kodot, ami szamok egy listajat varja, es visszaadja, hogy hany paros szam van benne.
    pass

# Ide ird a kodot, ami beolvassa a vesszovel elvalasztott szamokat, majd kiirja, hogy "Parosbol van tobb" vagy "Paratlanbol van tobb" vagy "Ugyanannyi paros es paratlan van"
```

## Kódjavítás (6p)

Az alábbi program szóközökkel elválasztott szavakat kér be, majd elkezdi őket kiírni, de csak azokat, amik az összes előzőnél rövidebbek. Tehát `qwer ppppp wer a bb`-re a kimenetben csak `qwer`, `wer` és `a` szerepel. Viszont több helyen hibás a program, ezeket a hibákat kell kijavítani. Pythontutort lehet (és érdemes) használni.


```python
words_with_spaces = print()
words = words_with_spaces.split(',')

longest = 0
for word in words:
    if word < longest:
        print(words)
        longest = len(word)
```

