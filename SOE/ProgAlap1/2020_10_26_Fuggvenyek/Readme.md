# Függvények

## Előszó

Aki már programozott más nyelven, valószínűleg ismeri a függvények fogalmát. 
Itt is találkoztunk már pár függvénnyel, pl `len`, `range` vagy `int`. De az I/O műveleteink (`input`, `print`) is függvények voltak.

Most csak a függvények alapjait tanuljuk meg, nagyobb hangsúlyt fektetve arra, miért, és mit szervezzünk ki függvényekbe, mint arra, hogy milyen lehetőségek vannak (név túlterhelés, név szerinti paraméterátadás, stb.)

## Motivációs példa

A függvények szükségességét, hasznait egy egyszerű példán keresztül nézzük meg: [Pascal háromszög](https://en.wikipedia.org/wiki/Pascal%27s_triangle) kirajzolása megadott mélységig. 
Nem fontos egyelőre a szép rendezés, a kimenettől valami ilyesmi elvárt:

```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
...
```


### Módszer

Természetesen meg lehetne ezt oldani listákkal és az összeadó szabályokkal egyszerűbben (házifeladat), de mi most arra a képletre támaszkodnánk, hogy az <!-- $n$ --> <img src="https://render.githubusercontent.com/render/math?math=n">-edik sor <!-- $k$ --> <img src="https://render.githubusercontent.com/render/math?math=k">-adik eleme <!-- $\binom{n}{k}$ --> <img src="https://render.githubusercontent.com/render/math?math=%5Cbinom%7Bn%7D%7Bk%7D">.

### Lépésről lépésre stratégia

A feladat így elsőre nagy falatnak tűnhet, boncolgassuk ezt a képletet tovább:

<!-- $$
\binom{n}{k}=\frac{n!}{k!\cdot(n-k)!}=\frac{1\cdot 2\cdot \dots \cdot n}{(1\cdot 2\cdot \dots \cdot k)\cdot(1\cdot 2\cdot \dots \cdot (n-k))}
$$ --> 

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Cbinom%7Bn%7D%7Bk%7D%3D%5Cfrac%7Bn!%7D%7Bk!%5Ccdot(n-k)!%7D%3D%5Cfrac%7B1%5Ccdot%202%5Ccdot%20%5Cdots%20%5Ccdot%20n%7D%7B(1%5Ccdot%202%5Ccdot%20%5Cdots%20%5Ccdot%20k)%5Ccdot(1%5Ccdot%202%5Ccdot%20%5Cdots%20%5Ccdot%20(n-k))%7D"></div>

Ha valami elsőre túl bonyolultnak tűnik, általában jó stratégia megpróbálni valami egyszerűsített változatot, vagy csak részfeladatot megcsámcsogni először, majd ha az megvan, ennek megfelelően epíteni a kódunkat.

Egy viszonlag jó tervnek tűnik a következő:
1. először csak kérjünk be egy számot, és számoljuk ki a faktoriálisát
2. ha ez megvan, ezt felhasználva írjunk programot, ahol bekérünk két számot, és kiírjuk a binomiális együtthatót
3. ha ez megvan, írjuk ki a Pascal háromszög első néhány sorát

### 1. lépés: faktoriális számítás

Ezt már az eddigiek alapján meg kell tudnunk oldani:

```python
szam=int(input())
faktorialis=1
for szorzo in range(1,n):
    faktorialis*=szorzo
print(faktorialis)
```
### 2. lépés: binomiális együttható számítás

A binomiális együtthatót 3 faktoriális összeszorozgatásával, osztásával kapjuk meg, ez egyszerű szekvencia, a kód nagy vonalakban valahogy így nézhetne ki:

```python
n=int(input())
k=int(input())

n_faktor kiszamitasa
k_faktor kiszamitasa
n_minusz_k_faktor kiszamitasa

n_alatta_k = n_faktor // (k_faktor * n_minusz_k_faktor)

print(n_alatta_k)
```
 
A faktoriálisok kiszámításához van már kódunk, hát használjuk:

```python
n=int(input())
k=int(input())

n_faktor=1
for szorzo in range(1,n):
    n_faktor*=szorzo

k_faktor=1
for szorzo in range(1,k):
    k_faktor*=szorzo

n_minusz_k_faktor=1
for szorzo in range(1,n-k):
    n_minusz_k_faktpor*=szorzo

n_alatta_k = n_faktor // (k_faktor * n_minusz_k_faktor)

print(n_alatta_k)
```

Nem kellett igazából mást csinálni, csak 3 "példányban" bemásolni a fenti kódot, figyelve arra, hogy a `range` megfelelően módosítva legyen, illetve a `faktorialis` változót átírni. De ha picit lustábbak vagyunk, akár ezt is csinálhattuk volna:


```python
n=int(input())
k=int(input())


faktorialis=1
for szorzo in range(1,n):
    faktorialis*=szorzo
n_faktor=faktorialis

faktorialis=1
for szorzo in range(1,k):
    faktorialis*=szorzo
k_faktor=faktorialis


faktorialis=1
for szorzo in range(1,n-k):
    faktorialis*=szorzo
n_minusz_k_faktor=faktorialis

n_alatta_k = n_faktor // (k_faktor * n_minusz_k_faktor)

print(n_alatta_k)
```

Maradjunk ennél az utóbbi változatnál, és akkor már folytathatjuk is a következő lépéssel.

### 3. lépés: Pascal háromszög kiiratása

Nem kell mást tennünk, mint két egymásba ágyazott ciklusba bepakolni a fentit, és a kiiratásokat a mefelelő helyre tenni:

```python
sorszam=int(input())

for n in range(sorszam):
    for k in range(n+1):

        faktorialis=1
        for szorzo in range(1,n):
            faktorialis*=szorzo
        n_faktor=faktorialis

        faktorialis=1
        for szorzo in range(1,k):
            faktorialis*=szorzo
        k_faktor=faktorialis


        faktorialis=1
        for szorzo in range(1,n-k):
            faktorialis*=szorzo
        n_minusz_k_faktor=faktorialis

        n_alatta_k = n_faktor // (k_faktor * n_minusz_k_faktor)

        print(n_alatta_k, end=' ')
    
    print()
```

A `print`-nél lévő `, end=' '` abban segít nekünk, hogy ne legyen automatikus sortörés egy együttható kiiratása után, csak egy szóköz. 
Hogy ez hogyan működik, majd kesőbb megnézzük, egyelőre csak jegyezzük meg, hogy így tudjuk ezt elérni.

## Szörnyülködés a teremtményünkön

Nem kell különösebben sok szépérzék hozzá, hogy a fenti, kódnak nevezett torzszülött valamire ránézve zavart érezzünk az erőben. 
Szedjük sorba, mi nem tetszik benne, és ez miért baj.

### Hosszú...

Bármennyire is gyerekes problémának tűnik ez, hiszen egy komoly szoftver forrása sok nagyságrenddel nagyobb, teljesen jogos sérelem ez. 
Abszolút értékben ez a kód nyilván nem hosszú, de *hosszabb a kelleténél*, ami több okból baj:
 - Nekünk, fejlesztőknek tovább tart elolvasni, átnézni, stb. Ez idő, mentális energia, az alkalmazói oldalon pedig súlyos költség.
 - Kevesebb lényeges dolog fér ki egy képernyőre, ami rátesz egy lapáttal az előzőre.
 - Vannak olyan helyzetek, amikor a gépeknek is fontos a kódméret, lásd pl frontend fejlesztés, compile-olt nyelvek build ideje, embedded rendszerek, stb.
  - A kódot valakinek át kell nézni, jóvá kell hagynia. Ez annak a valakinek is nehezebb, ha hosszabb, nehéz részekre bontani, egyben sokat kell átlátni.
  - 2 hónap múlva már mi is elfelejtjük a kód részleteit, ugyanúgy sok munka lesz átnézni, mint az előző pontban írva volt.

 ### Redundáns

 Ökölszabály az informatikában, hogy ha ismétlést látunk, az egy jele annak, hogy ezt valahogy szebben, jobban is lehetne csinálni. Miért is baj a ismétlés, redundancia?
  - Kódhosszt növel, ezt már kitárgyaltuk.
  - Unalmas dolog ugyanazt csinálni újra meg újra. Ha valami unalmas, nem figyelünk. Ha nem figyelünk, hibázunk.
  - Ha nem másolás közben hibáztunk, hanem kiderül, hogy már a másolandó kódban hiba volt, akkor azt sok helyen kell javítani. Ezek a javítások nem feltétlenül automatizálhatók, ha mindenhol egy picit belepiszkáltunk a kódba. 
  - Ha ilyen hibákat javítunk, akkor mivel ez nem automatikus, nem biztos, hogy mindenhol kijavítjuk ahol kell. 5-ből 4 helyen igen, de egy helyen benne marad. Használjuk tovább a szoftvert, és szépen csendben néha rosszul működik.
  - Nem csak hibás kódhoz nyúl hozzá az ember, hanem rendben működőhöz is, ha ki akarja egészíteni valamilyen új funkcionalitással. Ha ugyanaz a logika 24 helyen szerepel a kódban, akkor mind a 24 helyen át kell írni a kódunkat, hasonlóan a hibajavításhoz.

Általánosságban érdemes egy kódra nem úgy gondolni, mint valami, amit egyszer megcsinálunk, és utána jól működik, hanem mint egy működő rendszerre, amihez folyamarosan hozzányúlunk, javítgatjuk, lecserélünk részeket jobbra, tuningoljuk, új dolgokat teszünk rá, stb.

Ha jobban meglessük a kódunkat, van is benne egy hiba, a faktoriális számításnál a range-et nem jól állítottuk be. Ez a hiba most 3 helyen szerepel így.

## Átírás függvényekre

Mit kezdenénk intuitív módon ezzel a problémával? Az utolsó változatban (szinte) teljesen ugyanaz a 3 sor ismétlődik 3-szor. Ezt a 3 sort kitehetnénk valami megcimkézett helyre, és mindegyik helyen, ahol eddig volt, csak azt írnánk oda, hogy itt most azt a részt kell végrehajtani, aztán folytatni innét. 
Valami ilyesmi lehetne a kódunk:


```python
redundans_kodresz:
    faktorialis=1
    for szorzo in range(1,???):
        faktorialis*=szorzo

---------------------------------------

faktorialis=1
sorszam=int(input())

for n in range(sorszam):
    for k in range(n+1):

        goto redundans_kodresz
        n_faktor=faktorialis

        goto redundans_kodresz
        k_faktor=faktorialis


        goto redundans_kodresz
        n_minusz_k_faktor=faktorialis

        n_alatta_k = n_faktor // (k_faktor * n_minusz_k_faktor)

        print(n_alatta_k, end=' ')
    
    print()
```

Ez persze új problémákat vet fel. A kódrészek nem mindenhol voltak pontosan ugyanazok. Mindegyik másolásnál más volt a `range` felső határa, amit most a `???` jelöl. Valahogy lehetőséget kellene adni arra, hogy ezt a részt minden egyes odaugrásnál meg tudjuk határozni. Valami ilyesmi:

```python
redundans_kodresz:
    faktorialis=1
    for szorzo in range(1,???):
        faktorialis*=szorzo

---------------------------------------

faktorialis=1
sorszam=int(input())

for n in range(sorszam):
    for k in range(n+1):

        goto redundans_kodresz with ???=n
        n_faktor=faktorialis

        goto redundans_kodresz with ???=k
        k_faktor=faktorialis


        goto redundans_kodresz  with ???=n-k
        n_minusz_k_faktor=faktorialis

        n_alatta_k = n_faktor // (k_faktor * n_minusz_k_faktor)

        print(n_alatta_k, end=' ')
    
    print()
```

És ezzel gyakorlatilag felfedeztük magunkak a függvényeket/eljárásokat. 
Pontosan erre a célra, és ezt a működést valósítják meg a függvények a legtöbb programozási nyelven. (Igen, rekurzív hívásoknál ez nem teljesen igaz, de erről majd később.)

A `???`-lel átadott "specifikációt" argumentumnak hívjuk. 
A korrekt Python szintaktikától igazából nem vagyunk messze:
 - a cimke maga a függvény neve, és csak be kell írni, nem kell `goto`
 - a függvény megadásánál viszont kell egy `def` kulcsszó
 - a specifikáláshoz szükséges argumentumokat a függvénynév után kell zárójelek között felsorolni (csináltunk már ilyet, például `print(42)` vagy `len(lista)`, stb.)
 - `???` nem lehet argumentum név, de bármi ami változónév, az igen
 - nem kell a `------`, az indentálás jelzi, hol van vége a függvénynek
 - az argumentum értékét zárójelben adjuk át

Ezek alapján egy már teljesen valid Python kód:


```python
def faktorialis_szamolas (szam):
    faktorialis=1
    for szorzo in range(1,szam):
        faktorialis*=szorzo

faktorialis=1
sorszam=int(input())
for n in range(sorszam):
    for k in range(n+1):
        faktorialis_szamitas(n)
        n_faktor=faktorialis
        faktorialis_szamitas(k)
        k_faktor=faktorialis
        faktorialis_szamitas(n-k)
        n_minusz_k_faktor=faktorialis
        n_alatta_k = n_faktor // (k_faktor * n_minusz_k_faktor)
        print(n_alatta_k, end=' ')    
    print()
```


Már ebben a formában sokkal szebb, kompaktabb, átláthatóbb a kódunk, de azért hagy még kívánnivalót maga után. 
A `faktorialis_szamitas` függvény egyetlen célja, hogy kiszámoljon nekünk egy számot, ami az átadott szám faktoriálisa. Most a "fő" programunkból szólunk neki, hogy dolgozzon, átadunk egy számot. A függvény a `faktorialis` valtozoba beleirja ezt az értéket, amit aztán a fő programunk következő sorában a függvény végrehajtása után eltárolunk egy másik változóban.

Amikor egy függvény nem csak dolgozgatna valamit, hanem vissza is szeretne adni pl egy kiszámolt értéket, arra nyelvi támogatás adott szinte minden programozási nyelven. Pythonban sincs ez másképp, a függvény belsejében, törzsében a `return` utasítás hatására az utána megadott "érték" visszaadásra kerül, amit rögtön egy változóban el is tárolhatunk a meghívott helyen, így:

```python
def faktorialis_szamolas (szam):
    faktorialis=1
    for szorzo in range(1,szam):
        faktorialis*=szorzo
    return faktorialis


sorszam=int(input())
for n in range(sorszam):
    for k in range(n+1):
        n_faktor=faktorialis_szamitas(n)
        k_faktor=faktorialis_szamitas(k)
        n_minusz_k_faktor=faktorialis_szamitas(n-k)
        n_alatta_k = n_faktor // (k_faktor * n_minusz_k_faktor)
        print(n_alatta_k, end=' ')    
    print()
```

Ilyet is csináltunk már korábban, minden `x=input()` bekérésünk valójában egy függvényhívás, ami a háttérben csinálgat valamit a terminálunkban, majd visszaad nekünk egy szöveget, amit beolvasott. Ezt mi ebben a példában át is konvertáljuk egy egész számmá: `sorszam=int(input())`. Itt először az `input` hívódik meg paraméter nélkül, és visszaad egy szöveget. Ezt "rögtön átadjuk" az `int` függvénynek, ami éertelmezi a szöveget, és visszaad nekünk egy számot, amit aztán a `sorszam` változóban eltárolunk.

Node, alakul a dolog, mint Quasimodo a prés alatt. Viszont most azt látjuk, hogy az  `n_faktor`, `k_faktor`, `n_minusz_k_faktor` változókat csak arra használjuk, hogy 1-2 sor erejéig eltáruljanak egy értéket, amit aztán használunk az `n_alatta_k` kiszámításához. 
Jó lenne, ha ezeket is köztes eltárolás nélkül rögtön fel tudnánk használni, ahogy az előbb volt erről szó. Ennek természetesen semmi akadálya:

```python
def faktorialis_szamolas (szam):
    faktorialis=1
    for szorzo in range(1,szam):
        faktorialis*=szorzo
    return faktorialis


sorszam=int(input())
for n in range(sorszam):
    for k in range(n+1):
        n_alatta_k = faktorialis_szamitas(n) // (faktorialis_szamitas(k) * faktorialis_szamitas(n-k))
        print(n_alatta_k, end=' ')    
    print()
```

Sőt, ha nagyon spórolni szeretnénk a kódsorokkal, akkor még a `sorszam` változót is kiiktathatjuk így:

```python
def faktorialis_szamolas (szam):
    faktorialis=1
    for szorzo in range(1,szam):
        faktorialis*=szorzo
    return faktorialis

for n in range(int(input())):
    for k in range(n+1):
        n_alatta_k = faktorialis_szamitas(n) // (faktorialis_szamitas(k) * faktorialis_szamitas(n-k))
        print(n_alatta_k, end=' ')    
    print()
```

Folyamatosan újabb és újabb változatokat mutogatok, és az olvasást valószínűleg nehezíti, hogy mindig meg kell nézni, mi a különbség két egymást követő között. Jelölhettem volna a változásokat valami szép módon, de a saját lustaságomat félretéve: ugye milyen kellemes, hogy ehhez már nem kell fel-le görgetni, hanem elfér mindkét változat egy képernyőn? Így már jobban átérezzük, miért is jó a tömörebb kód.

Node nem végeztünk még. Bármikor, amikor van a kódunkban egy olyan rész, aminek az "értelme" jól körülhatárolható, azt érdemes egy függvénybe "kiszervezni" még akkor is, hogyha most egyelőre csak egyszer használjuk. 
A jól körülhatóságnak egy egészen jó definíciója, hogy egy-két értelmes magyar mondatban meg tudjuk-e határozni, hogy az a pár sor mit csinál. Ha igen, akkor jó eséllyel érdemes függvényt csinálni belőle. Ha azt látjuk, hogy ez a logika, működés máshol, önállóan is jól jöhet, megállja a helyét, akkor főleg ne habozzunk függvényt írni.

A fenti kódban ilyen a binomiális együttható kiszámítására a "képlet". Ez önállóan is értelmes dolog, máshol is kellhet a "későbbiekben" (ahogy beszéltük, a kód nem statikus, folyamatosan bővül, változik, stb.).

Kiszervezve afüggvénynek, megszüntetve a rövid életű `n_alatta_k` változót, és kicsit rövidítve a függvényneveket:

```python
def faktor (szam):
    faktorialis=1
    for szorzo in range(1,szam):
        faktorialis*=szorzo
    return faktorialis

def binom (n,k):
    return faktor(n) // (faktor(k)*faktor(n-k))

for n in range(int(input())):
    for k in range(n+1):
        print(binom(n,k), end=' ')    
    print()
```

## Végleges(?) változat

Ez az utolsó változat már nem bántja a szépérzékünket, rányomnánk a "Kész" pecsétet, de előtte azért nézzük meg, hogy működik-e. 

Próbaképp nézzük meg, mi történik 5-re:

```
1 
1 1 
1 1 1 
1 2 2 1 
1 3 6 3 1 
```

Minden jónak tűnik, de egy teszt nem teszt, szóval éljünk veszélyesen, nézzük meg 8-ra is:

```
1 
1 1 
1 1 1 
1 2 2 1 
1 3 6 3 1 
1 4 12 12 4 1 
1 5 20 30 20 5 1 
1 6 30 60 60 30 6 1 
```

Ez bizony nem jó, már a hatodik sorban abszolút hülyeségek jelennek meg. Mielőtt a szokásos szoftverfejlesztői depresszió elkapna minket, szerencsére eszünkbe jut, hogy jópár sorral feljebb már felvetődött, hogy a faktoriális számításnál a `range` nem biztos, hogy jó. 

Ezt most könnyen letesztelhetjük, hiszen csak beteszünk egy ilyen kódrészletet a "fő" kódunkba, és látjuk, hogy jól számolódnak-e ki a faktoriálisok:

```python
for i in range(10):
    print(faktor(n))
```
És látjuk, hogy nem jól, eggyel valóban el vagyunk csúszva. Megnézzük a függvényt, megtaláljuk a hibát, betesszük azt a `+1`-et, és akkor megvagyunk:

```python
def faktor (szam):
    faktorialis=1
    for szorzo in range(1,szam+1):
        faktorialis*=szorzo
    return faktorialis

def binom (n,k):
    return faktor(n) // (faktor(k)*faktor(n-k))

for n in range(int(input())):
    for k in range(n+1):
        print(binom(n,k), end=' ')    
    print()
```

Agyonteszteljük, de bárhogy próbálkozunk, nem tudunk kifogni rajta. Úgy néz ki, sikerült helyesen megoldani a feladatot.

## Megjegyzések

**SOHA** ne várjuk meg a teszteléssel amíg teljesen kész lesz a programunk. Amint van már egy értelmezhető működés, teszteljük le, hogy nincs-e benne hiba. Egy pici kódon sokkal könnyebb tesztelni, és esetlegesen hibát javítani. 
Ha meggyőződtünk róla, hogy jó ez a reszlet, akkor bővítjük a kódot, és amint lehet, megint tesztelünk. Ha hibába futunk, akkor tudjuk, hogy a hiba valószínűleg az újonnan megírt részben van, nem abban, amit 10 perce tüzetesen leteszteltünk.

A függvényekbe való szervezés ezt a hibakeresési folyamatot nagyban segíti. Sokkal nehezebb lett volna azonosítani a hiba helyét, ha nincs meg külön ez a függvényünk. Ha mondjuk a másikban lett volna a hiba, akkor a faktoriálist számító letesztelése után tudjuk, hogy máshol már nem lehet, mert a main-ben csak két for ciklus van, az rendben van, a faktoriális számító rendben van, a kettő között romlik el a dolog. 
Pár soros egyszerű függvények helyességéről meggyőződni mindig sokkal egyszerűbb, mint egy 30 soros kódról, amiben van 3-4 különböző logika.

## A tisztesség kedvéért

Függvények szintaktikája tehát a következő Pythonban:

```Python
def FUNCTION_NAME (ARGUMENTS) :
    FUNCTION BODY
```

Ahol:
 - a függvénynév ugyanolyan lehet, mint amiket eddig változóknak megengedtünk
 - argumentum lehet 0 darab, 1, vagy több, utóbbi esetben vesszővel vannak ezek elválasztva
 - két argumentumnak nem lehet ugyanaz a neve értelemszerűen
 - a függvénytörzsben ugyanúgy lehetnek utasítások, mint ahogy eddig a "főprogramunkban", azaz lehet használni változókat, ciklusokat, elágazásokat, meg lehet hívni másik függvényeket
 - `return` hatására a függvény futása véget ér, és visszaugrik a végrehajtás oda, ahol a függvény meg lett hívva
 - ha volt utána megadva érték, azt visszaadja (ha használva van)
 - egy törzsön belül lehet több `return` is, ennek tipikusan elágazásokon belül van értelme, mint egy `break`-nek a cikluson belül


Még nagyon sok tanulnivaló van a függvényekkel kapcsolatban, de a többit későbbre hagyjuk.
