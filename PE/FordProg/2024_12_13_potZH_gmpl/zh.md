# Fordítóprogramok pótZH 
2024.12.13.


# SLR parser generálás és végrehajtás

Készítsen SLR parsert a következő nyelvtanhoz, majd olvassa be vele a megadott bemenetet.

```bnf

model ::= declaration model | constraint model | objective;

objective ::= KEYWORD STRINGLITERAL ":" linear_expression ";" ;

declaration ::= KEYWORD STRINGLITERAL ";" ;

constraint ::= KEYWORD STRINGLITERAL ":" linear_expression RELATION NUMERICLITERAL ";" ;

linear_expression ::= 
    NUMERICLITERAL "*" STRINGLITERAL + linear_expression  |
    NUMERICLITERAL "*" STRINGLITERAL ;

```
Bemenet :

```docker

var kisfroccs;
var hazmester;

s.t. Szoda: 1 * kisfroccs + 2 * hazmester <= 10;
s.t. Bor:   1 * kisfroccs + 3 * hazmester <= 12;

maximize Bevetel: 200 * kisfroccs + 550 * hazmester ;
```

Megj.: A keywordok a `var`, `s.t.`, `maximize`, a többi értelemszerűen. 

