# Final version

```python
import regex

re = regex("(a|b)*baba(a|b)*")
re.complile() 

s = input()
print ("Yeppee" if re.accepts(s) else ":'(")
```

Step by step:

```python
re = regex("(a|b)*baba(a|b)*")
```

Instantiates regex objec, parses "regex-tree", builds NFA.

```python
re.complile() 
```
Builds equivalent DFA. (minimizes)

```python
re.accepts(s)
```
Uses NFA or DFA if exists to check if `s` is accepted / matches the regex.

# First step

```python3
from nfa import NFA

m = (NFA("a") | NFA("b")).kleene() + NFA("baba") + (NFA("a") | NFA("b")).kleene()
m.accept(input())
```





