# Gyakorlo feladatok

A feladat lepesrol lepesre bonyolodik. Egy feladatra akkor menj tovabb, ha az elozo mar megvan. Azert, hogy minden egyes valtozat megmaradjon, vagy mindegyiket uj fajlba (`feladat_01.py, feladat_02.py`) keszitsd, vagy kulon fuggvenyekbe szervezd ki, kommenteld ki, stb.


## 1) Atlagfogyasztas
Irj programot, mely egy auto atlagfogyasztasat szamolja ki a kovetkezo modon: kerjen be 3 adatot: 
 - utazas elott teletankoltuk a kocsit, ekkot hany km-en allt az auto?
 - utazas utan szinten teletankoltuk a kocsit, ekkor hany km-en allt az atuo, es hany litert tankoltunk?
Ezek alapjan irja ki az atlagfogyasztast. 

Egy pelda a mukodesre:

```
Utazas elotti km: 13152
Utazas utani km: 13537
Masodik tankolas literben: 29

Ezak alapjan az auto atlagfogyasztasa 7.53 l/100km.
```

## 2) Fuggvenybe szervezes
A fenti kod legyen ugy modositva, hogy hasznaljon egy `atlagfogyasztas(km1, km2, liter)` fuggvenyt, mely a fenti 3 adatot kapja, es visszaadja az atlagos 100 km-enkenti fogyasztast.

## 3) Atlagfogyasztas tobb adatbol.
Fejlesszuk tovabb a programot ugy, hogy 5 teletankolashoz kerjuk be a km ora allas es tankolas mennyisege adatokat. 
Ebbol 4 olyan utazas adatunk lesz, mint az elozo. Irjuk ki ezt a 4 atlagfogyasztast. 

## 4) Kodszepites
Ha nem igy irtuk volna meg eleve, fejlesszuk tovabb az elozo programot ugy, hogy:
 - a bekert adatokat egy ilyen jellegu dictionary-ben tarolja el:
 ```python
 {
     "km": 13152,
     "l" : 13
 }
 ```
 - Ezeket a dict-eket egy listaba tegye bele. 

## 5) Legjobb es legrosszabb fogyasztas
A program ne a 4 atlagfogyasztast irja ki, hanem hogy melyik volt a legjobb es a legrosszabb.

## 6) Fuggvenyekre bontas
Az elozo program atszervezese ugy, hogy az alabbi foprogrammal egyutt tudjon mukodni:

```python
tankolasok = []
for _ in range(5):
    tankolas = tankolas_beker()
    tankolasok.append(tankolas)

print(f"A legjobb fogyasztas {minimum_fogyasztas(tankolasok)} l/100km volt.")
print(f"A legrosszabb fogyasztas {minimum_fogyasztas(tankolasok)} l/100km volt.")
```

Tehat legyen 3 fuggveny:
 - `tankolas_beker()` ami beker egy tankolast es visszaad egy fenti formaban megadott dictionary-t.
 - `minimum_fogyasztas(tankolasok)` ami var egy ilyen dict-ekbol allo listat, es visszaadja a legjobb fogyasztast
 - `maximum_fogyasztas(tankolasok)` ami var egy ilyen dict-ekbol allo listat, es visszaadja a legrosszabb fogyasztast

 ## 7) Ne csak 5 beolvasasra mukodjon
Ha a `minimum_fogyasztas(tankolasok)` vagy `minimum_fogyasztas(tankolasok)` barhol kihasznalta volna, hogy 5 tankolasi adatunk van, akkor modositsuk ugy ezeket a fuggvenyeket, hogy hosszabb listakkal is egyutt tudjon dolgozni.

## 8) Adatok olvasasa fajlbol
Modositsuk a programunkat ugy, hogy a tankolasi adatokat a [`tankolasok.json`](tankolasok.json) fajlbol olvassa be, majd ez alapjan irja ki, hogy mi volt a legkisebb es legnagyobb fogyasztas.

## 9) Tovabbi adatok kiirasa
A program a legjobb es a legrosszabb fogyasztas mellett irja ki azt is, hogy:
 - hanyszor tankoltunk
 - mennyi volt a teljes atlagfogyasztas
 - hanyszor volt necces a dolog (tegyuk fel, hogy 35 literes tankunk van, ezert minden tankolas, ami 30 liternel nagyobb volt, az necces.)

## 10) Naplozo program
Vegezetul fejlesszuk tovabb ugy a programot, hogy amikor elinditjuk, akkor megkerdezi, hogy mit szeretnenk csinalni, valahogy igy:
```
Mit szeretnel?
 1) Statisztikak kiirasa
 2) Uj tankolas felvitele
```
Ha a felhasznalo az 1-est valasztja, akkor irjon ki minden statisztikat az eddigieknek megfeleloen. 

Ha a masodikat valasztja, akkor kerjen be egy uj tankolas adatot (erre mar van fuggvenyunk 6. feladat ota), majd ezzel egeszitse ki a [`tankolasok.json`](tankolasok.json)-ben levo naplonkat, hogy legkozelebb mar ez az adat is szerepeljen a statisztikaban. 