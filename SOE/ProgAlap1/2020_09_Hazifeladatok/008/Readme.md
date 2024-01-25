A félév elejei "teremből kimenős" példához hasonló feladatot kell leprogramoznunk: Van egy robotunk, mely kezdetben a koordináta rendszer `(0,0)` pontjában áll, és "észak" fele néz. (y tengely irányába).

Ezek után a következő parancsokat kaphatja: `forward`, `left`, `right`, `backward`, melyek után bekér egy további számot (nem feltétlenül egészet), ami megmondja, hogy előre, hátra, balra, jobbra, mennyit menjen a robot. 

A működés akkor ér véget, amikor a fenti irányok helyett egy `stop` parancs érkezik.

A működés végén jelenjen meg a kimeneten három szám: az x koordináta, az y koordináta, és az origótól való távolság. Mindegyik legfeljebb 2 tizedesjegy pontossággal.

Példa bemenet:
```
forward
2
left
4
forward
1
stop
```

Amire a helyes kimenet:
```
-4.0
3.0
5.0
```

Feltételezhetjük, hogy nem érkezik rossz parancs, és a kapott számok pozitívak. 
A kerekítéshez a [`round`](https://docs.python.org/3/library/functions.html#round) függvényt használjuk.


Egy másik minta bemenet:
```
forward
123.321
right
12
left
23.4
backward
23
right
34
stop
```

És a hozzá tartozó kimenet:

```
22.6
100.32
102.84
```
