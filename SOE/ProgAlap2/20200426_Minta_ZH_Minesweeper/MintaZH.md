# Minta ZH feladat Programozás Alapjai 2 tárgyhoz
Az elkészítendő program áll egy alap részből, melynek maradéktalan teljesítése szükséges az alíárás megszerzéséhez.
Ezen felül adottak plusz feladatok, melyek teljesítésével plusz pontok szerezhetők, amit pozitív irányban figyelembe veszünk a félév értékelése során.

A szükséges szintet az egyszerűbb elkészítés és ellenőrzés céljából több lépsrebontottuk. Javasoljuk, hogy mindenki ezeken a lépéseken menjen végig sorrendben.

## 0. lépés: "irodalmazás"
A ZH témája egy aknakereső(féle) játék elkészítése. Aki nem ismeri, először játszon vele pár kört  :-) 
A cél játék annyiban fog különbözni, hogy a pálya mérete fix, nem lehet jelölőket letenni, és nincs a 0 szomszédú mezők automatikus felderítése.

## 1. lépés: háttérlogika
Készítsünk egy `Minefield` nevű osztályt, ami egy 5x5-ös aknamezőt modellez le. 
Ennek az osztálynak legyen:
 - egy egész számot váró konstruktora, mely az aknák számát jelenti, amiket véletlen helyekre letesz.
 - egy `int neighbourMineCount(int x, int y)` függvénye, mely megmondja, hogy egy mező szomszédságában hány akna található.

 Ez utóbbi függvény dobjon egy `BummException` kivételt, ha aknás mezőre kérdeztünk rá.
 Az indexekről feltételezhetjük, hogy helyesek, azaz a 1-5 egészek.

 A könnyebb tesztelés érdekében a konstruktor az standard error streamre írja ki, hol vannak a bombák. 

## 2. lépés: karakteres játék
Készítsen egy `MineSweeperGame` osztályt, melynek a konstruktora inicializál egy 5x5-ös aknakereső játékot a megadott bombaszámmal.
Ez az osztály az előzőhöz képest számontartja, miket tippeltünk eddig, illetve, hogy megnyertük-e a játékot már.
Egy `reset(int minecount)` függvény segítségével a játék állapota resetelődik, a bombák újra leosztódnak, és minden indul előröl.
Az `int check(int x, int y)` függvény hasonlóan működik a fenti `neighbourMineCount` függvényhez, de ha bombára léptünk reseteli a játékot, és visszatér 9-cel. Ha nem léptünk bombára, akkor feljegyzi a lépésünket. (Ha kétszer lépünk ugyanoda, abból nincs semmi baj, de igazából nem történik semmi.)
A `boolean isCleared()` függvény `true`-val tér vissza, ha már minden bombamentes mezőre tippeltünk.
Végezetül a `void printState()` valami egyszerű formában jelenítse meg a játék állapotát a standard kimeneten, pl:
```
 |1|2|3|4|5|
-+-+-+-+-+-+
1| | | |1| |
-+-+-+-+-+-+
2| | | |1|1|
-+-+-+-+-+-+
3| | | |0|0|
-+-+-+-+-+-+
4| | | | |2|
-+-+-+-+-+-+
5| | | | | |
-+-+-+-+-+-+
```
vagy akár a fenti helyett csak:
```
???1?
???11
???00
????2
?????
```
Ezek után az alábbi main-nel már kényelmesen lehet játszani, és tesztelni a programot:
```
public static void main(String[] args) {
    MineSweeperGame game=new MineSweeperGame(5); // 5 aknat tesz le az 5x5-os palyara
    Scanner sc=new Scanner(System.in);
    int x, y;
    boolean newGame=true;
    while(!game.isCleared() && newGame){
        x=sc.nextInt();
        y=sc.nextInt();
        if(game.check(x,y)==9){
            System.out.print("Time to listen to Astronomia from Tony Igy. Wanna play another game?");
            if(sc.next().matches("[nN]o")) newGame=false;
        } else {
            game.print();
        }
    }
    if(game.isCleared()){
        System.out.println("Congrats, and thanks for playing!");
    } else {
        System.out.println("Maybe next time, bb.");
    }   
}
```
## 3. lépés: grafikus játék
Valósítson meg egy egyszerű grafikus felületet, amelyen aknakeresőt lehet játszani:
 - A felületen legyen 5x5 nyomógomb, amiken egy `?` van kezdetben.
 - Amikor megnyomjuk valamelyik gobbot, akkor rálépünk a mezőre. 
    - Ha akna volt rajta, akkor dobjon fel egy felugró ablakban egy kérdést, hogy szeretnénk-e újra játszani. Ha nem, lépjen ki a program. Ha igen, akkor legyen újra minden gomb alaphelyzetben.
    - Ha nem volt akna, akkor a gomb szövege cserélődjön le arra, hány szomszédján van akna, és többet ne lehessen rá kattintani.
 - Minden kattintás után ellenőrizzük, hogy végzett-e a játék, és ha igen, akkor dobjon fel egy üzenetet, és kérdezze meg, hogy akarunk-e még játszani?

## Javaslatok, tippek
 - A mezők könnyen megfeleltethetők 0-24 számoknak, ez hasznos lehet pl a random aknalerakázhoz. 
 - Néhány egymástól különböző random egész generálására több módszer van. Ki kell küszöbölni, hogy kétszer legyen ugyanaz. Erre az egyik mód, hogy Set-be pakolunk addig, amig a méret a kívánt nem lesz. Egy másik, hogy egy 0-24 számokkal feltöltött listát összekeverünk, és kivesszük az első pár elemet.
 - a szomszédos aknák számának az ellenőrzése egyszerűbb, ha egy 7x7-es mátrixot tárolunk, aminek a közepe a pálya, így nem kell a kiindexeléstől tartani.
 - Az egyes lépések nyilván épülnek az előzőkre, azért van így felépítve. Ne csináljunk meg semmit újra, próbáljuk használni a korábbi lépések eredményeit. És nem copy-paste módon, hanem kompozícióval, örökléssel, stb, ami a célnak leginkább megfelel.

## Plusz kiegészítő lehetőségek
 - Mind a karakteres, mint a grafikus játék esetében, legyen automatikus 0 felderítés, azaz ha 0-s mezőre tippelünk, akkor Annak automatikusan bejárja a teljes szomszédságát. És mindezt rekurzívan, azaz ha ott is talál 0-ást, akkor erre is vonatkozik ez. (A végtelen ciklus elkerülésére figyeljünk!)
 - A grafikus felületen lehessen beállítani az aknák számát.
 - Az aknamező ne fixen 5x5 legyen, lehessen konstruktorban meghatározni a méretét az aknák számával együtt. 
 - Az előzőre épülve, ezt legyen megvalósítva úgy, hogy a karakteres játék is tudjon tetszőleges méretű pályát kezelni.
 - Az előzőt a grafikus felületre is kiterjeszteni. 
 - Bármilyen egyéb pimpelés, ami eszetekbe jut, és van értelme.
