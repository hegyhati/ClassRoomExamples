# Listák

## Prológ / Mese-mátka

Amikor sok adatunk van, azt az átláthatóság, könnyebb/algoritmikus kezelhetőség miatt célszerű valamilyen formában csoportosítani, ha az logikailag is indokolt.
Szinte minden manapság használt programozási nyelv biztosít erre különbözű lehetőségeket. 
Ezek megjelenhetnek típusok formájában, vagy összetett sablon osztályokként, stb. 

A Python is támogat több ilyen típust, ezek közül az egyik legalapvetőbbel, a **listával** barátkozunk most meg.

### Mi az a lista?

Egy olyan adatszerkezet, amiben több adat van, és ezeket **sorban** tudjuk elérni, mindegyiknek megvan, hogy hányadik a listában. 

### Mikor gondoljunk listára?

Akkor, amikor több, logikailag összetartozó adatot kezelünk, melyek általában "azonos típusúak", csak különböző helyen, időben, stb keletkeztek. 

Tehát például ha az idei hazai COVID napi új fertőzésszámok statisztikáit szeretnénk valahol tárolni, akkor nem 365 darab változót veszünk fel, hanem egy listát, amiben benne van ez a 365 szám. 

Ha egy matematikai sorozat elemeit nézzük, azt is tehetjük egy listába, vagy például egy osztálynévsort.

### Mikor ne gondoljunk listára?

Egy listán belül az elemeknek adott a sorrendje, és a pozíciójuk alapján érjük el, azonosítjuk őket. 
Ha a sorrend nem fontos, akkor lehet más eszköz ideálisabb (erről később), azonban ha az azonosításhoz/eléréshez nem egy számszerű pozíció az ideális, hanem valami más, akkor mindenképp mást kell használnunk, erről pár hét múlva lesz szó. 
Tehát ha például a ZH eredményeket szeretnénk eltárolni, akkor ott név alapján keresnénk ki az eredményeket, nem pozíció alapján.

Ugyanígy nem érdemes listába tenni olyan adatokat, melyek akár azonos típusúak, de logikailag nem egy valaminek sok példánya. Például ha tárolunk valakiről olyan egészségügyi adatokat, mint a testtömege, magassága, testzsír ősszetétele, stb., akkor ezek mind numerikus adatok, de ettől még nem tesszük egy listába őket, mert logikailag különböző jelentésük van.

### Másik nyelven láttam már tömböket, akkor ezek ugyanazok?

Nem, de nagyon hasonlítanak rájuk, illetve alkalmazhatók "tömbként". Vannak nyelvek, ahol például teljesen más eszköz van fix méretű tömbre, változó méretű tömbre, és listára. 
Pythonban nincs ilyen szétszedés, ugyanaz az egy adatszerkezet tölti be az összes ilyen funkciót. 
Ennek vannak következményei arra vonatkozóan, hogy a memóriában hogy jelennek meg, de számunkra ez nem fontos. Egy kicsit fogunk erről beszélni pár hét múlva.

## Elég a mese, kódot ide nekem!

Fair enough...

![I hear and I forget. I see and I remember. I do and I understand. - Confucius](https://www.azquotes.com/picture-quotes/quote-i-hear-and-i-forget-i-see-and-i-remember-i-do-and-i-understand-confucius-6-21-24.jpg)

### Hogy hozom létre?

Egy listát szögletes zárójelek közötti felsorolással adunk meg, vesszővel elválasztva, pl.:

```python
mintalista=[1,1,2,3,5,8,13]
```

Egy lista lehet teljesen üres is:

```python
ureslista=[]
```

Ha ugyanazzal az elemmel szeretnénk feltölteni egy adott méretű listát, arra van egy egyszerű mód:

```python
tizelemulista=[0]*10
```

Ez ugyanazt eredményezi, mintha azt írtuk volna, hogy `tizelemulista=[0,0,0,0,0,0,0,0,0,0]`. 
Viszont a szorzatos formának a tömörségen kívül még előnye, hogy a szorzó nem csak konstans, "kódba égetett" szám lehet, hanem egy változó is. 
Emiatt ha nem a program írásakor, hanem futási időben derül ki, hogy mekkora listára van szükségünk, akkor is megfelelően működik.


## Hogy érem el, változtatom az adatokat?

A lista egy adott elemét szögletes zárójelben indexeléssel lehet elérni.
Fontos, hogy `0`-val kezdjük az indexelést.

A fenti példánál maradva, `mintalista[0]` értéke 1, `mintalista[1]` értéke szintén 1, `mintalista[2]` értéke 2, stb. 
Ezeket ugyanúgy kezelhetjük, mint bármilyen másik változót múlt hétről. Tehát ha beírjuk azt, hogy ```mintalista[0]=12`, akkor azzal a lista legelső elemét lecseréljük. 

Egy hasznos trükk, hogyha az utolsó elemet szeretnénk elérni, akkor használhatjuk a `-1` indexet, az utolsó előttihez a `-2`-t, stb. 
Tehát `mintalista[-1]` értéke 13.

## Mi történik, ha olyan indexre írok, ami (még?) nincs a listában?

Ha a listánkban `n` elem van, akkor `-n`-től `n-1`-ig indexelhetjük. 
Ha ezen az intervallumon kívüli indexet adunk meg, hibát fogunk kapni, figyeljünk erre.

A lista méretét mindig megtudhatjuk a `len` *függvénnyel*, a `len(ureslitsa)` 0-t fog adni, a  `len(mintalista)` pedig 7-et.

## És akkor nem is változtathatom a méretét egy listának, nem tudom bővíteni?

De, erre több lehetőség van, mi ezek közül most egyet használunk csak egyelőre, az `append` *függvényt* (akármit is jelentsen az):

```python
ureslista=[]
ureslista.append(123)
ureslista.append(43)
ureslista.append(0)
```

A kód eredményeképp lesz egy `[123,43,0]` *tartalmú* listánk, azaz az `append` függvény mindig a lista végére teszi be az új elemet.


## Számolni tudok vele, rendben, de hogy írom ki?

A lista egy elemét ugyanúgy ki lehet írni a `print`-tel mint egy bármilyen változót, az alábbi kód például kiírja az összes elemet külön külön sorokba:

```python
idx=0
while idx < len(lista)
    print(lista[idx])
    idx+=1
```
Vagy egy kicsit fancybb formában:

```python
idx=0
while idx < len(lista)
    print("A lista "+str(idx+1)+". eleme: " + str(lista[idx]))
    idx+=1
```

Ha nem a felhasználó számára írunk ki kimenetet, hanem csak magunknak, vagy fájlba mentünk, stb, akkor kényelmes megoldás, hogy a print-nek átadható maga a lista is:


```python
lista=[1,4,4,4]
lista.append(1)
lista[2]=6
print(lista)
```

A fenti kód egy `[1, 4, 6, 4, 1]` kiiratást eredményez a kimeneten.


## Pár záró gondolat

A listákban tárolt adatoknak nem kell azonos típusuaknak lenniük, sőt, listának eleme is lehet lista, aminek minden eleme lista, stb. 
Ilyeneket később nézünk majd meg. Illetve többször szerepelt korábban a *függvények* fogalma, amiket még nem tanultunk. 
Éppen ezért egyelőre épp csak annyit néztünk meg, amit feltétlenül muszáj: `len` és `append`. 
Egyelőre csak jegyezzük meg, hogy kell ezeket használni, és majd kicsit később tanuljuk meg, hogy mi történik a háttérben.
