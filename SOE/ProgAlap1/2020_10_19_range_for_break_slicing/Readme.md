# Listák egyszerűbb bejárása

Amikor egy listába beolvastunk értékeket, azt így tettük:
```python
idx=0
while idx < len(list):
    list[idx]=int(input())
    idx+=1
```
Amikor kiírtuk az elemeit egysével:
```python
idx=0
while idx < len(list):
    print(list[idx])
    idx+=1
```
Amikor csak minden pozitívot:
```python
idx=0
while idx < len(list):
    if(list[idx]>0):
        print(list[idx])
    idx+=1
```
A sort még folytathatnánk, de a következő minta látjuk, hogy gyakran előfordul:
```python
idx=0
while idx < len(list):
    # Do something, probably with list[idx]
    idx+=1
```
Az ilyen "menjünk végig a lista elemein egyesével sorban" típusú ciklusokhoz a nyelv támogat egy kompaktabb formát:
```python
for idx in range(len(list))
    # Do something, probably with list[idx]
```
A `range(n)` pontosabb működését csak később fogjuk megérteni, egyelőre képzeljük úgy el, mintha adna nekünk egy listát, amiben `0`-tól vannak a számok `n`-ig. Python 2-ben még így is működött, azonban a 3-as változatban már egy memóriahatékonyabb módon van ez megoldva.

Ez azonban több módon is paraméterezhető:
 - `range(n)` : `0`, `1`, `2`, ... , `n-1`
 - `range(k,n)` : `k`, `k+1`, `k+2`, ... , `n-1`
 - `range(k,n,i)` : `k`, `k+i`, `k+2*i`, ... , amíg `n` alatti a szám

Használva ezt, ennyi kiírni egy list pozitív elemeit:

```python
for idx in range(len(list)):
    if(list[idx]>0):
        print(list[idx])
```

Azonban ahogy az `idx` végigmegy a `range(n)` által "generált" listán, úgy akár el lehet érni a lista elemeit direktben is egy `for` ciklussal:

```python
for element in list:
    if(element>0):
        print(element)
```
A következő azonban nem a várt eredményt fogja adni:
```python
list=[1,2,3]
for element in list:
    element*=2
print(list)
```
A kimenet nem `[2,4,6]` hanem `[1,2,3]` lesz. Hogy ez miért van pontosan így, azt pár hét múlva részletesen megvizsgáljuk, addig kövessük azt az ökölszabályt, hogy ha csak olvasni szeretnénk a listát, akkor jó a fenti bejárás, ha felülírni is szeretnénk az elemeket, akkor használjunk továbbra is indexelt változatot.

# List slicing, lista másolás

A `[]` operátorral nemcsak egy adott eleme érhető el a listának, hanem a lista részeiről is készíthetünk. 
A következő jelölések mind egy **új** listát adnak vissza:
 - `list[start:]` a `start`-odik elemtől kezdve a lista végéig
 - `list[:stop]` a lista elejétől `stop`-odik előtti elemig
 - `list[start:stop]` a `start`-odiktól a `stop`-odik előtti elemig  

A `range()`-hez hasonlóan itt is meg lehet adni "lépésszámot": `list[3:100:2]` egy olyan listát ad vissza, amiben a 3., 5., 7., ... , 99. eleme van benne a listának.

Mindegyik rész (`start`,`stop`,`step`) opcionális, tehát `[::3]` például minden 3. elemet válogatja ki a teljes listából. A minimális eset a `[:]`, mely a teljes listáról készít másolatot. 

Felvetődhet a kérdés, hogy miért nem csak egyenlővé teszünk egy listát egy másikkal?
```python
list=[1,2,3]
list2=list
list3=list[:]
print(list)
print(list2)
print(list3)
```
Mind a 3 kiiratás esetében `[1,2,3]` jelenik meg, feleslegesnek tűnik a `[:]` a harmadik lista esetében. Azonban a következő kód rámutat a különbségre:
```python
list=[1,2,3]
list2=list
list3=list[:]
list[0]=11
list2[1]=22
list3[2]=33
print(list)
print(list2)
print(list3)
```
A kimenet ez esetben a következő lesz:
```
[11,22,3]
[11,22,3]
[1,2,33]
```
Ebből látszik, hogy `list` és `list2` ugyanazt a listát módosítják, `list3` viszont egy másolaton dolgozik. Az e mögött rejlő okokra pár hét múlva térünk vissza, addig jegyezzük meg, hogy ha le szeretnénk másolni a listát, akkor kell a `[:]`, különben nem.


# Típusok
A Python alapértelmezett típust támogat, ezek kösül náhánnyal találkoztunk már.

## Egész szám, `int`

Tetszőlegesen nagy méretű számot képes tárolni. (Python 2-ben erre volt a `long` típus, ott az `int`-nek volt maximális mérete.) Értelmezettek rá az alapvető matematikai operátorok, ezeket használtuk már: `-x`,`x+y`,`x-y`,`x*y`,`x//y`,`x**y`.

Vannak olyan műveletek, amik alkalmazása során az eredmény már a következő, lebegőpontos formában lesz. Ilyen például a sima osztás, `/`, vagy előfordulhat ez hatványozásnál is, pl `2**0.5`. (Negatív számok gyökeinek esetében komplex szám lesz az eredmény.)

## Lebegőpontos szám, `float`

Numerikus típus, mely nem csak egész számok tárolására alkalmas. Numerikus kerekítési hibák a számábrázolás módjából fakadóan előfordulhatnak. A szokásos algebrai műveletek mind alkalmazhatók rá. 
`12.0` egyenlő `12`-vel, de ha az egészrészét egy lebegőpontos számnak egész változó formájában szeretnénk megkapni, akkor az `int(float_variable)` konverzióval lehetséges.

## Karaktersorozat, `str`

Karakter sorozat literálokkal már korábban is találkoztunk, mint `"text"` vagy `'text'`. Változóknak is lehet ilyen típusú értéke. Az ilyen típusú változókra több operátor értelmezett, egy gyakran használt a `string1 + string2`, mely összefűz két karaktersorozatot.

Szöveghez `int` vagy `float` típusú változó nem fűzhető hozzá, azt előbb szöveggé kell alakítani, pl:
```python
for i in range(4):
    print("This is the " + str(i+1) + "th print statement")
```

Ha a `string` nevű változónk szövegként tartalmaz egy számot, akkor annak a numerikus értéke `int(string)` vagy `float(string)` módon nyerhető ki. 

A szöveg típusú változókra sok szempontból tekinthetünk úgy, mint karakterek listájára. Ugyanúgy használható a `len` vagy az indexelés, vagy a fenti slicing technika. `"Abrakadabra"[1:8:2]` eredménye `baaa`.

## Logikai érték, `bool`

Logikai típusú változók két értéket vehetnek fel: `True` és `False`. Erre értelmezettek a `not`, `and`, `or`, stb. logikai műveletek. 

Más típusú változók logikai kiértékeléséhez adottak szabályok, azonban kerüljük az ilyen szituációkat. 

## További típusok
Komplex számokról, rendezett n-esekről, szótárakról kesőbb fogunk részletesen beszélni.

# `break` és `continue`

Ciklusmagban (mindegy, hogy `for` vagy `while`) a `break` és  `continue` a következő szabályok szerint módosítják az utasítások végrehajtási sorrendjét:

```python
instructions before the loop
while condition:
    some instructions
    break / continue
    other instructions
    # continue would jump here
#break would jump here
instructions after the loop
```

A `break` hatására tehát az interpreter "kiugrik" a ciklusból, és a következő utasítás végrehajtásával folytat. 
A `continue` hatására csak a ciklusmag legvégére ugrik a vezérlés, amit a ciklusban maradási feltétel kiértékelése követ. 

Ilyen formában ezeknek sok értelme nincs, az `other instructions` rész sosem hajtódik végre, `break` esetében pedig a `while` is egy `if`-re degradálódik, hiszen rögtön az első iterációban már kiugrunk a ciklusból. A `break` és  `continue` ezért tipikusan valamilyen feltétel mellett szokott megjelenni, valahogy így:

```python
while condition:
    some instructions
    if (some error happens):
        handle the error
        break
    other instructions when no error occurs
```

Ökölszabálynak egyelőre azt írjuk fel magunknak, hogy ezt a két eszközt csak csínján használjuk, akkor, amikor tényleg így lesz szebb, átláthatóbb a kód. Kerüljük a túlzott használatujkat, az pont ennek az ellenkezőjét éri el.

Amennyiben több ciklus van egymásba ágyazva, ezek az ugrások mindig csak a legbelső ciklusra vonatkoznak, tehát:

```python
while some condition:
    instructions
    while other condition:
        instructions
        if yet another condition:
            instructions
            break / continue
        instructions
        # continue jumps here
    # break jumps here
    instructions
    # continue does NOT jump here
# break does NOT jump here
instructions
```

## Hátultesztelő ciklus - variációk egy témára

A Python nyelvi szinten nem támogat hátultesztelő ciklusokat a legtöbb programozási nyelvvel ellentétben. Hátultesztelő ciklusok a "csinálj valamit, aztán amíg egy feltétel teljesül, csináld újra" szituációkban hasznosak. 

Egy ilyen korábbi példa volt a "Kérjünk be számokat addig, amíg 0-t nem kapunk." Átfogalmazva: "Kérjünk be egy számot, majd kérjünk addig újra, amíg nem 0."

Ezt két módon is megoldottuk:

```python
x=1
while x!=0:
    x=int(input())
```
illetve:
```python
x=int(input())
while x!=0:
    x=int(input())
```

Mindkét megvalósításnak megvan a maga csúnyasága. Első esetben az `x` 1-re állítása hack. Ha később pont az 1-el való ellenőrzést szeretnénk nézni, akkor figyelni kell, hogy állítsuk át. Illetve bonyolultabb feltétel esetén nem feltétlen ilyen triviális kierőszakolni hogy mindenképpen menjen bele először a ciklusba a végrehajtás.

A második megoldás csúnyasága, hogy kétszer megjelenik ugyanaz a kód. Ez egy bekérésnél még nem vészes, de ha a ciklusmagban 10 utasitás van elágazásokkal, akkor csúnyán redundánssá válik a kód.

Logikai változó bevezetésével is megoldható a várt működés:

```python
first=True
while first or x!=0:
    first=False;
    x=int(input())
```

Ebben az esetben plusz egy változót be kellett vezetnünk, de legalább átlátható és nincs kódismétlés.

Egy utolsó megoldás a `break`-re épül:

```python
while True:
    x=int(input())
    if x==0: break
```






