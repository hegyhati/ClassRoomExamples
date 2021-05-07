# Programozás alapjai 2. -  ZH-2
2021.05.07

## 0. Bevezető

A feladat egy olyan program elkészítése, amely segít nekünk kiszámolni, hogyha adott kadenciával (fordulatszám percenként) tekerünk a bringánkon, akkor mennyi lesz a sebességünk, ha föl-le váltogatunk.

Az egyszerűség kedvéért olyan bringáról lesz szó, aminek csak egy első lánckereke van, hátul tudunk csak váltani.

 # 1. Háttérlogika osztály

Készüljön egy `Bike` osztály, melyet egy ilyen szerkezetű JSON fájlból lehet inicializálni:

```json
{
  "chainring" : 52,
  "cassette" : [11,12,13,14,15,16,17,19,21,23,25],
  "wheel_diameter" : 622

}
```
Az első értelemszerűen a fogak száma az egyetlen első lánckeréken, a második a hátsó lánckerekek fogszáma növekvő sorrendben. 
A harmadik pedig a kerék átmérője milliméterben.
Inicializálás után a lánc a legkisebb fogaskeréken legyen. (11-es a fenti példa alapján)

Az osztály a következő metódusokkal rendelkezzen:
 - `get_current_gear`: visszaadja, hogy épp melyik lánckeréken vagyunk hátul, alulról számolva, 1-el indítva
 - `get_current_teeths`: visszaadja, hogy hány fog van az aktuális fogaskeréken (hátul)
 - `shift_up`: egyet "felfele", azaz a nagyobb fogaskerekek irányába vált, ha tud
 - `shift_down`: értelemszerűen fordítva mint az előző
 
Az osztály megvalósítása során a szabályok:
 - semmelyik függványnek nem lehet semmilyen kiiratása a végleges változatban. 
 - egyik metódus sem használhat globális változókat, függvényeket, csak a sajátjait.
 - belső adatszerkezet, argumentumok típusa szabadon megválasztható, további privát metódusok kódszervezés jelleggel hozzáadhatók, publikusok nem.

# 2.Grafikus felület

Készüljön egy grafikus felület, ahol váltogathatunk, és nézhetjük, hogy változik a sebességünk.

A felületen:
 - Lehessen valamilyen módon megadni a kadenciát (Spinbox, Entry, pl) (fordulat per perc mértékegységben)
 - Látszódjon, hogy épp melyik sebességben vagyunk hátul
 - Lehessen sebességet váltani valahogy
 - Látszódjon a kadencia és váltóállás melletti sebesség km/h-ban

Értelemszerűen ha sebességet váltunk, akkor annak megfelelően változzon a sebesség.

Nem kell tudnia a programnak, hogy a kadencia változtatás után/közben is változzon a sebesség, elég ha csak a következő váltás után frissül. (Pirospont ha valaki mégis megcsinálja.)

A felület inicializáláskod kapjon egy `Bike` objektumot, illetve nem ismételhet semmilyen logikát, ami abban az osztályban már szerepel.

# Némi segítség a sebesség kiszámításához

A legegyszerűbben ezekkel a lépésekkel számolható ki a sebesség:
1. Pedálfordulatszámból megvan hogy egy óra alatt hányszor fordul körbe a pedál
2. Ebből és a az első lánckerék fogszámából kiszámolható, hogy hány láncszemnyit "ment odébb" a lánc (1 óra alatt)
3. Ebből és a hátul aktuálisan használt lánckerék fogszámából kiszámolható, hogy 1 óra alatt hányszor fordulna körbe a (hátsó) lánckerék, ami ugyanannyi, mint ahányszor a kerék is körbefordul.
4. Ebből és a kerék kerületéből megvan, hogy egy óra alatt mennyit ment előre a bringa. (hossz mértékegységre figyelni!)

