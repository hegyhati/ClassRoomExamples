# Első objektumorientált implementáció

## Alap csata OO változata

Az előző fejezetben megismert osztályok, objektumok, metódusok pontosan azok az eszközök, amik hiányoztak az RPG játék legutolsó változatánál. 
Ezen új ismeretek birtokában adja magát, hogy lérehozzunk egy `Unit` osztályt, ami a támadás, életpont, védekezés adatok mellett a nevet is tartalmazza:

```java 
class Unit {
    String name;
    int health;
    int damage;
    int defense;
}
```

> [!NOTE]
> Itt most már leírhatjuk, hogy a `String` szintén nem egy primitív típus, mint például az `int` vagy `boolean`, hanem ugyanúgy egy osztály, mint az általunk definiált `Unit`. 

Az előző fejezet végén *hozzátartozónak* ítélt függvények is könnyen tagfüggvénnyé alakíthatók. 
Például az `isAlive` korábbi változatából:

```java
static boolean isAlive(int[] unit) {
    return unit[0] > 0;
}
```

Egy ilyen metódus lett:

```java
class Unit {
    int health;
    ...

    boolean isAlive() {
        return health > 0;
    }
}
```

A későbbi `main` függvényben pedig `isAlive(hero)` helyett `hero.isAlive()` módon lehet ezt a metódust meghívni.

A teljes osztály az `attack` és `getDisplayText` metódusokkal kiegészítve:

```java
class Unit {
    String name;
    int health;
    int damage;
    int defense;

    boolean isAlive() {
        return health > 0;
    }

    void attack(Unit other) {
        int realdamage = damage > other.defense ? damage - other.defense : 0;
        other.health -= realdamage;
        if (other.health < 0) {
            other.health = 0;
        }
    }

    String getDisplayText() {
        return String.format("%s (HP: %d, DMG: %d, DEF:%d)", name, health, damage, defense);
    }
}
```

Ezt követi a korábbi kódból megmaradt `main` és `printStatus`, melyek nem sokat változtak, csupán tömb helyett objektumokat használunk, sima függvények helyett pedig a `Unit` osztály metódusait.

```java
class Main {

    static void printStatus(Unit unit1, Unit unit2) {
        System.out.printf("%s vs. %s\n", unit1.getDisplayText(), unit2.getDisplayText());
    }
   
    public static void main(String[] args) {

        Unit hero = new Unit();
        hero.name = "Hero";
        hero.health = 10;
        hero.damage = 1;
        hero.defense = 1;
        Unit monster = new Unit();
        monster.name = "Monster";
        monster.health = 5;
        monster.damage = 2;
        monster.defense = 0;
        
        printStatus(hero, monster);

        for (int turn = 0; hero.isAlive() && monster.isAlive() ; turn += 1) {
            if (turn % 2 == 0) {
                System.out.printf("%s attacks %s...\n", hero.getDisplayText(), monster.getDisplayText());
                hero.attack(monster);
            } else {
                System.out.printf("%s attacks %s...\n", monster.getDisplayText(), hero.getDisplayText());
                monster.attack(hero);
            }
        }

        if (hero.isAlive()) {
            System.out.println("The hero won the battle \\o/");
        } else {
            System.out.println("The hero lost the battle :-(");
        }
    }
}
```

A teljes kód [itt](src/0100_refactor_with_classes/Main.java) megtalálható. 

> [!NOTE]
> Bár a két osztály egy fájlban van definiálva, vegyük észre, hogy fordításkor elkészül egy `Main.class` és egy `Unit.class` fájl is.

## Egy tisztességesebb `Unit` osztály

A fenti kód bár működőképes, bőven hagy kívánnivalót maga után. 
A legelső dolog, hogy hacsak nem indokolt, egyelőre kövessük azt az ökölszabályt, hogy minden osztályt a saját nevével ellátott fájlban definiáljunk, azaz tegyük át a `Unit` osztályt a `Unit.java` fájlba. 

Ezt követően a legzavaróbb a `main` elején található 10 sornyi kód, ami két objektumunkat létrehozza:

```java
Unit hero = new Unit();
hero.name = "Hero";
hero.health = 10;
hero.damage = 1;
hero.defense = 1;
Unit monster = new Unit();
monster.name = "Monster";
monster.health = 5;
monster.damage = 2;
monster.defense = 0;
```

Ez így érezhetően hosszadalmas, hibaérzékeny, például nem jelez itt, ha valamit netán kihagyunk, és véletlenül a `defense` helyett a `damage`-et adjuk meg kétszer.
Az előző fejezetben tanult eszközök közül a konstruktor volt az, melynek célja, hogy kompakt, fordítási időben ellenőrizhető módon kódolhassuk le egy objektum létrehozását.

> [!NOTE]
> Konstruktor alkalmazásának más előnye is van, erről a `final` használatakor később még lesz szó.

A `Unit` osztályban egy egyszerű konstruktor így néz ki:

```java
Unit(String name_, int health_, int damage_, int defense_) {
    name = name_;
    health = health_;
    damage = damage_;
    defense = defense_;
} 
```

Viszonylag zavarja a szemet a konstruktor argumentumneveinek a végén az alulvonás, de jelen esetben szükséges, hiszen például a `name` azonosító már használt egy belső tagváltozóhoz, így ha az argumentum is `name` lenne, akkor a függvénytörzsben `name = name` szerepelne.
A várakozásoknak ellentmondóan ez a kód teljesen szabályos volna, azonban a szemantikája semmittevő: a konstruktor argumentumának neve *elfedi* a belső tagváltozót, azaz az argumentum értékét saját magára állító utasítást eredményezne a kód. 
A `this` minden esetben az adott objektumra mutató referencia, így még a fenti elfedés esetében is elérhető a saját tagváltozó ezen keresztül:

```java
Unit(String name, int health, int damage, int defense) {
    this.name = name;
    this.health = health;
    this.damage = damage;
    this.defense = defense;
} 
```

> [!TIP]
> Az elkövetkezőkben a `this` kulcsszót mindig kitesszük, még akkor is, ha nem szükséges. 
> Ez a kód olvasása során segít elkülöníteni a metódusok lokális változóit az objektum saját tagváltozóitól. 

> [!NOTE]
> Itt ez most csak konvenció, ahogy ez C++ esetében is lenne például. 
> Egyes nyelveknél (pl.: Python) azonban kötelező a `this` (vagy az annak megfelelő `self`) használata.

Az így elkészült konstruktort használva a `main`-ben a két objektum létrehozása erre a két sorra redukálódik (és akkor már használjuk ki az alkalmat új tesztadatok felvételére):

```java
Unit hero = new Unit("Bilbo", 10, 1, 1);
Unit monster = new Unit("Cavetroll", 40, 5, 0);
```

A következő dolog, amit illik igényesebben, explicitebben megadni, az az egyes adattagok, metódusok láthatósága. 
Jelenleg az alapértelmezett, *package public* láthatóságot használjuk, ami azt jelenti, hogy az azonos csomagban (egyelőre: azonos könyvtárban) lévő fájlok számára elérhető és látható. 
Könnyen elképzelhető, hogy később erre az alap osztályra másik csomagban lévő osztályoknak is szüksége lehet, így célszerű magát az osztályt, és a metódusait publikusra tenni.
Az adattagok esetében azonban más a helyzet.

> [!TIP]
> Egy legtöbbször követendő ökölszabály, hogy minden adattagot, és azokat módosító metódust alapértelmezetten privátra állítsunk, s ezeket csak akkor tegyük publikussá, ha arra feltétlenül szükség van, és más, későbbiekben tárgyalt megoldások nem megfelelőek.
> Ha pedig elgépelésből vagy egyéb hibából fakadóan *véletlenül* próbáljuk elérni az adattagot, akkor a fordítási lépés már jelzi ezt a hibát a helyén, ahelyett, hogy később nehezen felfedezhető, futtatás közben jelentkező szemantikai hibát okozna.

Ezek után a [`Unit.java`](src/0110_constructor_visibility_files/Unit.java) jelenlegi állapota:

```java
class Unit {
    private String name;
    private int health;
    private int damage;
    private int defense;

    public Unit(String name, int health, int damage, int defense) {
        this.name = name;
        this.health = health;
        this.damage = damage;
        this.defense = defense;
    } 

    public boolean isAlive() {
        return this.health > 0;
    }

    public void attack(Unit other) {
        int damage = this.damage > other.defense ? this.damage - other.defense : 0;
        other.health -= damage;
        if (other.health < 0) {
            other.health = 0;
        }
    }
    
    public String getDisplayText() {
        return String.format("%s (HP: %d, DMG: %d, DEF: %d)", this.name, this.health, this.damage, this.defense);
    }
}
```

A [`Main.java`](src/0110_constructor_visibility_files/Main.java)ban a konstruktorhíváson kívül annyi érdemi változás történt, hogy a `printStatus` függvényt privátra állítottuk, hiszen azt máshonnét vélhetően nem akarjuk majd meghívni.
Azt azonban vegyük észre, hogy ebben a fájlban már a kód független(ül értelmezhető) implementációs részletektől. 
A konstruktorhívásokat leszámítva nem lehet a `main` alapján megmondani, hogy most már rendelkeznek a lényeink védekezési értékkel, vagy sem. 
Ilyen értelemben ez a kód már *független* a `Unit` osztály belső viselkedésének részleteitől. 
Ha egy következő fejlesztés során az egész típusú alapadatokat lebegőpontosra cserélnénk, vagy változtatnánk azon, ahogy szövegesen megjelenítjük az adatokat, akkor a `Main.java` fájlon semit nem kellene  változtatni.

A teljesség kedvéért, jelenleg így alakul a csata:
```
Bilbo (HP: 10, DMG: 1, DEF: 1) vs. Cavetroll (HP: 40, DMG: 5, DEF: 0)
Bilbo (HP: 10, DMG: 1, DEF: 1) attacks Cavetroll (HP: 40, DMG: 5, DEF: 0)...
Cavetroll (HP: 39, DMG: 5, DEF: 0) attacks Bilbo (HP: 10, DMG: 1, DEF: 1)...
Bilbo (HP: 6, DMG: 1, DEF: 1) attacks Cavetroll (HP: 39, DMG: 5, DEF: 0)...
Cavetroll (HP: 38, DMG: 5, DEF: 0) attacks Bilbo (HP: 6, DMG: 1, DEF: 1)...
Bilbo (HP: 2, DMG: 1, DEF: 1) attacks Cavetroll (HP: 38, DMG: 5, DEF: 0)...
Cavetroll (HP: 37, DMG: 5, DEF: 0) attacks Bilbo (HP: 2, DMG: 1, DEF: 1)...
The hero lost the battle :-(
```

## `toString` használata

Viszonylag gyakori jelenség, akárcsak tesztelés során is, hogy az objektumainkat valamilyen módon szövegesen meg szeretnénk adni. 
A fenti kódban a `getDisplayText` függvény szerepe pontosan ez, amit a `main`-ben hatszor meg is hívunk.

Szerencsére adott erre Java nyelven egy nagyságrendekkel kényelmesebb megoldás, a `toString` metódus *felülírása*. 
Öröklődésről, függvények felülírásáról későbbi fejezetben lesz szó, addig érjük be annyival, hogyha ezt `getDisplayText` függvényt `toString`-re átnevezzük, eléírunk egy `@Override`-ot, akkor a `main`-ben `hero.getDisplayText()`, illetve `hero.toString()` helyett elegendő csak `hero`-t írni mindenhova, ahol szövegként próbáljuk használni az objektumunkat.

Azaz, a függvény így módosul:

```java
@Override
public String toString() {
    return String.format("%s (HP: %d, DMG: %d, DEF: %d)", this.name, this.health, this.damage, this.defense);
}
```

A `main` csata része pedig így:

```java
for (int turn = 0; hero.isAlive() && monster.isAlive() ; turn += 1) {
    if (turn % 2 == 0) {
        System.out.printf("%s attacks %s...\n", hero, monster);
        hero.attack(monster);
    } else {
        System.out.printf("%s attacks %s...\n", monster, hero);
        monster.attack(hero);
    }
}
```

A kódunk ismét egy fokkal rövidebb, átláthatóbb lett, teljes változat [itt](src/0120_toString/).

## Adattagok elérése, getterek/setterek és a `final`

Ha ránézünk a `Unit` osztály belső adattagjaira, jelenleg mindegyik privát, kívülről egyik sem érhető el direkt módon, amire nincs is szükség a programunkban (jelenleg).
Azonban könnyen elképzelhető, hogy a későbbiekben valahol ki szeretnénk iratni például az egyes lények neveit a zárójeles részletek nélkül, amiket a `toString` most visszaad. 
Vagy az életpontok száma alapján szeretnénk állítani egy csúszka szélességét, stb.
Ennek a megvalósítására több lehetőségünk is van.

Az első, legegyszerűbb mód, ha privát helyett publikusra állítjuk az adattagot.
Ez azonban nemcsak "olvasásra", hanem módosításra is elérhetővé teszi kívülről az adattagot. 
Az ilyet a legtöbb esetben célszerű elkerülni a fentebb már részletezett okokból. 

Egy másik lehetőség, hogy az adattag marad privát, azonban készítünk egy publikus metódust, ami visszaad egy *érték szerinti másolatot* az adattag értékéről. 

Ilyen függvények lehetnének:

```java

private String name;
private int health

public String getName() {
    return this.name;
}

public int getHealth() {
    return this.health;
}
```

> [!CAUTION]
> Ha nem úgynevezett *immutable* vagy primitív típusokat használunk, akkor körültekintően kell eljárnunk, amikor azt egy metódusnak átadjuk, vagy onnét visszaadjuk. 
> Az eddigi változóink közül ilyenek egyedül a tömbök voltak, illetve a saját magunk által készített `Unit` osztály példányai. 
> Később az olyan tárolóknál mint az `ArrayList` és a `HashMap` erre a kérdésre majd részletesebben visszatérünk. 
> Aki nem tudna addig várni, az keressen rá a *pass by value* illetve *pass by reference* kifejezésekre.

Az ilyen függvényeket szokás *getter*eknek hívni, a kódszerkesztők gyakran képesek ezeket automatikusan generálni a belső adattagokhoz. 
Az ilyen függvények alkalmazásának a további előnye a szimpla publikussá tételhez képest, hogy függetleníti az objektum belső *állapotának* megvalósítását, és azt, ahogy kívülről *használják* magát az objektumot. 

Példaképp, ha egy későbbi fejlesztés során a karakterünk kiérdemelhet mindenféle címeket, akkor a többi kód módosítása nélkül meg tudjuk tenni a következőt:

```java

private String name;
private String title = "";

public String getName() {
    return this.title == "" ? this.name : this.title + " " + this.name;
}
```

Ha simán publikus lett volna a `name` akkor vagy abban kellene a címet is eltárolnunk, és akkor gondban vagyunk, ha titulus nélküli névre van szükség, vagy be kellene vezetni egy új módot, ahogy a kódban el lehet érni a nevet, viszont akkor minden használatát a `name`-nek végig kellene ellenőrizni.


Egy fontos következő kérdés, ami felmerül, hogy akarjuk-e a későbbiekben ennek az adattagnak az értékét változtatni. 
Ha a `Unit` osztályunkat megtekintjük, jelenleg nem változik a név, a támadás, a védekezés, csak az életerő. 
Ezek közül ha előrenézünk, várhatóan szintlépésekkel változni fog a támadás, védekezés, azonban a név valószínűleg nem. 
A legtöbb nyelv nyújt valamilyen támogatást annak jelzésére, hogy egy belső adattagot nem akarunk változtatni az objektum élete során azután, hogy értéket kapott a konstruktorban. 
Java nyelven erre a `final` kulcsszó szolgál:

```java
private final String name;
```

Ez esetben a `name` adattagnak a konstruktorban továbbra is adhatunk értéket, az eddigi kód megfelelően működik, de másik tagfüggvényekben ha módosítani (egészen pontosan új értéket adni neki) szeretnénk, akkor a fordító hibát fog jelezni.
Például ha a név cserélésre készítenénk egy ilyet:

```java
public void changeName(String newName) {
    this.name = newName;
}
```

Akkor ezt a hibaüzenetet kapnánk:

```
Unit.java:15: error: cannot assign a value to final variable name
        this.name = newName;
            ^
1 error
```

> [!NOTE]
> A `final` kulcsszónak lesz további szerepe is, ezt majd az öröklődéssel foglalkozó fejezetben fogjuk taglalni.


> [!CAUTION]
> A *mutable* típusok (például tömbök, saját `Unit` objektumok, korábban említett `ArrayList` és a `HashMap`) esetében ismét körültekintőnek kell majd lennünk, és letisztázni a különbséget az *új érték adása* (*reasignment*) és a *módosítás* (*mutation*) között.  
> Erre is később térünk vissza, az eddig megismert többi típusnál a `final` a leírtak szerint működik.

> [!TIP]
> Amiről látszódik egyértelműen, hogy változni fog, azt felesleges `final`lé tenni, azonban ha már kérdéses, mindenképpen érdemes. 
> Könnyebb később *lazítani*, ha valahol tényleg azt látjuk, hogy szükséges a módosítás, addig pedig segít kivédeni emberi tévesztésből fakadó hibákat. 

Ha azonban egy adattag `final`, nem kell attól tartanunk, hogy kívülről kéretlenül módosítják, ezért bátrabban tehetjük meg publikus adattagnak. 
Jelen esetben a `name` ilyen, és akkor nem kell `monster.getName()`-ként elérni, elég `monster.name`-ként. 
Fontos különbség azonban, hogy ebben az esetben a változó nevét sem szabad / érdemes módosítani a továbbiakban, hiszen akkor mindenhol máshol is át kell írni. 
Bár ezt a legtöbb modern kódszerkesztő támogatja, inkább kerüljük.

Mi történik viszont akkor, ha szeretnénk, hogy módosuljon később az adattag? 
Ebben az esetben nyilván nem lesz `final`, és a következő kérdés ami felmerül, hogy csak *belülről* (az objektum tagfüggvényei) szeretnénk ha módosítható maradna, vagy kívülről is.
Szituációnként változik, hogy melyik helyzet áll fenn. 
Jelen esetben egyik adattag sem tűnik olyannak, amelyiknek a külső módosítását logikus volna (egyelőre) megengedni.
Tegyük fel azonban, hogy a korábban említett cím olyan, amit valamilyen játéklogika fog adni, attól függően, hogy milyen küldetéseket teljesítettünk. 
Például: kezdetben nincs ilyenünk, de ha a trollbarlang küldetést teljesítjük, akkor megkapjuk a *slayer of Trolls* kitüntetést, mely után a hivatalos nevünk "Bilbo, the slayer of Trolls" lesz.
A titulushoz ez esetben kell egy *setter*, ami beállítja ezt az adatot:

```java

public final String name;
private String title = "";

public String getOfficialName() {
    return this.title.equals("") ? this.name : this.name + ", the " + this.title;
}

public void setTitle(String newTitle) {
    this.title = newTitle;
}
```

Felvetődhet az a kérdés, hogy ha valamihez van *setter* és *getter* is, akkor miért nem tesszük szimplán publikussá az adattagot.
Legtöbb esetben ez ellenjavallt, mivel a sima publikussággal ellentétben egy setter ad kontrollra lehetőséget. 
Ha például lenne `setHealth` függvényünk, akkor egy szimpla értékbeállítás helyett, mellett megjelenhetne az a logika, hogy 0 alá nem megyünk:

```java
public void setHealth(int newHealth) {
    this.health = newHealth < 0 ? 0 : newHealth;
}
```

De felhasználhatjuk a függvényt naplózásra is, vagy bármilyen egyéb logikát is beírhatunk a tényleges értékadás mellett. 
Ha sima publikus adattagunk lenne, akkor ezekre nem lenne lehetőségünk.
Hasonlóképp, ha a belső adatreprezentációt cserélnénk, például nem azt tárolnánk, hogy mennyi életünk van, hanem hány százalékon van az életerőnk a maximumhoz képest, akkor a konvertálást a setterben meg tudjuk tenni anélkül, hogy a külvilág bármit észrevenne. 

Látjuk, hogy sok lehetőségünk van, és tapasztalat, konkrét szituáció adja meg, hogy mikor melyikkel érdemes élni, azonban az esetek nagy részében a következő ökölszabályokat érdemes megfogadni:

> [!TIP]
> - Ami csak lehet, legyen `private`. 
> - Ami csak lehet, legyen `final`.
> - Gettereket ne írjuk meg előre mindet, csak amire tényleg szükség van.
> - Setterek esetében az előző hatványozottan igaz, és figyeljünk arra, hogy ami *belső szabályokat*, *konvenciókat* betartunk, azt ezekben a függvényekben ellenőrizni kell. 

Nem betartva minden fenti javaslatot, annak érdekében, hogy mindenre legyen példa, a `Unit` osztályunk így módosul:

```java
class Unit {
    private String title = "";
    final public String name;
    private int health;
    final private int damage;
    final private int defense;

    public Unit(String name, int health, int damage, int defense) {
        this.name = name;
        this.health = health;
        this.damage = damage;
        this.defense = defense;
    } 

    public void setTitle(String newTitle) {
        this.title = newTitle;
    }

    public String getOfficialName() {
        return this.title.equals("") ? this.name : this.name + ", the " + this.title;
    }

    public int getHealth() {
        return this.health;
    }

    ...
}
```



A `main` végén is ejtsünk meg egy kis módosítást, hogy néhányat ezek közül használjunk:

```java
    if (hero.isAlive()) {
        hero.setTitle("slayer of trolls");
        System.out.printf("%s won the battle, and should be called henceforth as %s.", hero.name, hero.getOfficialName());
    } else {
        System.out.printf("The hero lost the battle :-(");
    }
```

A teljes kód [itt](src/0130_final/) érhető el.


# Szintlépés logika

Minden tisztességes RPG játékban a játékos karaktere szinteket lép a túlélt csaták után, amitől erősebb lesz. 
Ennek valami nagyon primitív változatát tegyük bele a programunkba:
 - minden ütés után kapunk 1 XP-t (experience point, tapasztalatpont)
 - minden összegyűjtött 10 XP után szintet lépünk, aminek hatására:
   * megnő a támadásunk 1-gyel
   * megnő a védekezésünk 1-gyel
   * az életerőnk a másfélszeresére nő.

Ehhez nem kell mást tennünk, mint bevezetni egy új adattagot, amit minden támadáskor növelünk, és ha 10-el osztható, akkor kell elvégezni a fent írt módosításokat, amit logikusan egy privát `levelUp` függvénybe kiszervezhetünk:

```java

    public void attack(Unit other) {
        ...
        this.experience++;
        if (this.experience % 10 == 0) this.levelUp();
    }

    private void levelUp() {
        this.damage++;
        this.defense++;
        this.health *= 1.5;
    }
```

Fordításkor viszont az alábbi hibát kapjuk:

```
Unit.java:43: error: cannot assign a value to final variable damage
        this.damage++;
            ^
Unit.java:44: error: cannot assign a value to final variable defense
        this.defense++;
            ^
2 errors
```

Vagyis a `damage` és a `defense` adattagok értékét nem szabad módosítanunk, hiszen `final`-ökké tettük őket. 
Ez egy teljesen természetes jelenség, idővel a szoftverek követelményei változnak, most eljött az idő, hogy eldöntsük, valóban szükség van-e ezek módosítására. 
Mivel a szintlépés logika alapja, hogy változnak a tulajdonságaink, ezért egyértelműen igen, itt nem csak egy programozási hibából fakadóan akarunk módosítani.

> [!NOTE]
> Ha nagyon-nagyon akarnánk, természetesen megoldhatnánk a dolgot úgy is, hogy bevezetünk egy nem `final` változót, mely a lépett szintek számát tárolja, és csak azt növeljük.
> Amikor pedig a sebzést, védekezést kell kiszámolni, akkor ezt is hozzáadjuk az alap értékekhez. 
> Bár technikailag jó megoldás, feleslegesen körülményes, és logikátlan.

Indokolt tehát kitörölni a két `final`-t, és akkor már le is fordul a kód.


Futtatás előtt még pár gyors változtatást megejtünk: a korábbi vállalásnak megfelelően a tagváltozók elé továbbra is kitesszük a `this`-t az egyértelműsítés kedvéért. 
Mivel metódusok esetében nem áll fenn semmilyen összetévesztésnek a lehetősége, ezért `this.levelUp()` helyett megfelelő lesz simán a `levelUp()` is. 

> [!NOTE]
> Java esetében nem fordulhatnak elő "önálló" függvények, amikkel ilyenkor összekeverhető lenne egy hívás. 
> Más nyelveken, például C++-ban viszont ez előfordulhat, és ekkor egy `functionName(...)` meghívásból nem lehet tudni, hogy az az aktuális objektumnak egy metódusa, vagy egy külső önálló függvény. 
> Rosszabb esetben mindkettő létezik, az egyikre gondolunk, hogy meghívódik (külső), de valójában a másik (tagfüggvény).
> Pythonban például szintén előfordulhatnak ilyen önálló függvények, azonban ott a `self` használata metódushíváskor is kötelező.

Végezetül növelünk egy kicsit az életerőkön, hogy tesztelés során eljussunk a szintlépésig.

```
Bilbo (HP: 80, DMG: 1, DEF: 1) vs. Cavetroll (HP: 100, DMG: 5, DEF: 0)
Bilbo (HP: 80, DMG: 1, DEF: 1) attacks Cavetroll (HP: 100, DMG: 5, DEF: 0)...
Cavetroll (HP: 99, DMG: 5, DEF: 0) attacks Bilbo (HP: 80, DMG: 1, DEF: 1)...

...

Bilbo (HP: 48, DMG: 1, DEF: 1) attacks Cavetroll (HP: 92, DMG: 5, DEF: 0)...
Cavetroll (HP: 91, DMG: 5, DEF: 0) attacks Bilbo (HP: 48, DMG: 1, DEF: 1)...
Bilbo (HP: 44, DMG: 1, DEF: 1) attacks Cavetroll (HP: 91, DMG: 5, DEF: 0)...
Cavetroll (HP: 90, DMG: 5, DEF: 0) attacks Bilbo (HP: 66, DMG: 2, DEF: 2)...
Bilbo (HP: 63, DMG: 2, DEF: 2) attacks Cavetroll (HP: 135, DMG: 6, DEF: 1)...
Cavetroll (HP: 134, DMG: 6, DEF: 1) attacks Bilbo (HP: 63, DMG: 2, DEF: 2)...
Bilbo (HP: 59, DMG: 2, DEF: 2) attacks Cavetroll (HP: 134, DMG: 6, DEF: 1)...
Cavetroll (HP: 133, DMG: 6, DEF: 1) attacks Bilbo (HP: 59, DMG: 2, DEF: 2)...

...

Bilbo (HP: 5, DMG: 3, DEF: 3) attacks Cavetroll (HP: 179, DMG: 7, DEF: 2)...
Cavetroll (HP: 178, DMG: 7, DEF: 2) attacks Bilbo (HP: 5, DMG: 3, DEF: 3)...
Bilbo (HP: 1, DMG: 3, DEF: 3) attacks Cavetroll (HP: 178, DMG: 7, DEF: 2)...
Cavetroll (HP: 177, DMG: 7, DEF: 2) attacks Bilbo (HP: 1, DMG: 4, DEF: 4)...
The hero lost the battle :-(
```

A középső részletben látszódik, hogy Bilbo adatai megnőttek, működik rendben a szintlépés. 
Kiíratást tehettünk volna a szintlépéses függvénybe, de nem volna szép ha a háttérlogika a kimenetre írna, el tudjuk képzelni, hogy a későbbiekben ez kellemetlen *side effect* lenne.
Viszont azt látjuk, hogy tapasztalatot később lehet mással is szerezhet majd Bilbo, ezért érdemes akár ezt a részt is külön függvénybe kiszervezni:

```java
    public void attack(Unit other) {
        ...
        gainExperience();
    }

    private void gainExperience() {
        this.experience++;
        if (this.experience % 10 == 0) levelUp();
    }
```

A kód jelenlegi változata teljességében [itt](src/0140_levelup/) érhető el. 

## Csak Bilbo lepjen szintet

Ha jobban megnézzük a legutolsó kimenetet, egy kis turpisságot észrevehetünk: nem csak Bilbo, hanem a barlangi troll is szintet lép. 
Ez természetesen nem volt cél, de mivel mindketten ugyanannak a `Unit` osztálynak a példányai, ezért ugyanazok a szabályok vonatkoznak rájuk jelenleg.
De ha már itt tartunk, valószínűleg titulusok szerzésére sem kellene alkalmasnak lennie a trollnak. 
A jelenleg ismert eszközeinkkel több megoldás is kínálkozik.

### Típus megjegyzése

Az egyik legkézenfekvőbb megoldás, hogy egy logikai változóban eltároljuk, hős-e az adott objektum, és bizonyos funkciók csak akkor érhetők el, ha igen.
A lényegi sorok:

```java
class Unit {
    private final boolean  hero;
    ...

    public Unit(String name, int health, int damage, int defense, boolean hero) {
        ...
        this.hero = hero;
    } 

    public void setTitle(String newTitle) {
        if (this.hero) this.title = newTitle;
    }
    
    ...

    public void attack(Unit other) {
        ...
        if (this.hero) gainExperience();
    }

    ...
}
```

Ezek után a `Main`-nen így hozzuk létre a két objektumot:

```java
    Unit hero = new Unit("Bilbo", 80, 1, 1, true);
    Unit monster = new Unit("Cavetroll", 100, 5, 0, false);
```

Futtatva a programot, örömmel tapasztaljuk, hogy Bilbo a csata közben háromszor is szintet lép, és ezúttal győzedelmeskedik:

```
Bilbo (HP: 80, DMG: 1, DEF: 1) vs. Cavetroll (HP: 100, DMG: 5, DEF: 0)
Bilbo (HP: 80, DMG: 1, DEF: 1) attacks Cavetroll (HP: 100, DMG: 5, DEF: 0)...
Cavetroll (HP: 99, DMG: 5, DEF: 0) attacks Bilbo (HP: 80, DMG: 1, DEF: 1)...
Bilbo (HP: 76, DMG: 1, DEF: 1) attacks Cavetroll (HP: 99, DMG: 5, DEF: 0)...
Cavetroll (HP: 98, DMG: 5, DEF: 0) attacks Bilbo (HP: 76, DMG: 1, DEF: 1)...

...

Bilbo (HP: 44, DMG: 4, DEF: 4) attacks Cavetroll (HP: 16, DMG: 5, DEF: 0)...
Cavetroll (HP: 12, DMG: 5, DEF: 0) attacks Bilbo (HP: 44, DMG: 4, DEF: 4)...
Bilbo (HP: 43, DMG: 4, DEF: 4) attacks Cavetroll (HP: 12, DMG: 5, DEF: 0)...
Cavetroll (HP: 8, DMG: 5, DEF: 0) attacks Bilbo (HP: 43, DMG: 4, DEF: 4)...
Bilbo (HP: 42, DMG: 4, DEF: 4) attacks Cavetroll (HP: 8, DMG: 5, DEF: 0)...
Cavetroll (HP: 4, DMG: 5, DEF: 0) attacks Bilbo (HP: 42, DMG: 4, DEF: 4)...
Bilbo (HP: 41, DMG: 4, DEF: 4) attacks Cavetroll (HP: 4, DMG: 5, DEF: 0)...
Bilbo won the battle, and should be called henceforth as Bilbo, the slayer of trolls.
```

Bár a programunk most már helyesen működik, ennek a megoldásnak több hátulütőjét láthatjuk:
 - Magukat a függvényeket a szörnyek számára nem tiltottuk le, így azok továbbra is ott vannak, csak nem csinálnak semmit.
 - Most még átláttuk, hogy elég volt az `attack` metódusban egy `if (this.hero)` *guard* mögé tenni a `gainExperience()` hívást, abban, illetve a `levelUp` függvényben nincs hasonlóra szükség. 
   De mi történik, ha később máshonnét is szerezne tapasztalatot a hős, és ott lefelejtjuk? 
 - Hogy fogjuk lekezelni, ha nem csak hős és szörny lesz, hanem másfajta egységek is? Még több boolean, és majd ezeknek megfelelően `if (this.hero || this.mercenary)` feltételek?
  
Érezzük, hogy ez a megoldás (teljes kód [itt](src/0150_Hero_Monster/)) nem a legjobb, induljunk el egy másik úton.


### Osztályok szétszedése

Hasonlóan egyszerű megoldás, ha készítünk egy hős és egy szörny osztályt, és mindkettőbe csak azt tesszük bele, ami szükséges.
A mostani `Unit`-ból `Hero` lesz, és egy szűkített változata lesz a `Monster`.

A `Hero`-ban megmaradt adattagok, függvények:

```java
class Hero {
    private String title = "";
    final public String name;
    private int health;
    private int damage;
    private int defense;
    private int experience = 0;

    public Hero(String name, int health, int damage, int defense) {...} 

    public void setTitle(String newTitle) {...}

    public String getOfficialName() {...}

    public int getHealth() {...}

    public boolean isAlive() {...}

    public void attack(Monster monster) {...}

    private void gainExperience() {...}

    private void levelUp() {...}
    
    @Override
    public String toString() {...}
}
```

És ugyanezek a `Monster` osztályra:

```java
class Monster {
    final public String name;
    private int health;
    private final int damage;
    private final int defense;

    public Monster(String name, int health, int damage, int defense) {...} 

    public int getHealth() {...}

    public boolean isAlive() {...}

    public void attack(Hero hero) {...}
    
    @Override
    public String toString() {...}
}
```

A `Main`-ben pedig így hozzuk létre a két objektumot:


```java
    Hero hero = new Hero("Bilbo", 80, 1, 1);
    Monster monster = new Monster("Cavetroll", 100, 5, 0);
```

A teljes kód [itt](src/0160_Hero_Monster_2/) érhető el.
Ha fordítani próbáljuk, akkor azonban több hibaüzenetet is kapunk:

```
Main.java:4: error: cannot find symbol
    private static void printStatus(Unit unit1, Unit unit2) {
                                    ^
  symbol:   class Unit
  location: class Main
Main.java:4: error: cannot find symbol
    private static void printStatus(Unit unit1, Unit unit2) {
                                                ^
  symbol:   class Unit
  location: class Main
Hero.java:33: error: defense has private access in Monster
        int damage = this.damage > monster.defense ? this.damage - monster.defense : 0;
                                          ^
Hero.java:33: error: defense has private access in Monster
        int damage = this.damage > monster.defense ? this.damage - monster.defense : 0;
                                                                          ^
Hero.java:34: error: health has private access in Monster
        monster.health -= damage;
               ^
Hero.java:35: error: health has private access in Monster
        if (monster.health < 0) {
                   ^
Hero.java:36: error: health has private access in Monster
            monster.health = 0;
                   ^
Monster.java:23: error: defense has private access in Hero
        int damage = this.damage > hero.defense ? this.damage - hero.defense : 0;
                                       ^
Monster.java:23: error: defense has private access in Hero
        int damage = this.damage > hero.defense ? this.damage - hero.defense : 0;
                                                                    ^
Monster.java:24: error: health has private access in Hero
        hero.health -= damage;
            ^
Monster.java:25: error: health has private access in Hero
        if (hero.health < 0) {
                ^
Monster.java:26: error: health has private access in Hero
            hero.health = 0;
                ^
12 errors
```

Lényegében kettő problémába ütközünk. Az első, hogy a `Main`-ben a `printStatus` továbbra is a nem létező `Unit`-okat várja. 
Mivel ezt már csak egyszer használjuk, a tartalmát fájdalommentesen átemelhetjük a `main` függvénybe.

A másik probléma már keményebb dió, hiszen a két osztály egymás `private` adatait nem tudja elérni.
Természetesen megoldás volna mindent `public`-ra tenni, de az szembemenne a korábban leírtakkal.
Ezt most a legegyszerűbben úgy oldhatjuk fel, ha készítünk egy `takeDamage` függvényt, publikusan, és az `attack` ezt hivja meg a támadási értékével.
Ez az átszervezés később is jól fog még jönni, amikor lesznek még mágikus, elementális, és egyéb támadások is.

A `Hero` osztályban így néz ki az `attack` és a `takeDamage` metódus:

```java
    public void attack(Monster monster) {
        monster.takeDamage(this.damage);
        gainExperience();
    }

    public void takeDamage(int damage) {
        damage -= this.defense;
        if (damage > 0) {
            this.health -= damage;
            if (this.health < 0) this.health = 0;
        }
    }
```

Ezek után fordul a [kód](/src/0161_Hero_Monster_2/) és helyesen is működik.
Az előző megoldásnál felhozott problémák sajnos itt is igazak, azaz macerásnak tűnik, ha megjelenik majd még 2-3 különböző lénytípus, esetleg egy viselkedés, ami ezek közül kettőnél kell majd, stb.

Viszont az sem nagyon szép, hogy ugyanazt a kódot ismételjük a két osztályban.
További probléma, hogy a `Hero` most tud `Monster`-t sebezni, és viszont, de ha lesz 5 féle típus, akkor minden viszonylatban definiálni kell majd ezeket a függvényeket. 

### Közös belső osztály

Az előző megoldásnak egyfajta továbbfejlesztése, ha a közös dolgokat meghagyjuk a `Unit` osztályban, a `Hero` és a `Monster` esetében pedig definiálunk egy privát belső adattagot ezzel a típussal. 

A teljes kód [itt](src/0170_Hero_Monster_3/) érhető el, de a `Hero` osztályban látszódik legjobban a lényeg.

A konstruktorban az említett `base` inicializálódik:

```java
class Hero {
    private Unit base;
    private String title = "";
    private int experience = 0;

    public Hero(String name, int health, int damage, int defense) {
        this.base = new Unit(name, health, damage, defense);
    } 
    ...
}
```

A metódusok egy része nem csinál mást, mint ennek a `base`-nek *továbbdobja* a hívást:

```java
    public int getHealth() { return this.base.getHealth(); }
    public boolean isAlive() { return this.base.isAlive(); }
    public void takeDamage(int damage) { this.base.takeDamage(damage); }
    @Override
    public String toString() { return this.base.toString(); }
```

Ezek ugyanígy történnek a `Monster` osztályban is. 
A `Hero` osztályban ezután jelennek meg azok a dolgok, amik rá specifikusak:

```java
    public void setTitle(String newTitle) {
        this.title = newTitle;
    }

    public String getOfficialName() {
        return this.title.equals("") ? this.base.name : this.base.name + ", the " + this.title;
    }

    public void attack(Monster monster) {
        monster.takeDamage(this.base.damage);
        gainExperience();
    }

    private void gainExperience() {
        this.experience++;
        if (this.experience % 10 == 0) levelUp();
    }

    private void levelUp() {
        this.base.damage++;
        this.base.defense++;
        this.base.health *= 1.5;
    } 
```

A program helyesen működik, és a kívánt eredményt adja.

> [!NOTE]
> A `Unit` osztály minden adattagját most publikusra tettük, hogy ezzel az eléréssel ne legyen gond.

Ezzel a megoldással elértük azt, hogy a közös függvényeknél csak annak a deklarációját kellett ismételni, magát a logikát nem. 
Tehát ha változtatni szeretnénk mondjuk a `takeDamage` logikán, csak a `Unit` osztályban kell módosítanunk azt, nem kell minden másik osztályban. 
Sőt, egy ilyen `base`-zel rendelkező későbbi osztályban azt is megtehetjük akár, hogy bizonyos függvényeket *elfedünk* és elrejtünk.
Vagy akár szimpla *továbbdobás* helyett összetettebb logikával felülírjuk.

## Konklúzió

Az előző három megoldás példáján okulva érezzük, hogy jó lenne valamilyen nyelvi támogatás arra, hogy:
 - hasonló osztályok közös működési logikát egymással megoszthassanak
 - mindezt duplikálás, vagy felesleges *bloat* sorok igénylése nélkül
 - és jó volna, ha *egy kalap* alatt lehetne kezelni ezeket a típusokat, amikor csak a közös részeket használjuk, hogy ne kelljen bizonyos működést minden típusra, vagy minden típuspárra megírni.
