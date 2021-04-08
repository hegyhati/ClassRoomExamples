# Grammar

```
json : object | array | basetype ;

basetype : STRING | INTEGER | FLOAT ;

object : '{' pairs '}'

pairs : /* nothing */
      | STRING ':' json _pairs
      ;

_pairs : /* nothing */
       | ',' STRING ':' json _pairs
       ;

array : '[' ']' 
      | '[' jsons ']'
      ;

jsons : json
      | jsons ',' json
      ;

```

# Input

```json
[ { "name" : "Kakarott", "power level" : {"over" : 9000 } } ]
```

```
[ { STRING : STRING, STRING : {STRING : INTEGER } } ]
```
