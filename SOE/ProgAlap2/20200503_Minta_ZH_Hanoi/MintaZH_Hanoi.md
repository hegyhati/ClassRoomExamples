# Minta ZH feladat Programozás Alapjai 2 tárgyhoz
Az elkészítendő program áll egy alap részből, melynek maradéktalan teljesítése szükséges az alíárás megszerzéséhez.
Ezen felül adottak plusz feladatok, melyek teljesítésével plusz pontok szerezhetők, amit pozitív irányban figyelembe veszünk a félév értékelése során.

A szükséges szintet az egyszerűbb elkészítés és ellenőrzés céljából több lépésre bontottuk. Javasoljuk, hogy mindenki ezeken a lépéseken menjen végig sorrendben.

## 0. lépés: "irodalmazás"
A ZH témája egy Hanoi torony "szimulátor" elkészítése. Rekurzív algoritmusok és világvége elmeletek tanulmányozása közben valószínűleg már mindenki találkozott vele, ha netán nem, [itt](https://en.wikipedia.org/wiki/Tower_of_Hanoi) érdemes a lényeget elolvasni.

## 1. lépés: háttérlogika
Készítsünk egy `HanoiTower` nevű osztályt, ami egy ilyen tornyot modellez. 
Ennek az osztálynak legyen:
 - paraméter nélküli konstruktora, ami egy olyan tornyot "épít fel", amin nincsen egyetlen korong sem.
 - egy egész paramátert váró konstruktora, ami annyi darab korongot tesz fel a toronyra szabályosan, melyek mérete 1, 2, stb. 
 - `int pop()` függvénye, mely leveszi a legfelső korongot, és visszaadja annaka  méretét. Ez dobjon egy `EmptyTowerException`-t, amennyiben már nincs korong a tornyon.
 - `void put(int size)` függvénye, mely egy `size` méretű korongot próbál a torony tetejére tenni. Ha nem sikerül, dobjon `InvalidMoveException`-t.

A könnyebb tesztelés és a következő lépés érdekében érdemes megírni a `toString`-et is.

Egy lehetséges egyszerű, nem mindenre kiterjedő tesztelés:

```
HanoiTower test= new HanoiTower();
try{
    test.pop();
    System.err.println("[ERROR] pop succesful from empty tower")
} catch (EmptyTowerException e){
    System.err.println("[OK] pop unsuccesful from empty tower")
}
try{
    test.put(6);
    System.err.println("[OK] put 6 succesful on empty tower")
} catch (InvalidMoveException e){
    System.err.println("[ERROR] put 6 succesful on empty tower")
}
try{
    test.put(4);
    System.err.println("[OK] put 4 succesful on tower [6]")
} catch (InvalidMoveException e){
    System.err.println("[ERROR] put 4 succesful on tower [6]")
}
try{
    test.put(1);
    System.err.println("[OK] put 1 succesful on tower [6 4]")
} catch (InvalidMoveException e){
    System.err.println("[ERROR] put 1 succesful on tower [6 4]")
}
try{
    test.put(2);
    System.err.println("[ERROR] put 2 succesful on tower [6 4 1]")
} catch (InvalidMoveException e){
    System.err.println("[OK] put 1 succesful on tower [6 4 1]")
}
```


## 2. lépés: karakteres szimulátor
Készítsen egy `HanoiSimulator` osztályt, mely a 3 torony helyzetét modellezi le.

Az osztálynak van egy egy egészet váró konstruktora. Ez inicializálja a tornyokat úgy, hogy az összes korong 1-től eddig a számig helyesen az első tornyon van, a másik két torony üres. A "cél" az, hogy a 2-es toronyra kerüljön át az összes korong.

Legyen ehhez egy `boolean isFinished()` függvénye, mely csak akkor tér true-val vissza, ha minden korong a második tornyon van.

Ezen kívül az osztálynak legyen egy `boolean move(int from, int to)` függvénye, mely a `from` torony tetejéről megpróbálja átrakni a legfelső korongot a `to` torony tetejére, valamint visszatér azzal, hogy ez sikeres volt-e.

Legyen az osztálynak felüldefiniálva a `toString` metódusa, ami valamely egyszerű módon kiírja a szimuláció helyzetét, pl:

```
Tower 1 : 5 3 1
Tower 2 : 6 4
Tower 3 : 2
```

Ezek után az alábbi main-nel már kényelmesen lehet szimulálni a rendszert:
```
HanoiSimulator simulator = new HanoiSimulator(4);
Scanner sc=new Scanner(System.in);
while(!simulator.isFinished) {
    System.out.println(simulator);
    System.out.print("Which tower should I take the top disk from? (1-3) ");
    int from = sc.nextInt();
    System.out.print("On which tower should I put it down? (1-3) ");
    int to = sc.nextInt();
    if(simulator.move(from,to)) System.out.println("Move successful.");
    else System.out.println("This move can not be carried out.");
}
System.out.println("Congrats, you win. You've just brought the end of the world. Thanks.... -.-");
```
## 3. lépés: grafikus játék
Valósítson meg egy egyszerű grafikus felületet, amelyen ezt a szimulátort lehet futtatni.
 - A felületen valahogy jelenjen meg a 3 torony helyzete (Pl.: `JList`)
 - Valamilyen módon lehessen megmondani, hogy honnét hova szeretnénk pakolni.
    - Ez lehet két `JField` / `JSpinner` / `JComboBox` és egy `JButton`, vagy 
    - 6 különböző áthelyezés `JButton`, vagy
    - 3 felvevő és 3 lerakó `JButton`, vagy
    - korong kiválasztás a listából, és a mozgatás helye `JRadioButton`-nel kiválasztva, vagy
    - bármi más egyéb
 - Hibás lépés esetén kapjunk egy ejnyebejnye üzenetet.
 - Ha sikerült a játék, akkor valahogyan gratuláljon a program.

## Plusz kiegészítő lehetőségek
 - A karaktereres / grafikus szimulátor a végén azt is írja ki, hogy hány lépésből sikerült megoldani a feladatot.
 - A szimulátor figyelje, hogy milyen állapotokban jártunk, és ha kétszer ugyanabba kerülünk, akkor érjen véget a dolog, nem tudtuk elhozni a világvégét.
 - Legyen egy AI, aminek meg kell adni a méretet, létrehoz egy szimulátort, és végiglépteti azt a szükséges állapotokon a cél eléréséhez.
 - Legyen egy `AdjacentHanoiSimulator` ami csak szomszédos tornyok között enged meg pakolást. A karakteres / grafikus szimulátor legyen úgy módosítva, hogy egyszerűen kicserélhető legyen a kettő, s a program futásának az elején kérdezze meg, melyik változatot szeretnénk szimulálni.
