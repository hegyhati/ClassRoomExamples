# PótZH feladat Programozás Alapjai 2 tárgyhoz
Az elkészítendő program áll egy alap részből, melynek maradéktalan teljesítése szükséges az alíárás megszerzéséhez.
Ezen felül adottak plusz feladatok, melyek teljesítésével plusz pontok szerezhetők, amit pozitív irányban figyelembe veszünk a félév értékelése során.

A szükséges szintet az egyszerűbb elkészítés és ellenőrzés céljából több lépésre bontottuk. Javasoljuk, hogy mindenki ezeken a lépéseken menjen végig sorrendben.

## 0. lépés: "irodalmazás"
A ZH témája egy **nagyon lebutított** [Kockapóker/Yahtzee](https://hu.wikipedia.org/wiki/Kockap%C3%B3ker) játék elkészítése. Az alap változatban mindössze annyiról van szó, hogy van 5 darab szabványos D6 dobókocka, amivel először mindegyikkel dobunk. Ezután minden körben ezek valamilyen részhalmazával dobunk újra. A játék addig tart, míg mind az 5 kockán ugyanaz nem lesz. 

## 1. lépés: alaposztály
Készítsünk egy `Dice` nevű osztályt, ami egy hat oldalú dobókockát modellez.
Ennek az osztálynak legyen egy:
 - paraméter nélküli konstruktora, ami még nem gurítja el a kockát, csak létrehozza. 
 - `void roll()` függvénye, mely elgurítja a kockát, amin aztán random 1-6 lesz felül
 - FOKSZ: `Integer getValue()` függvénye, mely visszaadja, hogy mit sikerült gurítani. Ha még nem gurítottuk el a kockát a létrehozása óta, akkor térjen vissza `null`-lal.
 - BSc: `int getValue()` függvénye, mely visszaadja, hogy mit sikerült gurítani. Ha még nem gurítottuk el a kockát, akkor dobjon egy `NotYetRolledException`-t

Egy lehetséges egyszerű, nem mindenre kiterjedő tesztelés:

FOKSZ:

```java
Dice dice = new Dice();
if(dice.getValue()==null) System.out.println("[OK] dice not yet rolled.");
else System.err.println("[ERROR] not yet rolled dice have a value.");
dice.roll();
if(dice.getValue()==null) System.err.println("[ERROR] rolled dice does not have a value");
else System.out.println("[OK] rolled dice has a value");


boolean stresstest=true;
for(int i=0; i<1000; i++){
  dice.roll();
  Integer value=dice.getValue();
  if(value==null || value < 1 || value > 6) {
    System.err.println("[ERROR] rolled dice does not have a value or has invalid value: " + value);
    stresstest=false;
  }
}
if(stresstest) System.out.println("[OK] Stresstest passed, dice always has proper value.");

```


BSc:

```java
Dice dice = new Dice();
try {
  Integer value=dice.getValue();
  System.err.println("[ERROR] not yet rolled dice have a value.");
} catch (NotYetRolledException e){
  System.out.println("[OK] dice not yet rolled.");
}
dice.roll();
try {
  Integer value=dice.getValue();
  System.out.println("[OK] rolled dice has a value")
} catch (NotYetRolledException e){
  System.err.println("[ERROR] rolled dice does not have a value");
}


boolean stresstest=true;
for(int i=0; i<1000; i++){
  dice.roll();
  try{
    Integer value=dice.getValue();
    if(value==null || value < 1 || value > 6) {
      System.err.println("[ERROR] rolled dice has invalid value: " + value)
      stresstest=false;
    }
  }catch (NotYetRolledException e){
    System.err.println("[ERROR] rolled dice does not have a value");
    stresstest=false;
  }
}
if(stresstest) System.out.println("[OK] Stresstest passed, dice always has proper value.");

```

## 2. lépés: karakteres játék
Készítsen `Yahtzee` osztályt, mely a femt leírt játékot szimulálja. 5 kocka, elsőre mindegyikkel gurít, majd utána csak azokkal, amiket kiválasztottunk.

Az osztálynak van egy alapértelmezett konstruktora, mely rögtön gurít is egyet mindegyik kockával.

Legyen továbbá egy `void rollDices(int [])` függvénye, mely a megadott indexű kockákat újragurítja.

Legyen az osztálynak felüldefiniálva a `toString` metódusa, ami valamely egyszerű módon kiírja a játék helyzetét, pl:

```
Dice 1: 3
Dice 2: 3
Dice 3: 4
Dice 4: 1
Dice 5: 2
```

vagy akár így (a ⚀ kódja `0x2680`): 
```
<< ⚁ ⚅ ⚁ ⚄ ⚁ >>
``` 

Legyen az osztálynak egy `boolean isYahtzee()` függvénye is, ami igazzal tér vissza, ha mindegyik kockán ugyanaz van felül.

Egy lehetséges tesztelő függvény:

``` java
Yahtzee game = new Yahtzee();
Scanner sc = new Scanner(System.in);

while (!game.isYahtzee()) {
  System.out.println("" + game + " Which dices would you like to roll?");
  char[] selectionChars = sc.nextLine().replaceAll("\\D", "").toCharArray(); 
  int[] selection = new int[selectionChars.length];
  for (int i = 0; i < selection.length; ++i)
    selection[i] = Character.getNumericValue(selectionChars[i]);
  game.rollDices(selection);
}
System.out.println(game);
System.out.println("Congrats, you won the game!");
```

Amivel így néz ki egy példajáték:

```
<< ⚁ ⚅ ⚁ ⚄ ⚁ >> Which dices would you like to roll?
2 4
<< ⚁ ⚀ ⚁ ⚀ ⚁ >> Which dices would you like to roll?
24
<< ⚁ ⚃ ⚁ ⚂ ⚁ >> Which dices would you like to roll?
2 and 4
<< ⚁ ⚂ ⚁ ⚃ ⚁ >> Which dices would you like to roll?
2,4
<< ⚁ ⚃ ⚁ ⚃ ⚁ >> Which dices would you like to roll?
24
<< ⚁ ⚁ ⚁ ⚅ ⚁ >> Which dices would you like to roll?
finally, only 4
<< ⚁ ⚁ ⚁ ⚅ ⚁ >> Which dices would you like to roll?
4!
<< ⚁ ⚁ ⚁ ⚃ ⚁ >> Which dices would you like to roll?
4, please
<< ⚁ ⚁ ⚁ ⚂ ⚁ >> Which dices would you like to roll?
almost. 4
<< ⚁ ⚁ ⚁ ⚁ ⚁ >> Congrats, you won the game!
```

## 3. lépés: grafikus játék
Valósítson meg egy egyszerű grafikus felületet, amelyen ezt a játékot lehet futtatni.
 - A felületen valahogy jelenjen meg a játék helyzete, pl:
    - 5 db `JLabel`/`JLabel`/`JCheckBox`
    - 1 db `JList` 
 - Valamilyen módon lehessen megmondani, hogy melyik kockákkal szeretnénk gurítani újra.
 - Ha megvan a póker, akkor valahogyan ezt tudassa velünk a program.

## Plusz kiegészítő lehetőségek
 - Ne `isYahtzee` függvény legyen, hanem egy `int getYahtzeeValue()` mely 50-et ad vissza, ha van póker, és 0-t ha nincs. A játék csak 2 körig megy, és a végén kiderül, mennyi pontot ér.
 - Ne csak a pókert ellenőrizze a játék, hanem hasonlóan legyenek `getFullHouseValue`/`getChanceValue`/... függvények (ebből néhányat valósítson meg, pontszámítás röviden [itt](https://en.wikipedia.org/wiki/Yahtzee#Lower_section).  A program 2 lépés után írja ki, hogy melyik formációk szerint ér pontot a játék, és mennyit.
 - Az előzőt egy kicsit szebben megoldani úgy, hogy egy osztályhoz tartozó publikus enum tárolja a lehetséges kombókat, és `int getValue(Type type)` függvény adja vissza, hogy abból a típusból mennyi pontot ér az adott kockagurítás.
 - A játék legyen több körös, midnen körben 2x lehet újragurítani. Minden körben az egyik opcióhoz el kell számolni a gurítást, akkor is, ha mindegyik szerint 0 pontot ér. A játék annyi körig tart, ahány típus meg lett valósítva, és a végén kiírja az összpontszámot és akár azt is, hogy ezt milyen gurításokkal sikerült elérni.
