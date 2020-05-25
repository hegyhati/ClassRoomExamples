# PótZH feladat Programozás Alapjai 2 tárgyhoz
Az elkészítendő program áll egy alap részből, melynek maradéktalan teljesítése szükséges az alíárás megszerzéséhez.
Ezen felül adottak plusz feladatok, melyek teljesítésével plusz pontok szerezhetők, amit pozitív irányban figyelembe veszünk a félév értékelése során.

A szükséges szintet az egyszerűbb elkészítés és ellenőrzés céljából több lépésre bontottuk. Javasoljuk, hogy mindenki ezeken a lépéseken menjen végig sorrendben.

## 0. lépés: "irodalmazás"
A ZH témája egy egyszerű [Akasztófa](https://hu.wikipedia.org/wiki/Akaszt%C3%B3fa_(j%C3%A1t%C3%A9k)) játék elkészítése.
Az alap változatban csak az angol ABC betűit használjuk, nincsenek szóközök, és egyéb speciális karakterek, és az ötödik mellélövésnél vége a játéknak.

## 1. lépés: alaposztály
Készítsünk egy `HiddenWord` nevű osztályt, ami egy olyan szót modellez, aminek egy része el van rejtve.
Ennek az osztálynak legyen egy:
 - egy `String`-et váró konstruktora, mely beállítja a szót csupa nagybetűssé alakítva, és kezdetben minden karakter rejtett. 
 - `String toString()` metódusa felüldefiniálva úgy, hogy a rejtett karakterek helyén `_` jelenjen csak meg. 
 - `ArrayList<Integer> reveal(char character)` függvénye, mely a megadott karakter összes előfordulását "felfedi" a szóban. (Mostantól a `toString` által visszaadott Stringben már látszódnak. A függvény térjen vissza azoknak az indexeknek a listájával, ahol ez a karakter előfordult.
 - `boolean isRevealed()` függvénye, mely akkor tér vissza `true`-val, ha a szó összes karaktere felfedett.

Egy lehetséges egyszerű, nem mindenre kiterjedő tesztelés:



```java
    HiddenWord test= new HiddenWord("Rickroll");

    System.out.println(test);
    if (test.toString().equals("________")) System.out.println("[OK] Correct starting clue");
    else System.err.println("[ERROR] Incorrect starting clue");

    ArrayList<Integer> response;

    response=test.reveal('R');
    if(response.size()==2) System.out.println("[OK] Found correct number of matches for R");
    else System.err.println("[ERROR] Found incorrect number of matches for R");

    System.out.println(test);
    if (test.toString().equals("R___R___")) System.out.println("[OK] Correct clue after R");
    else System.err.println("[ERROR] Incorrect clue after R");

    response=test.reveal('A');
    if(response.size()==0) System.out.println("[OK] Found correct number of matches for A");
    else System.err.println("[ERROR] Found incorrect number of matches for A");

    System.out.println(test);
    if (test.toString().equals("R___R___")) System.out.println("[OK] Correct clue after R and A");
    else System.err.println("[ERROR] Incorrect clue after R and A");

    response=test.reveal('L');
    if(response.size()==2) System.out.println("[OK] Found correct number of matches for L");
    else System.err.println("[ERROR] Found incorrect number of matches for L");

    System.out.println(test);
    if (test.toString().equals("R___R_LL")) System.out.println("[OK] Correct clue after R,A, and L");
    else System.err.println("[ERROR] Incorrect clue after R,A, and L");

```

## 2. lépés: karakteres játék
Készítsen `HangmanGame` osztályt, mely egy akasztófa játékot valósít meg.

Az osztálynak legyen egy olyan konstruktora, mely első paraméterként a kitalálandó szót várja, második paraméterként pedig azt, hogy hányadik rossz tippnél érjen véget a játék.

Legyen az osztálynak egy `ArrayList<Integer> guess(char character)` függvénye, mely térjen vissza `null`-lal, ha a játék már véget ért. Egyébként tlrjen vissza a megadott karakter előfordulási indexeivel, és ha ilyen nem volt, akkor rögzítsen egy rossz tippet.

Legyen az osztálynak felüldefiniálva a `toString` metódusa, úgy, hogy egyrészt kiírja a szót az aktuálisan ismert változatában, valamint valamilyen formában azt is, hogy hány rossz tippünk volt eddig, és még mennyit ronthatunk.

Legyen az osztálynak egy `isGameOver` és egy `isWon` függvénye is, melyek egyszerűen azt adják vissza, hogy elvesztettük / megnyertük-e már a játékot.

Egy lehetséges tesztelő függvény:

``` java
    System.out.print("Give me a word to guess: ");
    Scanner sc=new Scanner(System.in);
    HangmanGame game=new HangmanGame(sc.next(), 5);
    while(!game.isGameOver() && !game.isWon()){
      System.out.println(game);
      System.out.print("Give me a guess: ");
      if(game.guess(sc.next().charAt(0)).size()>0) System.out.println("Lucky guess!");
      else System.out.println("Too bad, that character does not appear in the hidden word.");
    }
    if(game.isWon()) {
      System.out.println(game);
      System.out.println("Congratulations, you won the game!");
    } else System.out.println("You are hanged. 💀 💀 💀 💀 💀 ");
    sc.close();
```

Amivel így néz ki egy példajáték:

```
Give me a word to guess: Yeppeeeeee
__________ ♥ ♥ ♥ ♥ ♥ 
Give me a guess: E
Lucky guess!
_E__EEEEEE ♥ ♥ ♥ ♥ ♥ 
Give me a guess: A
Too bad, that character does not appear in the hidden word.
_E__EEEEEE 💀 ♥ ♥ ♥ ♥ 
Give me a guess: B
Too bad, that character does not appear in the hidden word.
_E__EEEEEE 💀 💀 ♥ ♥ ♥ 
Give me a guess: C
Too bad, that character does not appear in the hidden word.
_E__EEEEEE 💀 💀 💀 ♥ ♥ 
Give me a guess: P
Lucky guess!
_EPPEEEEEE 💀 💀 💀 ♥ ♥ 
Give me a guess: Y
Lucky guess!
YEPPEEEEEE 💀 💀 💀 ♥ ♥ 
Congratulations, you won the game!

```

## 3. lépés: grafikus játék
Valósítson meg egy egyszerű grafikus felületet, amelyen ezt a játékot lehet futtatni.
 - A felületen valahogy jelenjen meg a játék helyzete, 
 - Valahogy lehessen megadni, hogy melyik betűt tippelnénk következőnek
 - Ha így vagy úgy véget ér a játék, akkor azt valahogy tudassa a program

## Plusz kiegészítő lehetőségek
 - A `HiddenWord` konstruktorának lehessen megadni olyan bemenetet is, mely tartalmaz szóközt, és egyéb írásjeleket. Amelyik karakter nem betű, az automatikusan legyen felfedve.
 - A grafikus felületen minden karakternek saját gombja legyen.
 - A karakteres / grafikus felület valahogy tartsa számon, hogy melyik karaktereket próbáltuk már, és ha a guess függvény ilyennel van meghívva, akkor ne történjen semmi. Illetve ez az információ jelenjen is meg valahol valahogyan a felhasználó számára.
