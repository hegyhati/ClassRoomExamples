# Fájlkezelés

Nagyobb mennyiségű adatot a programjainkhoz viszonylag kényelmetlen mindig bepötyögni. Ezen valamennyire tudott segíteni a `python3 main.py < input.txt` bash magic, de azért nyilvánvalóan jobb lenne, ha a programunk képes lenne az adatokat egy fájlból beolvasni. 

Mindemellett az is jó volna, ha ki is tudnánk menteni dolgokat fájlokba, hogy a program következő futásakor azt beolvasva ugyanazzal tudjunk indulni.

Most 3 megoldást nézünk meg erre, mindegyiknek megvan az előnye, hátránya.

## Egyszerű, szüveges fájlkezelés

A legegyszerűbb módja egy fájl olvasásának, hogy az `open` függvénnyel "megnyitjuk":

```python
file=open("akarmi.txt","rt")
```

Itt az első argumentumn értelemszerűen a fájl neve, a második pedig `r`ead in `t`ext mode-ot jelent. 
`t` helyett lehetne `b` is, ami bináris olvasást jelöl,`r` helyett pedig lehetne pl. `w` vag `a`, errol majd hamarosan lesz szó.

Ezután a `file` egy "olvasó" magához a fájlhoz, amivel több mindent lehet csinálni:

```python
whole_content=file.read()
```

Ez nem csinál mást, mint a teljes tartalmát a fájlnak beleteszi a szöveges változóba.

```python
next_line=file.readline()
```
Ez kiolvas egyetlen sort a fájlból


```python
for line in file:
    # do something with line
```
Egyesével végigmegy a sorokon.

Fontos mindegyikhez megjegyezni, hogy egyrészt az újsor karakterek (`\n`) is benne maradnak a visszaadott szövegekben, másrészt ha egyszer már végigolvastuk valamelyik módon a fájlt, akkor utána még hiába hívunk meg bármilyen olvasást, az "olvasófejünk" a fájl végén van, nem fog visszaadni semmit.

Az olvasófejet a fájl elejére egy `file.seek(0)`-val tehetjük vissza.


Amikor végeztünk egy fájl beolvasásával, akkor egy `file.close()`-zal illik lezárni a dolgot.

Ha írni szeretnénk egy fájlba, akkor azt hasonló módon tehetjük meg: először meg kell nyitni a következő módok valamelyikével:

```python
overwrite_file=open("whatever.txt","wt")
append_file=open("whatever.txt","at")
```

Az első esetben ha már létezik a fájl, akkor felülírjuk, a második esetben a végére írunk hozzá. 

Ezek után egy `file.write("This is written into the file)` függvényhívással írhatunk a fájlba.

Terméeszetesen ha végeztünk, itt is illik egy `close()`-zal lezárni a dolgokat.

## Pickle

A `pickle` egy *modul* (akármik is legyenek azok), ami arra lesz alkalmas, hogy akármilyen változónk, adatunk van, azt könnyedén, bináris formában ki tudjuk menteni egy fájlba, vagy onnét visszaolvasni.

A használatához "be kell tölteni" a modult:

```python
import pickle
```

Ezt követően ha van egy összetett adatom, pl:

```python
runs = [
    {"distance": 12.3, "time":"01:01:01"},
    {"distance": 42.2, "time":"04:01:01"},
    {"distance": 21.1, "time":"01:35:13"},
    {"distance": 12.3, "time":"01:01:01"}
]
```
Akkor azt a következő módon tudom kimenteni egy fájlba, úgymond *dumpolni*:

```python
outfile = open("runs.pickle","wb")
pickle.dump(runs,outfile)
outfile.close()
```

Figyeljünk arra, hogy `wb`-t kell megadni, nem `wt`-t, mert a pickle bináris formátumban menti ki a dolgokat.

Ha valamikor vissza szeretnénk tölteni ezt a változót, akkor pedig így tehetjük meg:

```python
infile=open("runs.pickle","rb")
runs=pickle.load(infile)
infile.close()
```
Itt is figyeljünk az `rb`-re. 

Ha megnyitnánk egy ilyen fájlt, látjuk, hogy számunkra olvashatatlan.

## JSON fájlok

A JSON (JavaScript Object Notation) egy nagyon elterjedt [formátum](https://www.w3schools.com/js/js_json_intro.asp), weben gyakorlatilag ha adat közlekedik, az szinte mindig ebben a formában teszi. 

Lényegében majdnem teljesen megeggyezik azzal, ahogyan pythonban összetett adatokat kódban megadtunk.

Pár apró különbség van:
 - dictionary-k a szokott módon, de csak string lehet kulcs
 - listák a szokott módon
 - tuple-ök és set-ek nincsenek


Ha van egy json fájl, akkor azt a a `json` modul betöltése után így tudjuk beolvasni egy változóba:

```python
import json
file=open('data.json')
data = json.load(f)
f.close()
```

A másik irány érdekesebb: ha van egy összetett változónk, amit JSON formátumba szeretnénk átkódolni, akkor azt alábbi módon tehetjük meg:

```python

import json

foo = {
    "a" : 1,
    "b" : [1,2,3],
    (1,2) : {"a","b","c"},
    1 : (1,2,3)
}

json_representation=json.dumps(foo)

print(json_representation)
```

Ha a fenti programot megpróbáljuk futtatni, akkor nem fog sikerülni. A tuple kulcsot egyáltalán nem fogja engedni, illetve a set értéket sem. 

Ha ezeket átírjuk így:
```python
import json

foo = {
    "a" : 1,
    "b" : [1,2,3],
    1.2 : ["a","b","c"],
    1 : (1,2,3)
}

json_representation=json.dumps(foo)
print(json_representation)
```

Akkor már lefut a program, és ezt a kimenet produkálja:

```
{"a": 1, "b": [1, 2, 3], "1.2": ["a", "b", "c"], "1": [1, 2, 3]}
```

Pár külünbséget észrevehetünk:
 - amikor nem string volt a kulcs, akkor stringgé konvertálta
 - a tuple értékeket listává konvertálta


Ezt utána az első módszerrel kitehetjük egy fájlba.


## Összefoglalás

A használattól függ, hogy melyik eszközhöz érdemes nyúlni. Néhány (nem teljeskörű) tanács:
 - Ha csak logolni szeretnénk, emberek számára, és készőbb nem akarjuk a programunkkal beolvastatni, akkor az első módszer tökéletes.
 - Ha pythonból akarunk kimenteni adatot, amit mi ugyanúgy később, pl egy következő futás alkalmával szintén egy python kódban olvasnánk be, felhasználónak nem kell tudni olvasni, akkor pickle.
 - Ha a programunk külső forrásból vár adatot, vagy külső félnek, pl egy JS frontend ad adatot, akkor JSON.




# Kis kiegészítés for ciklusokhoz

Listát eddig kétféleképpen jártunk be: `for index in range(len(list))` vagy `for element in list`.
Az utóbbit használtuk akkor, ha elég volt nekünk csak az elem, és nem akartuk módosítani. Az elsőt használtuk akkor, ha valamiért fontos volt az index, vagy módosítani akartuk a listaelemet.

A kettő közül az első általánosabb, azonban ha mondjuk a ciklusmagon belül csak egy helyen van szükség magára az indexre, és 10 helyen az eltárolt elemre, akkor "kényelmetlen" mindenütt `lista[index]`-et irogatni. A második módszer viszont nem elég.

Ilyen esetekre hasznos a következő forma:

```python
for idx,item in enumerate(list)
    print (idx,". element: ",item)

```
