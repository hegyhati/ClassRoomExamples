# Minta ZH

Keszits programot, mely egy (erosen limitalt utasitaskeszletu) Logo kodot olvas be, majd SVG-ben kirajzolja az eredmenyt. 

## Logo background

A `.logo` kiterjesztesu fajlunk a kovetkezo 3 utasitast tartalmazhatja:
 - `fd DISTANCE`: a teknoc elore megy `DISTANCE`-nyit
 - `rt ANGLE` : a teknoc jobbra fordul `ANGLE` _foknyit_
 - `lt ANGLE` : a teknoc balra fordul `ANGLE` _foknyit_

A teknoc a (0,0) pontbol indul, kezdetben eszakra nez, es feltetelezhetjuk, hogy helyes a beolvasando kod.

## SVG template

A kirajzolashoz hasznald a kovetkezo SVG template-et:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewbox="-20 -20 140 230">
	<line x1="0" y1="186" x2="0" y2="86" stroke="black" />
</svg>
```

## C++ fajlbeolvasas es iras
Mindkettohoz az `fstream` header-re van szukseg. Olvasashoz `std::ifstream`, irashoz `std::ofstream` tipusu objektumot kell letrehozni, konstruktronak megadva a fajlnevet. Ezek utan ugyanugy lehet oket hasznalni, mint az `std::cin`-t es az `std::cout`-ot olvasasra, illetve irasra. A streamet a muvelet vegen egy `.close()`-zal le kell zarni.


Egyszeru pelda minden szo beolvasasara:
```cpp
#include <fstream>
#include <string>

int main() {
    std::ifstream s("example.txt");
    std::string word;
    while (!s.eof()) {
        s >> word;
        // do something with word
    }
    s.close();
}
```
## Szogfuggvenyek

A teknoc poziciojanak kiszamolasahoz kelleni fognak majd szogfuggvenyek, ezek a `cmath` headerben talalhatok meg. Figyeljunk ra, hogy a `sin` es `cos` fuggvenyek **radiant** varnak.

## Megoldas lepesei

### 2D pont

Elsonek keszits egy `Point2D` osztalyt/strukturat melynek van x es y adattagja (`double`).

### PolyLine

Keszits egy `PolyLine` osztalyt, mely egy torottvonalat fog tarolni. A publikus fuggvenyei:
 - `PolyLine::PolyLine()` : letrehozza uresen az objektumot
 - `PolyLine::append(Point2D point)` : kiegesziti a torottvonalat egy ujabb ponttal
 - `PolyLine::clear()` : torli a teljes vonalat
 - `PolyLine::saveToSVG(std::string filename)` : elkesziti az SVG fajlt

### main

A main inicializalja a teknoc helyzetet (0,0)-ra, az iranyt ahova nez 90 fokra. 
Ezutan olvassa be a [house.logo](house.logo) fajlban talalhato parancsokat es mindegyik utan szamolja ki a teknoc uj poziciojat, es tegye bele egy tortvonalba. A vegen exportalja a tortvonalat a [house.svg](house.svg) fajlba.

## Pelda 

Bemenet:
```logo
fd 100 
    rt 30 fd 100 rt 120 fd 100 rt 120 fd 100 rt 90
rt 90
fd 100
rt 90
fd 100
rt 90
fd 100
rt 90
```
Kimenet:

![SVG output](house.svg)