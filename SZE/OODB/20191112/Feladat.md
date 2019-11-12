# OO Programozás minta vizsga

Készítsen C++ osztályokat zeneszámok és videók közös lejátszási listájának kezeléséhez.

A kétféle médiaelem adatainak tárolásához készítse el az alábbi osztályokat:

- `Music`
    - Tárolja az előadó nevét, a szám címét, és hosszát (sec), ezek megadása legyen kötelező a konstruktorban, és ne legyenek módosíthatók.
    - Legyen egy `print()` metódusa, ami írja ki a fenti adatokat a standard kimenetre: `Artist - Title (m:ss)`
- `Video`
    - Tárolja a videó címét, hosszát (sec), vízszintes és függőleges felbontását (px), ezek megadása legyen kötelező a konstruktorban, és ne legyenek módosíthatók.
    - Legyen egy `print()` metódusa, ami írja ki a fenti adatokat a standard kimenetre: `Title (m:ss - width x height)`
- `Media`
    - A `Music` és `Video` közös adatait (cím és hossz) tárolja, és megadja a közös interfészüket.
    - Ne lehessen példányosítani.

Készítsen egy `MultiMediaPlaylist` osztályt, amely a lejátszási listát valósítja meg. A következő funkciókat valósítsa meg:

- `current()`: Az aktuálisan játszott média (első elem) címének visszaadása. Üres lista esetén adjon vissza null-pointert. A visszaadott pointeren keresztül ne legyen módosítható a médiaelem.
- `add(media)`: A paraméterben (cím szerinti átadással) kapott médiaelemet adja hozzá a lista végéhez. Gondoskodjon róla, hogy később a kapott objektumok memóriaterülete felszabadításra kerüljön.
- `skip()`: Törölje az első elemet a listából.
- `sortByLength()`: Rendezze a lista elemeit hosszuk szerint növekvő sorrendbe.
- `sortByTitle()`: Rendezze a lista elemeit cím szerint ábécésorrendbe.
- `print()`: Írja ki a lista elemeit.

A fenti feladatleírás helyes megoldása elégséges érdemjegyet ér. Az érdemjegy értéke növelhető az alábbi módokon:

- +1, ha kihasználja a standard library által nyújtott eszközöket: a lejátszási lista tárolásához a legmegfelelőbb STL tárolót használja **ÉS** a rendezésekhez az `std::sort()` függvényt használja.
- +1, ha a megvalósítja a médiaadatok bármilyen standard kimeneti streamre való kiírását `<<` operátorral. Pl.: `std::cout << *mediaPtr`. A kiírt adatok tartalmazzák a zenék és videók specifikus adatait is.
- +1, ha a `MultiMediaPlaylist`hez olyan másoló konstruktort készít, ami a cím szerint tárolt médiaelemekből megfelelő típusú másolatokat készít.

A megoldás teszteléséhez használhatja a mellékelt `main.cpp`-t.

Példa kimenet:
````
Playlist contents:
  0 - Foobar Fighters - The Preprocessor (4:29)
  1 - Ricky and Mort S04E01 (22:00 - 1920 x 1080)
Currently playing: Foobar Fighters - The Preprocessor (4:29)
After sortByLength():
Playlist contents:
  0 - Rage Against The Computer - Nulls On Parade (3:50)
  1 - Foobar Fighters - The Preprocessor (4:29)
  2 - Ricky and Mort S04E01 (22:00 - 1920 x 1080)
After sortByTitle():
Playlist contents:
  0 - Rage Against The Computer - Nulls On Parade (3:50)
  1 - Ricky and Mort S04E01 (22:00 - 1920 x 1080)
  2 - Foobar Fighters - The Preprocessor (4:29)
Current playback finished: Rage Against The Computer - Nulls On Parade (3:50)
Next up: Ricky and Mort S04E01 (22:00 - 1920 x 1080)
Playlist contents:
  0 - Ricky and Mort S04E01 (22:00 - 1920 x 1080)
  1 - Foobar Fighters - The Preprocessor (4:29)
Playlist contents:
  0 - Ricky and Mort S04E01 (22:00 - 1920 x 1080)
  1 - Foobar Fighters - The Preprocessor (4:29)
Playlist contents:
  0 - Foobar Fighters - The Preprocessor (4:29)
TEST: Playlist should be empty now:
Playlist contents:
````