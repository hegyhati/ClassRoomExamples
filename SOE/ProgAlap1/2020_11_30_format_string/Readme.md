# Formázott szöveg kiírás

Eddigi kódjainkban gyakran előfordultak ilyesmi kiiratások:

```python
print(name + " osszesen " + str(count) + " alkalommal csinalt valamit.")
```

vagy:
```python
print(name, " osszesen ", str(count), " alkalommal csinalt valamit.")
```

Ez nem túl szép megoldás, mert keveredik a kód, és a kiiratás szövege. Ezzel könnyű hibákat véteni, rémálom fordítóknak (lokalizációs értelemben, nem compiler) odaadni, stb. 

Sokkal szebb lenne, ha valami placeholderek lennének hagyhatók a szövegben ott, ahol az adatot szeretnénk kiírni, és utólag határoznánk meg, hogy milyen adat legyen behelyettesítve. Erre pythonban 3 mód is létezik:
  - `"%s osszesen %d alkalommal csinalt valamit." % (name,count)`
  - `"{} osszesen {} alkalommal csinalt valamit.".format(name,count)"`
  - `f"{name} osszesen {count} alkalommal csinalt valamit."`

Az első a "régimódi" megközelítés, aki találkozott `printf`-el más nyelvekben, annak ismerős lehet a szintaktikája. A második módszer a python 2.6-os verziójával érkezett meg, és "more pythonic", a harmadik f-string megoldás pedig 3.6 óta létezik. Hatékonyság szempontjából az utolsó a leggyorsabb, azonban itt most a fenti szétválasztás érdekében az középsőt nézzük meg. Ha valakinek a harmadik tetszik jobban, járjon utána, használja nyugodtan, szituációja válogatja, melyik a kézenfekvőbb.

Az alapvető működés meglehetősen egyszerű: `{}` az áhított placeholder, majd a `.format()` függvénynek fel kell sorolni, hogy ezek helyére mit írjon ki. Nincs szükség megmondani előre, hogy milyen típusú az a valami, vagy stringgé konvertálni. 

Próbáljátok ki, mi történik, ha kevesebb, vagy több argumentumot kap a `format` mint amennyit kellene!

Ezen az alapműködésen felül rengeteg mindent testre lehet még szabni, van ennek szép hosszú dokumentációja, álljon itt néhány példa.

```python
"{0} is {1}".format("time","relative")
```

Tehát meg lehet adni explicit, melyik placeholder helyére hányadik argumentum kerüljön. Ez akkor hasznos értelemszerűen, ha változtatunk a sorrenden, például egy más nyelvre történő fordítás során. Ilyenkor nem kell a kódon módosítani, csak a string literálon:

```python
"The candidate of the {0} party received {1} percent of the votes.".format(pname,ratio)
"A szavazatok {1} százalékát a {0} párt kapta.".format(pname, ratio)
```

Ha egy dictionary több adatát iratnánk ki, akkor két lehetőség is adott:

```python
player={"name":"Kocsis Sándor", "score":11, "nationality":"HU"}
"{} osszesen {} golt lott a vilagbajnoksagon".format(player["name"],player["score"])
"{0[name]} osszesen {0[score]} golt lott a vilagbajnoksagon".format(player)
```

A kiiratás formáját is testreszabhatjuk, pl:
```python
"10 karakter szelesen kiirt adat: {:10}".format(data)
"10 karakter szelesen kiirt adat balra igazitva: {:<10}".format(data)
"10 karakter szelesen kiirt adat jobbra igazitva: {:>10}".format(data)
"10 karakter szelesen kiirt adat kozepre igazitva: {:^10}".format(data)
```

Van még sok további lehetőség, ha valamire szükségetek van, üssétek fel a [dokumantációt](https://docs.python.org/3/library/string.html#custom-string-formatting), és nézzétek meg, van-e valami ami jól jön.

# Véletlen

Gyakran szükségünk van a programjainkabn valamilyen véletlenszerű működésre. Ehhez a `random` modul nyújt segítséget. A teljesség igénye nélkül náhány hasznos függvény:

```python
import random

random.random() # Veletlenszeru float a [0,1[ intervallumbol
random.uniform(a,b) # Veletlenszeru float az [a,b] intervallumbol
random.randint(a,b) # Veletlenszeru int az {a,a+1,a+2,....b} szamok kozul
random.choice(mylist) # Veletlenszeru elem a listabol
random.shuffle(mylist) # Osszekeveri a lista elemeit
```

# Modulok

A múlt heti óra ütmezős kódja már kellően nagy és csúnya lett, érződik, hogy jó volna a függvényeket valahogy nagyobb blokkokba szervezni, amik logikailag összetartoznak, és ezeket külön fájlokba szétpakolni. Erre (is) valók a modulok. Modulból már használtunk többet is, például `random`, `json`, `pickle`. 

Ha egy saját modult, mondjuk `vector2d` szeretnénk csinálni, nem kell mást tennünk, mint minden logikailg a 2D vektorokhoz kapcsolódó függvényt beletenni egy `vector2d.py` fájlba, pl:

```python
# content of vector2d.py

def length(v):
    return (v[0]**2 + v[1]**2)**0.5
def add(u,v):
    return (u[0]+v[0],u[1]+v[1])
def scalar_product(u,v):
    return u[0]*v[0]+u[1]*v[1]
def is_parallel(u,v):
    return u[0]*v[1]==v[0]*u[1]

#...

```

Ezek után egy másik fájlban mondjuk a  `main.py`-ban a következő módon tudjuk használni ezeket a függvényeket:

```python
# content of main.py

import vector2d as v2d

vec1=(1,2)
vec2=(-4,3)

print ("The scalar product of {} and {} is {}".format(vec1,vec2,v2d.scalar_product(vec1,vec2))
```