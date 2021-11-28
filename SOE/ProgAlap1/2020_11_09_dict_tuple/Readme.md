# További összetett tároló adattípusok

## Dictionary / szótár

Amikor a listákról tanultunk, volt két rövid rész arról, hogy mikor érdemes listába tenni dolgokat, és mikor nem. Felelevenítve: ha valamiből több van, pl több napra adott, több emberre adott, van valamilyen határozott sorrend értelmezve köztük, stb, akkor lista. Ha pedig összetartozó adatokról van szó, de nem *ugyanolyan* adatok, nincs egyértelmű sorrendjük, akkor nem lista.

A múlt heti zh példánál maradva: egy csomagnál adott az, hogy mennyi az alapdíja, mennyibe kerül egy sms, és hogy mennyibe kerül egy perc. Ez három *számszerű* adat, pl: `1000`, `10`, `15`, de érezzük, hogy nem *ugyanarról* van szó, és a sorrend, amiben most felírtuk őket, elég önkényes. Ha egy listába tenném be ezeket, akkor miért lenne a 0. elem a havidíj, és nem az sms díja? Valahova fel kellene írnom magamnak, hogy mindenhol konzisztensen ilyen sorrendben használjam ezeket, stb.

Itt igazából nem sorrend van, hanem ez három összetartozó adat, amelyik mindegyike egy nagy valaminek (tariacsomag) egy része, amit egy névvel tudunk azonosítani. Pontosan erre valók a dictionary-k, avagy szótrárak. (más nyelveken map, associative array néven is hivatkoznak rájuk.)

A fenti tarifát pl így tudnánk eltárolni:

```python
tarifa={
    "havidij" : 1000,
    "smsdij" : 10,
    "percdij" : 15
}
```

vagy akar csak egy sorban:

```python
tarifa={ "havidij" : 1000, "smsdij" : 10, "percdij" : 15 }
```

Ezek után ezeket az értékeket, adatokat hasonlóan érjük el, mint listánál. De az index itt nem egy sorszám, hanem egy azonosító: `tarifa["havidij"]`, `tarifa["smsdij"]`, `tarifa["percdij"]`.

Ennek a módszernek az előnye ahhoz képest, mintha csak `listatarifa=[1000,10,15]`-öt írtunk volna az, hogy most név alapján tudjuk azonosítani az adatot, ami kényelmesebb, átláthatóbb, és legfőképp ha a programban egy másik függvénynek átadjuk, akkor annak nem kell tudnia, hogy milyen sorrendben írtuk be a dolgokat, csak azt, hogy milyen adattagot szeretne elérni.

És ha már a beírás sorrendjéről beszélünk, ez is ugyanazt eredményezi, mint a fenti:

```python
tarifa={ "smsdij" : 10,  "havidij" : 1000, "percdij" : 15 }
```
Azaz teljesen mindegy a sorrend. Nyugodtan hozzá is tehetünk plusz adatokat, ha fontossá válik, pl:

```python
tarifa={ "nev" : "Westel 0660 - alap", "havidij" : 1000, "smsdij" : 10, "percdij" : 15 }
```

Az azonosítót, ami az index itteni megfelelője **kulcsnak (key)** hívjuk általában. 

Azt már láttuk, hogy egy adott kulcshoz tartozó adatot hogyan érünk el, ugyanúgy, mint egy listánál az intexekkel. 

Plusz adattaggal való bővítés egyszerű:
```python
tarifa["elofizeteses"]=True
tarifa["husegido"]=12
```

Kitörölni egy kulcshoz tartozó értéket a `pop` függvénnyel tudunk:
```python
tarifa.pop("elofizeteses")
```

Leellenőrizni, hogy egy kulcs szerepel-e az `in` kulcsszóval tudjuk:
```python
if("husegido" in tarifa):
    print("Szukseges ",tarifa["husegido"],"honapnyi huseg.")
else:
    print("Nem kell husegnyilatkozat.")
```

Egy üres szótárat `{}`-vel tudunk létrehozni.

Egy apró záró megjegyzés szótárakhoz: az eddigi példákban a kulcs mindig string volt, de lehetett volna egész/lebegőpontos szám is, lisa viszont nem.

```python
mydict={}
mydict["string1"]="another string"  # OK
mydict["string2"]=[1,2,3]           # OK 
mydict[3]="another string"          # OK
mydict[[1,2]]=1                     # NOT OK
mydict[1.2]={"string":1}            # OK
mydict[{"string":1}]=1              # NOT OK
```
Röviden: érték lehet bármi, kulcs nem lehet lista és másik szótár. Egyelőre úgy tűnik, hogy egyszerű dolgok lehetnek kulcsok, érték pedig bármi. A helyzet valójában kicsit más: érték bármi lehet, kulcs viszont csak immutable dolog.

## Set / halmaz

Néha előfordul, hogy nem sorbarendezett adataink vannak, de nincsenek is kulcs-érték párok, csupán kulcsok vannak, amik *maguk* az értékek. Ilyen például, hogy melyik tárgyakat vettem fel, vagy melyik kocsmákat látogattam már meg Sopronban. Ezekre nincs egyértelmű sorrend, vagy nem fontos. Kocsmáknál lehetne az első meglátogatás sorrendje, de lehetne az is, hogy mikor voltam ott utoljára. De ha ez a feladat szempontjából lényegtelen, akkor jó volna, ha nem lenne jelentősége annak, milyen sorrendben írom be őket, ahogy a dictionary esetében sem volt a kulcsoknak.

Erre való a set, halmaz:

```python

myset={1,2,3}
```

Ez egy olyan adateggyüttes, amiben benne van 3 adat, de nem tudjuk index alapján lekérdezni, hogy melyik az első, mert nincs sorrend. Az `in`,  `len` és `pop` ugyanúgy működnek, hozzáadni pedig `myset.add(4)` módon lehet.

Üres set-et nem `{}`-vel hanem `set()`-tel tudunk létrehozni, elkerülve az ütközést az üres dictoinary-vel.

A set ugyanúgy mutable, így szintén nem lehet kulcs dictoinary-ben.


## Tuple / rendezett n-es

Használtuk már a szögletes zárójeleket, kapcsos zárójeleket, csak a sima zárójelet nem.

De ha beírjuk ezt:

```python
t=(1,2,3)
```

vagy ezt:
```python
t=(1,"two",3.0,[4,4.0],{'fifth':5})
```

akkor látjuk, hogy mindkettőt elfogadja a python. 
Hasonlít a dolog nagyon a listákhoz. [Pythontutoron](http://pythontutor.com/live.html#code=t%3D%281,%22two%22,3.0,%5B4,4.0%5D,%7B'fifth'%3A5%7D%29&cumulative=true&curInstr=1&heapPrimitives=true&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) is eléggé hasonlóan néz ki, mint a lista. 

Ami különbséget itt látunk, hogy a 3. indexen mutatott listánál a sárga doboz mellett `tuple` szerepel, nem `list`, és hogy a sárga doboz a lista esetében jobbról és fentről nem rendelkezik kerettel. 

Ez már sejteti, mi lesz a különbség a kettő között. Ha megpróbáljuk a lista szokásos műveleteit végrehajtani, akkor a következőket fogjuk tapasztalni:

```python
mytuple=(1,2,3,4)

for t in mytuple:               # OK
    print(t)                    # OK

for t in range(len(mytuple))    # OK
    print(mytuple[t])           # OK

mytuple[1]=2                    # NOT OK
mytuple.append(3)               # NOT OK
mytuple.pop(0)                  # NOT OK
```

Amit észrevehetünk, az az, hogy minden működik, ami csak *olvasni* szeretne, de változtatni az adatokat nem tudjuk. És ezzel meg is fogalmaztuk, hogy mi az a tuple: egy olyan lista, amit nem lehet módosítani. Kicsit pontosabban: nem változhat a mérete, és az sem, hogy az elemei hova mutatnak. (Ha az, ahova mutatnak egy módosítható valami, akkor az módosulhat. Tehát a fenti második példánál a `t[3].append("four")` például teljesen megengedett, mert a tuple maga nem változik.)

Mikor jobb egy tuple mint egy lista? Egyelőre úgy tűnik, hogy a lista mindent tud, amit a tuple, and more.
 -  Ha tudjuk, hogy valami olyanról van szó, amiról még *véletlenül* sem akarjuk, hogy módosuljon, akkor érdemesebb tuple-t használni. Ha valamilyen hibából valamelyik kódrészünk mégis módosítaná, hibát kapunk, amit már akár egy linter, fejlesztőkörnyezet is jelezhet. Ha listát használnánk, akkor futna tovább a program hibás adatokkal.
 - Mivel a tuple immutable, használható például dictionary kulcsaként, lista nem.
 - Ha egy függvénytből több adatot szeretnénk visszaadni, az több nyelv esetében tud macerás lenni, külön körítés kell hozzá. Python esetében ez egyszerű:

```python
def min_max(a,b):
    if a<b: return (a,b)
    else: return (b,a)

a=int(input())
b=int(input())
(smaller,larger)=min_max(a,b)

...
```
A fenti működik a zárójelek explicit kiírása nélül is:
```python
def min_max(a,b):
    if a<b: return a,b
    else: return b,a

a=int(input())
b=int(input())
smaller,larger=min_max(a,b)

...
```

Érdemes ezt is [Pythontutoron](http://pythontutor.com/live.html#code=def%20min_max%28a,b%29%3A%0A%20%20%20%20if%20a%3Cb%3A%20return%20a,b%0A%20%20%20%20else%3A%20return%20b,a%0A%0Aa%3Dint%28input%28%29%29%0Ab%3Dint%28input%28%29%29%0Asmaller,larger%3Dmin_max%28a,b%29&cumulative=true&curInstr=8&heapPrimitives=true&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%225%22,%221%22%5D&textReferences=false) végignyomkodni. 


## ypes, types everywhere

Az előzőek után kisebb káosz alakulhat ki, hogy itt van rengeteg tool, mikor, melyikhez érdemes nyúlni. Az alábbi rövid program általában segít ennek eldöntésében:

```python

valasz=input("Az adatod egyszerű, egy darab adat?")
if valasz=="igen":
    print("Használj egyszerű változót (int,float,str,bool).")
else:
    valasz=input("Az adataid (legnagyobb blokkjai) sorbarendezhetők, és ez a sorrend fontos?")
    if valasz=="igen":
        valasz=input("A darabszáma vagy értéke ezeknek az adatoknak szabad, hogy módosuljon?")
        if valasz=="igen" 
            print("Használj listát.")
        else:
            print("Használj tuple-t.")
    else:
        valasz=input("Ezek a nem sorbarendezhető adatok külön kulcsokkal azonosíthatók?")
        if valasz=="igen":
            print("Használj dictionary-t.")
        else:
            print("Használj set-et.")
```

Érdemes megnézni a vizualizációkat is [Pythontutoron](http://pythontutor.com/live.html#code=my_int%3D1%0Amy_float%3D2.3%0Amy_string%3D%22You%20know%20the%20rules%20and%20so%20do%20I%22%0Amy_bool%20%3D%20False%0A%0Amy_list%20%3D%20%5B%22Never%22,%22gonna%22,%22give%22,%22you%22,%22up%22%5D%0Amy_tuple%3D%20%28%22Never%22,%22gonna%22,%22let%22,%22you%22,%22down%22%29%0Amy_set%20%3D%20%7B%22Never%22,%22gonna%22,%22run%22,%22around%22,%22and%22,%22desert%22,%22you%22%7D%0Amy_dictionary%3D%7B%22You%20have%20been%20rickrolled%22%3ATrue%7D%0A%0A&cumulative=true&curInstr=8&heapPrimitives=true&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).

