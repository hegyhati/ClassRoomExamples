# Scope, és ami a memóriában történik.

Egy ideig elprogramozgathatunk úgy, hogy "nem nézünk be a motorháztető alá", azonban öszetettebb programok megírásánál könnyedén belefuthatunk olyan szituációkba, ahol a progam nem úgy működik, mint ahogy gondoltuk volna.
Ilyenkor a python (vagy tetszőleges másik programnyelv) működésének mélyebb megismerése gyakran segít választ adni.

## Látom, nem látom

Vegyük az alábbi egyszerű kódot:

```python
a=1
b=2

def fuggveny():
    b=22
    c=33
    print("Fuggveny a: ", a)
    print("Fuggveny b: ", b)
    print("Fuggveny c: ", c)


fuggveny()
print("Forporgam a: ", a)
print("Foprogram b: ", b)
print("Foprogram c: ", c)
```

Meg tudjuk-e előre mondani, mit fog kiírni? 

Abban valószínűleg egész biztosak vagyunk, hogy az elején `Fuggveny a: 1`, `Fuggveny b: 22`, `Fuggveny c: 33` jelenik meg, valamint `Foprogram a: 1`, de utána? `Foprogram b: 2` vagy `Foprogram b: 22`?

Ha megpróbáljuk futtatni ezt a kódot, az alábbi hibát kapjuk:

```
Traceback (most recent call last):
  File "scope.py", line 15, in <module>
    print("Foprogram c: ", c)
NameError: name 'c' is not defined
```

Ebből látszódik, hogy a `c` változó, amit a függvényben használtunk, az csak a függvényen belül létezik, látható, "kívülről" nem. 
Ez lehetne egy másik függvény is akár.
Módosítsuk picit ezt a sort, és futtassuk újra. Az eredmény:

```
Fuggveny a:  1
Fuggveny b:  22
Fuggveny c:  33
Forporgam a:  1
Foprogram b:  2
Foprogram c:  nem lathato
```

Ebből a kimenetből pár további konklúziót vonhatunk le:
 - Ha a "főprogramunkban" van egy változó, a függvényünkben nincs, akkor a függvényen belül azt elérjük, ki tudjuk iratni.
 - Ha értéket adunk egy olyan nevű változónak, amilyen nevű "kint" is szerepel, akkor az egy **új**, saját, "belső" változó lesz (`b=33`), ami semmilyen hatással nincs a "külső"-re. Hiszen a függvény lefutása után a főprogramban továbbra is 2 a `b` értéke.

 Hogy egy változó hol látszódik, azt a változó **scope**-jának hívjuk. 
 Bármilyen programozási nyelvet is tanulunk, a későbbi hibák elkerülése végett fontos átlátni, hogy az adott nyelven ez hogy működik. 
 A fő "ökölszabály" a legtöbb nyelvre érvényes: Ha egy változót létrehozunk, akkor az az adott blokkkon belül látható. Ha a blokkon belül van egy másik blokk, ott is látható lesz. (Ilyenel mi még csak úgy találkoztunk, hogy főprogramon belül függvény, de lesznek majd összetettebb esetek is.) Viszont ha egy belső blokkban ugyanezzel a névvel beállítunk egy másik változót, akkor az elfedi az ugyanolyan nevű, külső blokkban lévőt.

 Összetettebb példáknál vannak bonyolító tényezők, de nekünk erre a félévre ennyit elég tudni. Még egy általános irányelv, hogy függvényből "főprogrambeli", ún. *globális* változót csak akkor érjünk el, ha feltétlenül indokolt. Törekedjünk inkább arra, hogy a függvénynek amilyen értékekre szüksége van, azt kapja meg argumentumként, amit pedig kifele szeretne változást, azt visszatérési értékként adja vissza.

 Node erről enyi, ugorjunk a következő fejvakarós dologra:


## Másolom, nem másolom

Vegyük az alábbi egyszerű függvényt:

```python
def novel(x):
    x=x+1
    print()
```

Mi történik vajon ha az alábbi kódot futtatjuk le?

```python
novel(3)
```

Kiíródik `4`, nem túl meglepő, de mi történik, ha ezt?

```python
y=3
novel(y)
```

Ugyanúgy 4, de mi lesz akkor ha:

```python
y=3
novel(y)
print(y)
```

A `4` megjelenik, amit a `novel` ír ki, de utána `3` vagy `4` jelenik meg? 
Másképp megfogalmazva: az `y` az *ugyanaz* mint a `novel`-ben az `x` vagy nem?
Ha igen, akkor `4`-nek kellene megjelennie, ha nem, és egy *másolat* készül `y`-ról, és az az `x`, akkor `3`-nak.

Ha lefuttatjuk, akkor kiderül, hogy az utóbbi eset áll fenn, legalábbis `3` jelenik meg `y` kiiratásakor. Ez a *másolósdi* logikusnak tűnik, hiszen a `novel` függvénynek nem csak *változót* adhattunk meg, hanem *értéket* is, tehát azt, hogy `3` vagy akár azt, hogy `2*y+1`. Ezek esetében nem működött volna az, hogy *ugyanazt* használja a függvény, mert ezek nem *változók* csak *értékek*. (Akit érdekel mélyebben a téma, keressen rá az *l-value*, *r-value* kifejezésekre, nekünk most ennyi elég.)

Alakul a hipotézisünk, hogy ilyenkor bizony másolat készül, de egy teszt nem teszt, nézzük meg mondjuk stringekre is:

```python
def append(s):
    s=s+" whatever"

mystring="foobar"
append(mystring)
print(mystring)
```
Az eredmény (csak) `foobar`, ami tovább erősíti a hipotézisünket. 
Nézzük meg listákra is:

```python
def modify(l):
    l[1]="modified"

mylist=[1,2,3]
modify(mylist)
print(mylist)
```
És az eredmény `[1,"modified",3]`... Nem az, amire számítottunk. Akkor az "egyszerű" dolgok lemásolódnak, a lista pedig nem? Nem ez a helyzet, maga a string sem egy egyszerű dolog, sőt. 

Mielőtt mélyebben megértenénk, miről van szó, emlékezzünk vissza, hogy listákkal kapcsolatban már egy fura dologba belefutottunk a műltkor:

```python
for l in mylist:
    print(l)
```
szépen kiírta a lista tartalmát, viszont

```python
for l in mylist:
    l=3
```

nem módosította a listát. Akkor azt mondtuk, hogy a módosításhoz egyelőre jegyezzük meg, hogy indexszel kell elérni az elemeket.

# Tartalmazom, nem tartalmazom (csak mutatom)

Python esetében sajnos csak alap feladatok erejéig működik az a megközelítés, hogy a változókat dobozoknak képzeljük el, amik értékeket tartalmaznak, és ha azt egy függvénynek átadom, akkor arról a dobozról egy másolat készül.

Ami **valójában történik**, az az, hogy a változók nem dobozok, amik *tartalmazzák* az értékeket, hanem csak nevek, *kezelők*, *referenciák*, amik **rámutatnak egy dobozra, ahol az érték tárolva van**.
A *doboz* itt nyilván egy memóriaterületet jelent a valóságban. (A változó pedig egy doboz, amiben ennek a memóriacíme van benne, ezt több nyelvben *pointereknek*/*mutatóknak* hívják, és pythonban valójában minden *változónk* az egy *objektummutató*, de ebbe enyire majd csak a következő félévben mászunk bele a python lelki világába.)

[**EZ**](http://pythontutor.com/visualize.html#mode=edit) egy kiváló eszköz arra, hogy vizualizáljuk, mi történik *valójában*. **Erősen ajánlott** mindenkinek eljátszogatni vele, hogy megértse, hogyan működik a dolog.

Amire figyeljünk, az az, hogy a következő beállításokat válasszuk ki:
 - Python 3.6
 - Show all frames (Python)
 - Render all objects on the heap (Python/Java)
 - Draw pointers as arrows 

Szépen lépésről lépésre végig lehet léptetni (és léptessétek is végig), hogy mi történik. Működik pár másik programnyelvvel is. Ha tanultatok másik programnyelvet, érdemes összehasonlítanotok, hogy ott hogy működnek a dolgok, és mik változtak.

# Leírom, nem írom

Bármiféle szöveges, képekkel kiegészített jegyzetnél sokkal jobb, ha tényleg megnézitek a fenti toolt, és interaktív módon végignyomkodjátok. 
De hogy ne legyen teljesen lusta oktató, itt van pár (egyre bonyolultabb) program, amit érdemes végigvinni. 

Javaslom, hogy mindne lépés előtt próbáljátok meg magatok megmondani, mi fog történni következőnek.


```python
x="alma"
y=x
x="korte"
```

```python
x=3
y=x
y+=1
```

```python
def increase(x):
    x+=1

y=1
increase(y)
```

```python
def double(x):
    x=2*x
    return x

y=3
y=double(y)
```

```python
mylist=["a","b","c"]
for item in mylist:
    item="foo"
```

```python
def modify(l):
    l[1]=1
    l.append("end")

mylist=[1,2,3,4,5,6]
modify(mylist)
```

Illetve bármilyen nem túl nagy órai kódot nyugodtan nézzetek végig, ha nem világos.


# Mutálom, nem mutálom

**immutable** vagyis **nem módosítható** típusoknak mondjuk azokat, amiknél nem módosulhat a *doboz tartalma*. Az alap típusok (`int`, `float`, `str`) esetében azt láttuk, hogy a doboz soha nem változik, amikor a változónak *új értéket* adunk, akkor létrejön egy új doboz, amibe beíródik az új érték, és a változó már oda fog mutatni. Az ilyen típusok esetében nem vesszük észre a mülönbséget aközött, hogy dobozok vannak és másolunk, vagy mutatók vannak és nem másolunk, amikor függvényeknek átadjuk őket (lásd fentebb).

A lista viszont **mutable** vagyis **módosítható**, láttuk, ahogy az utolsó példában megváltoztattuk, hogy az `l` kibővült például. Az ilyen típusok esetében vesszük észre a változást a korábbi "dobozos, másolat készül" elképzelésünktől. 

Az eddigi típusok mindegyike **immutable** volt a listát leszámítva, jövő héten mindkét csoport bővül egy elemmel.



