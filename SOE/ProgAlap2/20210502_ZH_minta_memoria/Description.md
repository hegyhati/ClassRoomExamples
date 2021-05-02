# Programozás alapjai 2. - Próba ZH-2
2021.05.02

## 0. Bevezető

A feladat egy egyszerű 4x5-os memória játék leprogramozása. 
Aki nem ismerné, a játékot 20 kártyával játszák, minden kártyából pontosan 2 db ugyanolyan van, tehát 10 különböző.
A kártyákat lefordítva 4x5-ös elrendezésben letesszük az asztalra. Minden körben kettőt felfordítunk. Ha megeggyezik a két kártya, akkor felfordítva maradnak, egyébként újra lefordítjuk őket. 
A játék akkor ér véget, ha minden kártya felfordítva maradt már, azaz megtaláltuk az összes párt.

 # 1. Háttérlogika osztály

Készüljön egy `MemoryGame` osztály, mely megvalósítja a játék logikáját.
Az egyszerűség kedvéért a kártyákon most az 0,1,..9 számok szerepelnek. 

Az osztály a következő metódusokkal rendelkezzen:

 - `reset`, amely megkeveri a kártyákat, elrendezi őket 4x5-ös formában, valamint minden kártyát "lefordít".
 - `get`, mely koordináták alpaján megmondja, hogy ott milyen kártya van anélkül, hogy forgatná. Dobjon exceptiont, ha rossz koordinátát adunk meg.
 - `try`, mely két koordinátát kap, és a játék egy körének megfelelően megpróbálkozik velük: ha egyformák, felfordítva maradnak, ha nem, akkor lefordítva. A visszatérési érték ennek megfelelően `True` és `False` Ha valamelyik koordináta olyan, ami már fel van fordítva, vagy rossz, akkor dobjon exception-t. 
 - `is_upward`, amely visszaadja, hogy egy adott koordinátán lévő kártya fel van-e fordítva. Hibás koordináta esetén exception.
 - `is_won`, amely visszaadja, hogy véget ért-e már a játék.

Az osztály megvalósítása során a szabályok:
 - amikor létrejön egy példány, akkor resetelődjön.
 - semmelyik függványnek nem lehet semmilyen kiiratása a végleges változatban. 
 - egyik metódus sem használhat globális változókat, függvényeket, csak a sajátjait.
 - belső adatszerkezet, argumentumok típusa szabadon megválasztható, további privát metódusok kódszervezés jelleggel hozzáadhatók, publikusok nem.

# 2.Grafikus felület

Készüljön a játékhoz egy grafikus felület, amin játszani lehet. 

Legyen egy játéktér, ahol a 4x5 kártya látható. Ezen kívül legyen egy további gomb, amivel bármikor resetelhető a játék. 

Ha megnyertük a játékot, írja ki, hogy hány lépésből sikerült.

Az implementálás során a feltételek, javaslatok:
 - Megjelenésre nincsenek megkötések, mindenki annyira csinosítja, amennyire szeretné. Célszerű `Button`-oket használni a kártyáknak, de nem kötelező.
 - A `MemoryGame` osztály metódusai legyenek használva, semmilyen ott meglévő logika ne legyen duplikálva a GUI-ban. 
 - Nem kötelező osztályba szervezni a GUI-t, de pozitívan értékeljük.
 - Mást kell csinálni ha elsőnek, vagy másodiknak kattintunk egy kártyára. Ennek egyik lehetséges kezelési módja, hogy felveszünk egy változót az utolsó kattintás tárolására. Ez alapértelmezetten `None`. Első kattintáskor csak felfordítjuk a kiválasztott kártyát, majd eltároljuk a koordinátát ebben a változóban. A második kattintásnál ennek a változónak a tartalmából lehet tudni, hogy már a másodikat kattintottuk, és meghívhatjuk a ˙try`-t. 
 - A második kattintás után ha nem egyezik, akkor vissza kell fordítani ugye a kártyákat. Hogy ezt egy időzítővel oldja meg valaki, vagy a következő kattintás fordítja őket vissza automatikusan, az megintcsak szabadon választható.


 # További lehetőségek gyakorlásra
  - Tetszőleges méretű játék.
  - Számok helyett a grafikus felületen képek, vagy színek.
  - Smire nem szabadna már kattintani, az legyen disabled.
  - A GUI készítsen statisztikát arról, hány lépésben sikerül megfejteni.
  - Ha megnyertük, kérjen be nevet, és legyen toplista. 
  - Két játékos mód, ahol felváltva lép a két játékos, és az nyer, aki több párt talál meg.
  - A két járékos két különböző gépről tudjon játszani.
