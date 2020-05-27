# Grammar

```bnf

print : '{' '{' value filters '}' '}' ;

value : VARIABLENAME
      | LITERAL
      ;

filters : filter filters
        | /* empty */
        ;

filter : '|' FILTERNAME
       | '|' FILTERNAME ':' arguments
       ;
  
arguments : value 
          | value ',' arguments 
          ;



```

# Input

```liquid 
{{ message | toUppercase | append: "!!!" }}
```

```
{ { VARIABLENAME | FILTERNAME | FILTERNAME : LITERAL } }
```
