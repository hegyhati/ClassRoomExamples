# ZH feladat Programozás Alapjai 2 tárgyhoz
Az elkészítendő program áll egy alap részből, melynek maradéktalan teljesítése szükséges az alíárás megszerzéséhez.
Ezen felül adottak plusz feladatok, melyek teljesítésével plusz pontok szerezhetők, amit pozitív irányban figyelembe veszünk a félév értékelése során.

A szükséges szintet az egyszerűbb elkészítés és ellenőrzés céljából több lépésre bontottuk. Javasoljuk, hogy mindenki ezeken a lépéseken menjen végig sorrendben.

## 0. lépés: "irodalmazás"
A ZH témája egy [Domino](https://en.wikipedia.org/wiki/Dominoes) játék elkészítése. Az alap változatban egy irányban kell tudni egy Domino láncot bővíteni.

## 1. lépés: alaposztály
Készítsünk egy `DominoTile` nevű osztályt, ami egy dominót modellez, aminek van dedikáltan egy bal és egy jobb oldali mezője, amelyik mindegyikén 0-6 db pötty lehet.
Ennek az osztálynak legyen egy:
 - paraméter nélküli konstruktora, ami véletlen számú megengedett pöttyöt rak mindkét oldalra
 - legyen egy két egészet váró konstruktora, ami a pöttyök számát adja meg. Ez a konstruktor dobjon egy `InvalidDotNumberException` kivételt, ha a pöttyök száma nem 0 és 6 között van.
 - `void rotate()` függvénye, mely megfordítja a dominót, tehát pl `[3|4]`-ből `[4|3]`-at csinál
 - `boolean canConnectFromLeft(DominoTile other)` függvénye, mely megmondja, hogy az `other` dominóhoz balról hozzáíileszthető-e a dominó. Pl egy `[1|2]` balról hozzáilleszthető egy `[2|3]`-hoz, fordítva azonban ez nem igaz.

A könnyebb tesztelés és a következő lépés érdekében érdemes megírni a `toString`-et is.

Egy lehetséges egyszerű, nem mindenre kiterjedő tesztelés:

```
try {
    DominoTile d11=new DominoTile(1,1);
    System.out.println("[OK] [1|1] domino tile created successfully.");
    try {
        DominoTile d12=new DominoTile(1,2);
        System.out.println("[OK] [1|2] domino tile created successfully.");
        try {
            DominoTile d17=new DominoTile(1,7);
            System.err.println("[ERROR] [1|7] domino tile created successfully.");
        } catch (InvalidDotNumberException e){
            System.out.println("[OK] Domino [1|7] could not be created.");
        }
        if(d11.canConnectFromLeft(d12)) System.out.println("[OK] [1|1] can connect to [1|2]");
        else System.err.println("[ERROR] [1|1] can not connect to [1|2]");
        if(!d12.canConnectFromLeft(d11)) System.out.println("[OK] [1|2] cannot connect to [1|1]");
        else System.err.println("[ERROR] [1|2] can connect to [1|1]");
        d12.rotate();
        if(!d11.canConnectFromLeft(d12)) System.out.println("[OK] [1|1] cannot connect to [2|1]");
        else System.err.println("[ERROR] [1|1] can not connect to [2|1]");
        if(d12.canConnectFromLeft(d11)) System.out.println("[OK] [2|1] ca connect to [1|1]");
        else System.err.println("[ERROR] [2|1] cannot connect to [1|1]");
    } catch (InvalidDotNumberException e){
        System.err.println("[ERROR] Domino [1|2] could not be created.");
    }
} catch (InvalidDotNumberException e){
    System.err.println("[ERROR] Domino [1|1] could not be created.");
}
}
```

## 2. lépés: karakteres játék
Készítsen egy `DominoGame` osztályt, mely a következő játékot szimulálja: a játék kezdetekor kitesz egy random dominót, amivel megkezdi a sort. 
Ezután kipakol 3 random dominót, amik közül eldönthetjük, hogy melyiket szeretnénk balról hozzátenni a sor elejéhez. 
Ha ez lehetséges, akkor hozzáteszi, majd a felhasznált dominó helyére egy új véletlenszerűt tesz ki.

Az osztálynak van egy alapértelmezett konstruktora, mely a fenti inicializáló lépéseket elvégzi. 

Legyen továbbá egy `DominoTile getTileOption(int number)` függvénye, mely visszaadja a 3 lehetséges dominó közül azt, amelyiket a paraméterben kértük. (Nem kell lekezelni, ha nem 1,2, vagy 3 értéket kap.)

Ezen kívül az osztálynak legyen egy `void continueWithOption(int number)` függvénye, mely a megadott dominóval próbálja balról folytatni a sort. Ha nem sikerül, dobjon egy `InvalidMoveException`-t.

Legyen az osztálynak felüldefiniálva a `toString` metódusa, ami valamely egyszerű módon kiírja a játék helyzetét, pl:

```
[1 | 2] [3 | 6] [1 | 4]
    [2 | 3] [6 | 1] [4 | 4]

Option 1 : [1 | 2]
Option 1 : [2 | 2]
Option 1 : [4 | 3]
```

Legyen az osztálynak egy `boolean isGameOver()` függvénye is, ami igazzal tér vissza, ha már sehogy sem lehet tovább lépni.

Ezek után az alábbi main-nel már kényelmesen lehet szimulálni a rendszert:
```
DominoGame game = new DominoGame();
Scanner sc=new Scanner(System.in);
while(!game.isGameOver()) {
    System.out.println(game);
    System.out.print("Which domino should I use? (1-3) ");
    int domino = sc.nextInt();
    try{
        game.continueWithOption(domino);
    } catch (InvalidMoveException e) {
        System.out.println("Domino "+game.getTileOption(domino)+" can not be used to continue.");
    }
}
System.err.println(game);
System.out.println("Game over");
```
## 3. lépés: grafikus játék
Valósítson meg egy egyszerű grafikus felületet, amelyen ezt a játékot lehet futtatni.
 - A felületen valahogy jelenjen meg a játék helyzete, pl:
    - 1 `TextArea`
    - 1 `JList` + 3 db `JLabel`/`JButton`
    - 1 `JLabel` + 3 db `JRadioButton`
    - Ezekhez akár megírható szükségszerűen plusz függvények a `DominoGame` osztályhoz.
 - Valamilyen módon lehessen megmondani, hogy melyik dominóval szeretnénk kiegészíteni
    - 3 db `JButton` Option 1, Option 2, Option 3 felirattal
    - 3 db `JButton` amiken a felirat a dominók maguk
    - `JSpinner` / `JComboBox` /  3 db `JRadioButton` + `JButton`
    - bármi más egyéb
 - Hibás lépés esetén kapjunk egy ejnyebejnye üzenetet.
 - Ha véget a játék, akkor valahogyan tudassa ezt a program.

## Plusz kiegészítő lehetőségek
 - Lehessen a lehetséges dominókat megforgatni is.
 - Lehessen két irányba bővíteni a dominó sort.
 - Legyen paraméterből állítható, hogy hány dominó opció van a játékban (3 helyett bármennyi).
 - Legyen egy  `High_Score.txt` fájl, amiben a 10 legjobb eredmény látszódik. (Ki, mikor, milyen hosszú dominósort tudott építeni.) Ha a játékunkkal erre felkerülnénk, akkor kérjen egy nevet, és frissítse a listát.
 - Ne teljesen random generálódjanak a dominók, hanem legyen egy "pakli", amiben az összes lehetséges pár előfordul,és abból rakja ki az elsőt, illetve az opciókat, amíg a pakli el nem fogy.
