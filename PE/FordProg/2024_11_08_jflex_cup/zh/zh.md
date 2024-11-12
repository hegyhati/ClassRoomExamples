# Fordítóprogramok ZH 
2024.11.08.

# Elméleti igaz-hamis

 - Az egyik leggyakoribb IR fordítóprogramok esetében a DFA.
 - A kódoptimalizálás jelentős része a fordítóprogram baclendjén történik.
 - A symbol table feladata a nem ASCII karakterek tárolása.
 - Az LL(1) parserek szűkebb nyelvosztályt képesek elfogadni, mint a LALR társaik.
 - Amennyiben egy nyelvtan tartalmaz jobbrekurziót, a hozzá tartozó LR(0) parserben garantált a shift-shift conflict.

# SLR parser generálás és végrehajtás

Készítsen SLR parsert a következő nyelvtanhoz, majd olvassa be vele a megadott bemenetet.

```bnf

dockerfile ::= source build_instructions command

source ::= FROM image

image ::= IMAGENAME ":" VERSION

build_instructions ::= instruction build_instructions | ;

instruction ::= RUN COMMAND | LABEL STRING | ADD PATH PATH

command ::= COMMAND

```
Bemenet :

```docker
FROM ubuntu:latest

RUN apt install openjdk-jre
ADD LilyPond.class LilyPond.class

CMD java LilyPond
```


