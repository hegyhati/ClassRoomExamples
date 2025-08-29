# Öröklődés

Az öröklődés lényegében megoldja azokat a problémákat, amikbe az előző projektfejezet végén kerültünk.
Hasonlóan az utolsó megvalósításhoz, a közös részek kikerülhetnek a `Unit` osztályba.
Nem olyan körülményes azonban ennek használata a specifikus osztályokban, hiszen a *gyerekek* öröklik az adattagokat és a metódusokat, nincs szükség egy `base` létrehozására, valamint a *továbbdobálásra*.

A `Unit` osztályban egyelőre semmilyen változás nem szükséges, a `Monster` pedig lényegében kiüresedik, hiszen egyelőre semmilyen plusz dolgot nem tesz hozzá az alap `Unit`-hoz:

```java

class Monster extends Unit {

    public Monster(String name, int health, int damage, int defense) {
        super(name, health, damage, defense);
    } 

}
```

A `Hero` már izgalmasabb:

```java
class Hero extends Unit {
    private String title = "";
    private int experience = 0;

    public Hero(String name, int health, int damage, int defense) {
        super(name, health, damage, defense);
    } 

    public void setTitle(String newTitle) {
        this.title = newTitle;
    }

    public String getOfficialName() {
        return this.title.equals("") ? this.name : this.name + ", the " + this.title;
    }

    public void attack(Unit other) {
        other.takeDamage(this.damage);
        gainExperience();
    }

    private void gainExperience() {
        this.experience++;
        if (this.experience % 10 == 0) levelUp();
    }

    private void levelUp() {
        this.damage++;
        this.defense++;
        this.health *= 1.5;
    }    
}
```

Pár dolgot figyeljünk meg:
 - Inicializálni kell azt a részét is az objektumnak, ami az ősosztályhoz (`Unit`) tartozik, ezért a konstruktorban meg kell hívni annak a konstruktorát is, erre használtuk a `super`-t.
 - A közös metódusokat itt sem kell feltüntetni, azokat szimplán örökli a `Unit`-tól a `Hero` ahogy a `Monster` esetében is.
 - Egyszerűsödött az örökölt adattagok elérése a kompozíciós megoldáshoz képest, `this.base.damage` helyett `this.damage`-dzsel elérhető.

Egy további előnye a megoldásnak, hogy az `attack` függvény argumentuma lehet a `Unit` ősosztály. 
Tehát ha a későbbiekben lesznek más származtatott osztályok is, nem lesz szükséges páronként definiálni, engedélyezni ezt a működést.

A teljes kód [itt](src/0200_Inheritance/) érhető el.

## `protected` és `super`

Van azonban némi szépítenivaló a kódban. 
A `Hero` osztály támadási működése eltér az alaptól, amit a `Unit` osztálytól örököl, ezért felülírja az `attack` metódust:

```java
    public void attack(Unit other) {
        other.takeDamage(this.damage);
        gainExperience();
    }
```

Ezért először is illik egy `@Override` megadása.
Ez ismét elsősorban nekünk ad egyfajta biztonságot. 
Az `@Override` megadása nélkül próbáljuk ki, mi történik ha az `attack` függvény nevében "véletlenül" kitörlünk egy betűt, mondjuk például `atack`-ra változtatva azt.

> [!TIP]
> Továbbolvasás előtt próbáld meg végiggondolni, mi lesz ennek az eredménye.

Elsőre talán meglepő módon a program sikeresen lefordul, futás közben sem kapunk hibát, azonban... Bilbo elveszíti a csatát.
Jogosan számíthattunk arra, hogy hibát kapunk, mert `attack` metódust hívunk meg, de nekünk `atack` van. 
Pontosabban, olyan metódusunk **is** van, de `attack` is, hiszen megörököltük azt a `Unit`-tól.
Viszont így sosem hívódik meg a `gainExperience`, Bilbo nem lép szintet, és így nem tudja megnyerni a  csatát.

Tegyük most be (még a hibás nevű függvény elé) az `@Override`-ot, mely részünkről kifejezi a fordító fele azt a szándékunkat, hogy ez nem egy új függvény szeretne lenni, hanem egy már ősosztálytól örököltnek a felülírása.
Kapunk is egy hibaüzenetet fordításkor:

```
Hero.java:17: error: method does not override or implement a method from a supertype
    @Override
    ^
1 error
```

Vagyis keresi a fordító az ősosztályban az azonos paraméterlistával rendelkező `atack` függvényt, de nem találja.
Tehát az `@Override` kitételének az elsődleges előnye számunkra, hogy megvéd a fenti típusú szemantikai hibáktól.
Javítsuk ki a függvénynevet, de még nézegessük egy picit tovább.

A `gainExperience` híváson kívül azt szeretnénk, hogy pontosan úgy működjön ez a metódus, mint bármilyen két `Unit` között, amit jelenleg úgy értünk el, hogy bemásoltuk ide az ősosztálybeli `attack` függvény jelenleg egyetlen sorát. 
Talán látható, hogy ebből gond lehet, ha később ebben a függvényben változtatunk a `Unit` osztályban, de azt elfelejtjük átmásolni a `Hero` vagy más hasonló osztályokba is. 
Éppen ezért itt az ősosztály azonos nevű függvényét szeretnénk inkább meghívni, amit Javaban így tehetünk meg:

```java
    @Override
    public void attack(Unit other) {
        super.attack(other);
        gainExperience();
    }
```

Egy másik csúnyaság, hogy a `Unit` osztályban az adattagok még mindig publikusak, de most már nincs erre szükség. 
Azt továbbra is szeretnénk, hogy `Hero` direktben elérje őket, de kintről nem tűnik ideálisnak, ha bárki beleturkálhat.
Pontosan erre a szituációra létezik a `protected` jogosultsági szint. 

A `damage`, `defense` és `health` mellett a `takeDamage` függvényt is jobb elrejteni a külvilág elől. 
Ha azt látjuk, hogy szükség lesz majd ilyen direkt sebződésre, később publikussá tehető, de egyelőre a lények csak úgy sebződhetnek, ha egymást támadják.

```java
class Unit {
    final public String name;
    protected  int health;
    protected  int damage;
    protected  int defense;

    ...

    protected void takeDamage(int damage) {
        damage -= this.defense;
        if (damage > 0) {
            this.health -= damage;
            if (this.health < 0) this.health = 0;
        }
    }
    
    ...
}
```

A teljes kód [itt](src/0210_Protected_super/) érhető el.
Vegyük észre, hogy a tapasztalatszerzés (azaz a legutolsó új funkció) óta a kódunk hossza csak csökken, illetve kisebb darabokra esik szét. 

## Gyógyítás

Nincs RPG játék anélkül, hogy valamilyen módon a hősünket ne tudnánk gyógyítani. 
Tipikusan van egy maximum életerő, ameddig az aktuális életerőt fel lehet tornázni ételek, gyógyitalok elfogyasztásával, vagy szintlépéssel, speciális tereptárgyak meglátogatásával.

Legyen tehát a következő továbbfejlesztésünk célja ez, azaz:
 - hős esetében legyen megjegyezve a maximális életerő
 - lehessen egy metódussal gyógyítani (ha még él), de a maximum fölé nem mehet
 - lehessen maximumra gyógyítani
 - szintlépéskor a maximum nőjön meg 10-el, és gyógyuljon fel teljesen a hős
  
> [!TIP]
> Próbáld meg ezeket a módosításokat egyedül elvégezni a `Hero` osztályon.
> Ha jól valósítottad meg, ez lesz a végeredmény:
> ```Bilbo (HP: 120, DMG: 5, DEF: 5) won the battle, and should be called henceforth as Bilbo, the slayer of trolls.```

Vegyük észre, hogy csak a `Hero` osztályhoz kell hozzányulnunk, hiszen a szintlépéses logika is csak őt érinti. 
Nem változik se a `Unit` / `Monster`, se a `Main`.

A releváns új részek: 

```java
class Hero extends Unit {
    ...
    private int maxHealth;

    public Hero(String name, int health, int damage, int defense) {
        super(name, health, damage, defense);
        this.maxHealth = health;
    } 

    public void heal(int points) {
        if (isAlive()) {
            this.health += points;
            if (this.health > this.maxHealth) 
                this.health = this.maxHealth;
        }
    }

    public void healToFull() {
        if (isAlive()) this.health = this.maxHealth;
    }

    ...
    
    private void levelUp() {
        this.damage++;
        this.defense++;
        this.maxHealth += 10;
        healToFull();
    }    
}
```

## `title` a helyén

Egy korábbi alkalommal már fejlesztettük úgy a `Hero` osztályunkat, hogy nyerhessen el különböző címeket. 
Ezeket szörnyek legyőzésével lehet megszerezni, ez a logika pedig jelenleg a `Main`-en belül található. 
Sokkal logikusabb volna, ha egy szörny legyőzésekor maga a szörny adná oda ezt a címet a hősnek. 

Ennek a logikája mondjuk legyen az, hogyha egy szörnynek van odaadományozható címe (amit a konstruktorban megkap), akkor miután meghalt, azt odaadhatja valakinek, de csak egyszer.

Ez egyszerűen megoldható az eddigi ismeretek alapján, és most akkor már a `Monster` osztály sem egy üres származtatottja a `Unit`-nak.

```java
class Monster extends Unit {

    private String title;

    public Monster(String name, int health, int damage, int defense, String title) {
        super(name, health, damage, defense);
        this.title = title;
    }

    public String fetchTitle() {
        if ( !isAlive() && this.title != null) {
            String tmp = title;
            this.title = null;
            return tmp;
        } else return null;
    }
}
```

A legtöbb szörny azonban nem osztogat ilyeneket, így hasznos lehet egy `Monster(String name, int health, int damage, int defense)` konstruktor, azonban a Java nem támogat alapértelmezett argumentum értékeket, csak metódus túlterhelést, azaz több azonos nevű függvény létrehozását különböző argumentumokkal. 
Így egy további konstruktort is definiálhatunk, mely a fentit paraméterezi: 

```java
public Monster(String name, int health, int damage, int defense) {
    this(name, health, damage, defense, null);
}
```

Ezután már csak a `Hero` támadását kell módosítanunk, hogy "kérje el" a címet, és vegye fel, amennyiben sikerült legyőzni a szörnyet a legutolsó csapással:

```java
@Override
public void attack(Unit other) {
    super.attack(other);
    gainExperience();
    if (!other.isAlive()) {
        addTitle(other.fetchTitle());
    }
}
```

A címek kezelését is ennek megfelelően kicsit módosítani érdemes, hogy több címet lehessen begyűjteni:

```java 
private void addTitle(String newTitle) {
    if (newTitle != null) this.title += ", the " + newTitle;
}

public String getOfficialName() {
    return this.name + this.title;
}
```

A [`Main`-ből](src/0230_title/Main.java) pedig eltűnhet a címekre vonatkozó logika, hiszen ezt most már egymás közt megoldja a `Hero` és a `Monster`.

Azonban, ha fordítani próbálunk, a következő hibát kapjuk:

```
Hero.java:36: error: cannot find symbol
            addTitle(other.fetchTitle());
                          ^
  symbol:   method fetchTitle()
  location: variable other of type Unit
```

Itt ütközünk abba a hibába, hogy az argumentumban kapott `other` nem `Monster` hanem `Unit` típusú, tehát nincs `fetchTitle()` metódusa. 
Ennek és hasonló problémáknak a feloldására általában több út is lehetséges.
Sokszor nem létezik egyértelműen helyes válasz, a választás elsősorban attól függ, milyen későbbi változások várhatók.
Az ilyen jellegű dilemmákról a későbbi, tervezésre fókuszáló fejezetekben még lesz részletesebben szó.

Az első lehetőség, hogy a metódust felvisszük a `Unit` osztályba, ahol nem csinál semmit, majd a `Monster`-ben felülírjuk. 
Mivel egyáltalán nem várható, hogy később hasonló működést szeretnénk adni hősnek, vagy `NPC`-knek, ezért ez nem igazán követendő.

Egy másik megoldás, hogy az `attack` függvényen belül ellenőrizzük, hogy `Monster`-ről van-e szó, és ha igen, akkor csinálunk ilyet:

```java
@Override
public void attack(Unit other) {
    super.attack(other);
    gainExperience();
    if (!other.isAlive() && other instanceof Monster) {
        addTitle(((Monster) other).fetchTitle());
    }
}
```
Ez sem a legszebb megoldás, hiszen egy strukturális kapcsolatot tesz be a `Hero` és a `Monster` közé. 
Eddig akár teljesen meg is szüntethettük volna a `Monster` osztályt, a `Hero` attól függetlenül működött volna. 

Van még más megoldás is, de maradunk ennél, részben a technikai ismeretek miatt, részben azért, mert kicsi esélye van annak, hogy megszűnne a `Monster` osztály, vagy más is adna címeket.

A teljes kód [itt](src/0230_title/) érhető el.

# Játék, térkép, első felület

Sokáig halogattuk, de itt az ideje ténylegesen játszani. 
Nyilvánvalóan rengeteg funkciót el tudunk képzelni, de első változatnak törekedjünk egy nagyon minimális változatra, és azt bővítsük a későbbiekben.
Egy minimális játékban van egy nagyon egyszerű pálya, ahol több szörny van lepakolva, a hőssel pedig ezt kellene bejárni.
Győzünk, ha az összes szörnytől sikerült megszabadítani a területet, veszítünk, ha a hős meghal. 
A későbbi fejezetekben nagyobb figyelmet kap majd, hogy miként érdemes hasonló funkciókat előre megtervezni úgy, hogy az a továbbiakban a lehető legkönnyebben - azaz legkevesebb kód(struktúra) változtatással - bővíthető legyen. 
Most azonban szándékosan csak a következő lépésre figyelünk, és egy meglehetősen egyszerű megközelítést alkalmazunk, lefixálunk pár dolgot.
Tesszük mindezt a annak tudatában, hogy később ez nehézségeket okozhat majd, ugyanakkor így kézzel foghatóbb lesz, miért érdemes előre felderíteni, mik a várható vagy nem valószínű módosítások, kiegészítések.

## Proof of Concept funkciók

Az első, minimális tényleges játékunk a következő legyen:
 - Adott egy téglalap alakú, egyszerű négyzetrácsos pálya.
 - Minden mező vagy szabadon bejárható, vagy egy áthatolhatatlan fal.
 - A pályán egy hősnek kell az összes szörnyet legyőznie. 
 - A hős 4 irányban mozoghat szomszédos szabad mezőkön.
 - Minden mezőn legfeljebb egy szörny található, ami nem mozog. 
 - A hős csak akkor tudja megütni a szörnyet, ha ugyanazon a mezőn áll, és ekkor a szörny utána vissza is üt. 
 - A játék akkor ér véget, ha sikerült legyőzni az összes szörnyet, vagy a hős meghal.  
 - Az ütések, szintlépések logikája a korábbiakkal megegyezik.

A megjelenítésre egyelőre semmilyen megkötést nem alkalmazunk.

## Logika - megjelenítés szétválasztása

Csábító a lehetőség, hogy fejest ugorjunk az implementálásba, hiszen már nincs messze, hogy végre játszható változata legyen a nagyon primitív, de legalább saját játékunknak. 
Ugyanakkor érdemes még billentyűzet helyett egy kis ideig papírt és ceruzát ragadni, hogy az elkészítendő osztályainkat valamennyire megtervezzük. 

Az első és legfontosabb, hogy a játéklogikát és a megjelenítést már az elején jól elkülönítsük. 
Ez egy bevállt és logikus tervezési minta, legyen szó weboldalakról, játékokról, vagy egy táblázatkezelőről. 
Rögzítsük le tehát, hogy legyen két osztályunk, jól körülhatárolt felelősségekkel:
 - `GameLogic`, mely felelős a pálya betöltéséért, a kezdeményezett események végrehajtásáért, és ezzel együtt a játékállapot karban tartásáért. 
 - `UI`, mely fő feladata a játékossal való kommunikáció, azaz számára értelmezhető módon megmutatni a játék állapotát, valamint a következő eseményt bekérni.

Fontos, hogy a logika semmilyen formában ne kommunikáljon a játékossal. 
A játék jelenlegi szintjén gondolhatunk úgy rá, mint egy passzív állapotgép, amit csak a `UI` léptet tovább, ha a felhasználótól arra utasítást kapott. 
Jelen helyzetben a logika nem is tud a megjelenítési rétegről, szimplán kiszolgálja azt. 
Ez lehetőséget ad arra, hogy a logika változtatása nélkül a megjelenítést lecseréljük.
A `UI` viszont tud a logikáról, hiszen őt használja, neki továbbítja a játékos utasításait, és tőle kérdezi le a játék új állapotát, hogy azt a játékosnak megjeleníthesse.

Egy leegyszerűsített folyamata a játéknak így néz ki:
1. Inicializálódik a játéklogika, és a felhasználói interfész.
2. Utóbbi megjeleníti a játék kezdeti állapotát.
3. Amíg a játék valamilyen módon nem ért véget:
   1. A felhasználói felület bekéri a következő lépést a felhasználótól, ha szükséges, ezt ellenőrzi, újrakéri, stb.
   2. A felület végrehajtatja a játéklogikán a lépést, ami így egy új állapotba kerül.
   3. A felület lekérdezi a logikától az új állapotot, és megjeleníti a felhasználó számára.

> [!NOTE]
> A logikáért felelős részére a szoftvernek általában `Model`-ként hivatkozunk, míg a megjelenítésért felelős részre `View`-ként. 
> Ez általános, ahogy a fent taglalt szempontok is. 
> Arra azonban, hogy ezek együttműködése pontosan miként szerveződik, arra számos hasonló, de részleteiben eltérő megközelítés adott.
> Egy nem teljes lista:
>  - **MVC**  - [Model-View-Controler](https://chatgpt.com/c/67d2a8a6-0cc0-8008-9a0b-5a523e196082)
>  - **MVVM** - [Model-View-ViewModel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
>  - **MVP** - [Model-View-Presenter](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter)


## Osztályok megtervezése

Bár vélhetően nem lesz teljes a lista, próbáljuk a fenti folyamat alapján összeszedni, milyen metódusokra lesz szükség `UI` és `GameLogic` oldalon, valamint azoknak milyen argumentumai, visszatérési értékei vannak.

> [!TIP]
> Továbbolvasás előtt próbáld meg összeírni ezeket.

### Inicializálás, pálya fájlformátum

Mivel a view-nak kell tudni a modellről, ezért előbb az utóbbit kell inicializálni. 
A leírtak alapján a pályát egy fájlból volna célszerű beolvasni. 
Hogy ez a fájl milyen nyelven legyen megírva, arra több kézenfekvő opció is adja magát.
A teljesség igénye nélkül néhány triviális ötlet:
 - **JSON** - [JavaScript Object Notation](https://docs.fileformat.com/web/json/)
 - **YAML** - [YAML Ain't a Markup Language](https://yaml.org/)
 - **XML**  - [Extensible Markup Language](https://docs.fileformat.com/web/xml/)
 - saját formátum

Ezeknek és más további opcióknak is megvannak az előnyeik, hátrányaik, amikre most részletesen nem térünk ki, csak röviden vázoljuk, miért az XML-t választjuk:
 - Saját szöveges formátum vélhetően a legegyszerűbb és legátláthatóbb az elején, azonban újabb entitások megjelenésével ez az előny hamar hátránnyá válik, sok lehet a hibalehetőség, stb.
 - JSON és YAML jól definiált formátumok, viszonylag könnyen olvashatók emberi szemmel is, könnyen kiterjeszthetők, elterjedtek, így létezik hozzájuk parser. Azonban ezek nem az alapértelmezett Java könyvtár részei. 
 - Az XML kevésbé könnyen olvasható, kissé régimódibb, de nem szükséges hozzá külső könyvtárak használata, így maradunk ennél.

XML formátumban egy példa pálya például így nézhetne ki:

```xml
<game>
    <map>
##############################
#_______________4_____2______#
#_##################H##__###_#
#_#_____1_________3____1111__#
##############################
    </map>
    <hero name="Rosie" health="25" damage="1" defense="0" />
    <monsters>
        <monster type="1" name="Goblin" health="20" damage="1" defense="0" />
        <monster type="2" name="Orc" health="30" damage="3" defense="0" />
        <monster type="3" name="Uruk hai" health="40" damage="4" defense="2" />
        <monster type="4" name="Wraith" health="200" damage="10" defense="5" title="Wraithslayer" />
    </monsters>
</game>
```

Ez az egyszerű fájl tartalmaz minden szükséges információt egy játék létrehozásához:
 - a `<map>` node tartalmazza a térképet, ahol `#` jelöli a falakat, számok a különböző szörnyeket, `H` pedig a hős kezdeti helyét
 - a `<hero>` írja le a hős fontosabb kezdeti adatait
 - a `<monsters>` alatt vannak az egyes szörnytípusok adatainak a részletei

Ahhoz, hogy ebből a fájlból fel tudjon épülni a játékállapot, kelleni fog egy `GameLogic(String filename)` konstruktor.

A view-nak tudnia kell a modellről, így annak logikus egy `UI(GameLogic model)` konstruktor.

### Aktuális játékállapot megjelenítése

Eddig nem esett szó róla, hogyan nézne ki a megjelenítés. 
Legelső körben mindenképpen valamilyen karakteres interfészt készítünk el. 
Még ezen belül is sok lehetőség adódna, de most a lehető legegyszerűbb megoldáshoz folyamodunk, és valami ilyesmit képzelünk el:

```
Your hero: Rosie (HP:25, DMG: 1, DEF: 0) - LVL 1
There is nothing in front of you. 
Where do you want to go? (N/E/W/S)
> N
You cannot move there.
> E
You cannot move there.
> S
Your hero: Rosie (HP:25, DMG: 1, DEF: 0) - LVL 1
There is a monster in front of you. 
Do you want to move (N/E/W/S) or Attack (A)?
> A
You attack the monster...

Your hero: Rosie (HP:22, DMG: 1, DEF: 0) - LVL 1
There is a monster in front of you. 
Do you want to move (N/E/W/S) or Attack (A)?
>
```

Ebből az aktuális játékállapot a hős adatai, illetve az azt követő sor arról, hogy van-e szörny az adott mezőn. 
Ezt logikusan egy `UI.printState()` metódus írná ki.

Most gondoljuk végig, hogy ennek a függvénynek milyen másik függvényekre van szüksége modell oldalon.
A hős adatainak kiírásához például három lehetőség, ami adja magát:
 - `String GameLogic.getHeroInfo()` mely egy az egyben visszaadja a szükséges szöveget.
 - `Hero GameLogic.getHero()` mely visszaadja magát a hőst, és a view-ra bízza, abból milyen adatokat, milyen formában vesz ki, jelenít meg.
 - `String GameLogic.getHeroName()`, `int GameLogic.getHeroDamage()`, stb. metódusokkal minden egyes adat külön lekérdezhető.

Vegyük sorra az egyes opciók előnyeit, hátrányait.
Az első megoldás most tökéletesen megfelel az igényeinknek, hiszen view oldalon ennyi lenne az implementáció:

```java
class UI {
    private GameLogic model;
    
    public UI(GameLogic model) {
        this.model = model;
    }

    public void printState() {
        System.out.println(this.model.getHeroInfo());
        // print field info
    }
}
```

Bár ez most bőven elég, könnyen látható, hogy a későbbiekben ha bármilyen más formában szeretnénk megjeleníteni a hős adatait, akkor már csak körülményes workaroundokkal lehetséges.
Ez egy nagyon beégetett megjelenítési logika a modell oldalon, kerülendő.

A második megoldás sokkal nagyobb szabadsági fokot adna, és valami ilyesmire cserélődne a fentihez képest a `printState` függvény:

```java
    public void printState() {
        System.out.println(this.model.getHero());
        // print field info
    }
```

Legalábbis amennyiben megfelel a `Hero.toString()` kimenete. Ha nem, akkor viszont szövegmanipulációk helyett a `Hero` osztály gettereivel szabadon módosíthatjuk később a megjelenést a modell változtatása nélkül:

```java
    public void printState() {
        Hero hero = this.model.getHero();
        System.out.println(hero.getOfficialName());
        System.out.printf("\tHealth: %d/%d\n", hero.getHealth(), hero.getMaxHealth());
        System.out.printf("\tDamage: %d\n", hero.getDamage());
        System.out.printf("\tDefense: %d\n", hero.getDefense());
        // print field info
    }
```

Sokkal testreszabhatóbb megoldás, mint az első, természetesen szükség van modell oldalon a `getHero()` metódusra is:

```java
class GameLogic {
    Hero hero;

    public int getHero() { return this.hero; }
}
```

A harmadik esetben elég hasonló lenne a kód, csak a `hero` helyett közvetlenül a modellnek tennénk fel ezeket a kérdéseket:

```java
    public void printState() {
        System.out.println(model.getHerofficialName());
        System.out.printf("\tHealth: %d/%d\n", model.getHeroHealth(), hero.getHeroMaxHealth());
        System.out.printf("\tDamage: %d\n", model.getHeroDamage());
        System.out.printf("\tDefense: %d\n", model.getHeroDefense());
        // print field info
    }
```

Ugyanúgy testreszabható, mint az előző megoldás, azonban a modellben is meg kell írni ezeket a függvényeket mind:

```java

class GameLogic {
    Hero hero;

    public int getHeroHealth() { return this.hero.getHealth(); }
    public int getHeroMaxHealth() { return this.hero.getMaxHealth(); }
    ...
}
```

Érződik, hogy ez nem szép megoldás. 
Egyrészt sok kódsort eredményez, másrészt a korábbi két példában egy "kapcsolat" volt a két osztály között (emiatt a funkció miatt), most lett 5. 
Általános cél, hogy igyekezzünk az ilyen kapcsolatok számát minimalizálni.
Ezekre tekinthetünk úgy, mint egyfajta ígéretek a szoftverünk különböző részei között. 
Minél több ilyen van, annál nehezebb később módosítani bármit, hogy ne szegjünk meg egyetlen ígéretet sem. 
Ha pedig megszegünk egyet, akkor akinek az ígéretet tettük (jelen esetben a view), annak is változtatnia kell magán. 
Ennél a megoldásnál a modell egyfajta mindenre figyelő felügyelő, aki a view és a hős között közvetít. 
A második esetben lényegében csak összeismerteti a két felet, és rájuk bízza, hogy oldják meg egymás között a dolgot.

Mindezek alapján a második megoldás mellett maradunk most, azonban itt is meg kell fogalmaznunk egy kritikát: a felület mindenféle kontrol nélkül hozzáfér ugyanahhoz a hős objektumhoz, amit a model is használ. 
Ez több turpissághoz / figyelmetlenségből adódó hibához ad jó táptalajt. 
Ezt most csak mentálisan feljegyezzük magunknak, és amíg a következő fejezetben vissza nem térünk rá, addig úri becsületszavunkat adjuk, hogy csak *okosan* használjuk ezt az objektumot.

Volt az állapotkiírásnak egy második része is, mely megadta, hogy van-e szörny a hőssel megeggyező mezőn. 
Erre is természetesen több lehetőség van:
 - `bool GameLogic.isMonsterCloseToHero()`
 - `Position GameLogic.getHeroPosition()`, `bool GameLogic.isMonsterAtPosition(Position)`
 - `Position GameLogic.getHeroPosition()`, `Monster GameLogic.getMonsterAtPosition(Position)`
 - `Monster GameLogic.getMonsterInFrontOfHero()`
 - `ArrayList<Monster> GameLogic.getAliveMosters()`, `Position GameLogic.getPositionOfUnit(Unit unit)`

> [!TIP]
> Az előző eszmefuttatás mentén hozz fel pro-kontra érveket az egyes opciók mellé, esetleg javasolj jobb megoldást.

Mi most az egyszerűség kedvéért a negyedik, `Monster GameLogic.getMonsterInFrontOfHero()` függvénnyel indulunk el, és akkor így egészül ki a view oldali függvény:

```java
    public void printState() {
        System.out.println(this.model.getHero());
        Monster monster = this.model.getMonsterInFrontOfHero();
        if (monster != null) {
            System.out.println("There is a monster in front of you!");
            System.out.println(monster)
        } else {
            System.out.println("There is nothing in front of you.");
        }
    }
```

### Következő lépés bekérése és végrehajtása

Az eddigi programjaink nem olvastak be semmit sem még a bemenetről, így egy új eszközhöz kell nyúlnunk.
A sztenderd bemenetről való olvasás legegyszerűbb módja egy `Scanner` létrehozása, és annak használata.

```java
import java.util.Scanner;

class UI {
    public String askNextMove(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Attack(A) or move(N/E/W/S)?");
        return sc.next();    
    }
}
```

Egyelőre eltekintünk annak ellenőrzésétől, hogy a felhasználó helyes választ adott-e meg.
Ezután már csak végre kell hajtatnunk a lépést a modellel, aminek nyilván kell a lehetséges eseményekhez megfelelő függvényének lennie.
Egy egyszerű megoldás:

```java
class UI {
    public void nextStep(){
        String command = askNextMove();
        switch (command) {
            case "n", "N", "e", "E", "w", "W", "s", "S" -> this.model.moveHero(command);
            case "a", "A" -> this.model.attack();
            default -> System.out.println("Unknown command, use N/E/W/S or A.");
        }
    }
}

class GameLogic {
    public void attack(){...}
    public void moveHero(String direction){...}
}
```

A modell logika implementálását későbbre hagyjuk. 

> [!NOTE]
> A fenti az újabb, Java 14-es szintaktika, a "hagyományos" `switch-case` szerkezettel `case "a", "A" -> ...` helyett `case "a": case "A": ... break;` lett volna szükséges.


### Játék végének ellenőrzése

Ezt egyszerűen egy `bool GameLogic.isGameOver()` metódussal megoldhatjuk.

### Végleges "interfészterv"

A fenti néhány pontban ezeket a metódusokat gyűjtöttük össze: 

```java
class UI {
    public UI(GameLogic model){...}
    public void printState() {...}
    public String askNextMove(){...}
    public void nextStep(){...}
}

class GameLogic {
    public GameLogic(String filename){...}
    public int getHero() { ... }
    public void attack(){...}
    public void moveHero(String direction){...}
}
```

Ezek mind, pici, egyszerű metódusok, a legtöbbnek tervezés közben már az implementációját is megadtuk. 
Hogy ne a main-ből kelljen a fentebb megírt folyamatot vezérelni, érdemes még egy `UI.run()` metódust megadni, ami levezényli a játékot, illetve akár egy `UI(String filename)` konstruktort is, amely létrehozza a modellt magának a fájl alapján. 

## Modell implementálása

A modellben igazából három dolgot kell eltárolni:
 - a térképet
 - a szörnyeket (és azok helyét)
 - a hőst (és a helyét)

Az könnyen látható, hogy koordinátákra többször szükségünk lehet, így erre érdemes egy külön típust definiálni.
Ennek egy váza valahogy így nézhetne ki:

```java
class Coordinate {
    public final int x;
    public final int y;
    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

Java 14 óta van egy kevésbé terjengős módja annak, hogy hasonló POD osztályokat rövidebben létrehozhassunk, ezek a [rekordok](https://blogs.oracle.com/javamagazine/post/records-come-to-java). 
Ezt az eszközt használva így tudunk egy pozíció típust bevezetni sor- és oszlopindex adattagokkal.
Célszerűbb ezt az indexelést használni jelen esetben, egyértelműbb, hogy a nagyobb sor index van lejjebb, stb.

```java
    record Position(int row, int col){} 
```

> [!NOTE]
> Más nyelveken is adott általában tömör, kényelmes eszköz arra, hogy hasonló típusokat létrehozzunk. 
> Például pythonban programozó olvasók figyelmébe ajánljuk a `named tuple`-öket, `dataclass`okat, stb.

Mivel egyelőre csak a modell használja ezt az információt, nyugodtan definiálhatjuk ezt egy belső típusként. 
Erre épülve a többi adattag is már megadható:

```java
import java.util.HashMap;

class GameLogic {
    
    private record Position(int row, int col){} 

    private final boolean[][] accessible;
    private final HashMap<Position,Monster> monsters = new HashMap<>();
    private final Hero hero;
    private Position heroPosition;
```

A legtöbb dolog magától érthetődő, két apró megjegyzést azonban indokolt.
`HashMap`-et eddig nem használtunk, ez egy Javaban alapból adott szótár/asszociatív tömb tároló, mely kulcs-érték párokat tárol. 
Azzal, hogy a pozíció a kulcs, az érték pedig a szörny, egyszerre tudjuk tárolni a szörnyeket a pozíciójukkal, és gyorsan hozzá tudunk férni egy adott mezőn lévő szörnyhöz, ha van.
Utóbbi a mi kicsi pályáinkon nyilván nem fontos, de egy valamirevaló informatikus (egy adatstruktúrák kurzussal a háta mögött) nem fogja például listában eltárolni a pozíció-szörny párokat. 

Egy másik érdekes dolog, hogy a `heroPosition`-t leszámítva minden `final`.
Ez logikus az `accessible`-nél, de a többi adatnál arra gondolnánk, hogy változik, pl a hős is sebződik, stb.
Ezt a gondolatot most félretesszük a következő fejezetig, ahol a korábban taglalt `getHero()` problémát is kitárgyaljuk. 
Most röviden előrevetítve csak annyi, hogy itt `hero` *személye* végleges, nem az *állapota*, és ugyanez igaz a szörnyeknél is.

A következő a konstruktor, mely beolvassa az XML fájlból az adatokat, és inicializálja ezeket az adattagokat. 
Mivel jelen jegyzetnek nem fókusza az XML parzolás, csupán a fejlesztett program egy kényelmi funkciójáról van szó, ennek a kódját verbatim közöljük. 
Az érdeklődő olvasó ne habozzon felcsapni a kapcsolódó referenciát ha összetettebb dolgot szeretne megvalósítani.
Tehát egy működő, és viszonylag tömör konstruktor két segédfüggvénnyel:

```java
    private static String getStringAttribute(Node node, String attributeName) {
        Node attribute = node.getAttributes().getNamedItem(attributeName);
        return attribute == null ? null : attribute.getNodeValue();
    }
    private static int getIntAttribute(Node node, String attributeName) {
        String value = getStringAttribute(node, attributeName);
        return value == null ? 0 : Integer.parseInt(value);
    }

    public GameLogic(String filename) throws Exception {        

        Document document = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new File(filename));
        
        String mapString = document.getElementsByTagName("map").item(0).getTextContent().trim();
        String[] rows = mapString.split("\n");
        int height = rows.length;
        int width = rows[0].length();
        this.accessible = new boolean[height][width];

        HashMap <Integer,Node> monsterNodes = new HashMap<Integer,Node>();
        NodeList monstersNodeList = document.getElementsByTagName("monster");
        for (int i=0; i<monstersNodeList.getLength(); ++i) {
            Node monsterNode = monstersNodeList.item(i);            
            monsterNodes.put(getIntAttribute(monsterNode, "type"), monsterNode);
        }

        Node heroNode = null;
        for (int r = 0 ; r < height ; ++r) {
            for (int c = 0 ; c < width ; ++c) {
                char cell = rows[r].charAt(c);
                this.accessible[r][c] = (cell != '#');
                if (cell == 'H' && heroNode == null) {
                    this.heroPosition = new Position(r,c);
                    heroNode = document.getElementsByTagName("hero").item(0);                        
                }
                else if (Character.isDigit(cell)){
                    Node monsterNode = monsterNodes.get(Integer.valueOf(String.valueOf(cell)));                        
                    this.monsters.put(new Position(r,c), new Monster(
                        getStringAttribute(monsterNode, "name"),
                        getIntAttribute(monsterNode, "health"),
                        getIntAttribute(monsterNode, "damage"),
                        getIntAttribute(monsterNode, "defense"),
                        getStringAttribute(monsterNode, "title")
                    ));
                }
            }
        }
        this.hero = new Hero(
            getStringAttribute(heroNode, "name"),
            getIntAttribute(heroNode, "health"),
            getIntAttribute(heroNode, "damage"),
            getIntAttribute(heroNode, "defense")
        );
    }
```

Megjegyzendő még, hogy pár import szükséges, illetve a parzolás során keletkező potenciális hibák lekezelése helyett most szimplán jeleztük, hogy ez a konstruktor is dobhat kivételt. 
Ezt majd az ezt meghívó `UI` konstruktornál is ugyanígy meg kell tennünk.

> [!TIP]
> Továbbolvasás előtt próbáld meg a korábban megtervezett metódusokat implementálni.

Ezek után végre a lényegre térhetünk.
Terveztünk két egyszerű gettert, valamint egy játék végét ellenőrző függvényt.
Ezek a fentieket használva kényelmesen egy sorban megvalósíthatók:

```java
    public Hero getHero() { return this.hero; }
    
    public boolean isGameOver() {
        return this.monsters.isEmpty() || !this.hero.isAlive();
    }

    public Monster getMonsterInFrontOfHero() {
        return this.monsters.get(this.heroPosition);
    }
```

Fontos megjegyezni, hogy jelenleg ha nincs szörny a hős előtt, akkor a `getMonsterInFrontOfHero` nem kivételt dob, hanem a `HashMap.get` működése alapján `null`-t ad vissza.

A `moveHero` esetében érdemes bevezetni egy logikai visszatérési értéket, hogy sikerült-e az adott irányba elmozdulni a hőssel, vagy falba ütköztünk.
Ezek után a kapott N/E/W/S szöveg alapján módosítani kell a hős pozícióját. 

```java
    boolean moveHero(String direction) {
        Position newPosition;
        switch(direction) {
            case "n", "N" -> newPosition = new Position(this.heroPosition.row - 1, this.heroPosition.col);
            case "e", "E" -> newPosition = new Position(this.heroPosition.row, this.heroPosition.col + 1);
            case "w", "W" -> newPosition = new Position(this.heroPosition.row, this.heroPosition.col - 1);
            case "s", "S" -> newPosition = new Position(this.heroPosition.row + 1, this.heroPosition.col);
            default -> { return false; }
        }
        if (!this.accessible[newPosition.row][newPosition.col]) return false;
        this.heroPosition = newPosition;
        return true;
    }
```

A támadás is könnyen megvalósítható, arra kell csak figyelni, hogy a szörny is visszaüssön, ha még életben maradt:

```java
    void attack() {
        Monster monster = getMonsterInFrontOfHero();
        if (monster == null) return;
        this.hero.attack(monster);
        if (monster.isAlive()) monster.attack(hero);
        else this.monsters.remove(this.heroPosition);
    }
```

Ha meghalt a szörny, akkor pedig kitöröljük a szörnyszótárból.

Ezzel készen is vagyunk a modellel, minden tervezett függvény megvan, összesen ~30 sorból az XML parzolást és az adattagok deklarálását leszámítva.

## View implementálása

Mivel ezt már félig-meddig korábban meg is tettük, könnyebb dolgunk lesz. 
A fenti tervekben egyetlen adattagja volt a `UI` osztálynak. 
Azonban pazarló volna minden egyes `askNextMove` hívás esetén új `Scanner`t létrehozni, ezért már inicializáláskor készítünk egyet, és azt használjuk minden egyes felhasználói bemenet olvasáskor.

```java
import java.util.Scanner;

class UI {
    private final GameLogic model;
    private final Scanner scanner = new Scanner(System.in);
```

Itt is minden lehet privát és `final`.

Mivel a másik tipikus dolog, amit a `UI` tesz, hogy kiír valamit a sztenderd kimenetre, ezért érdemes egy saját `print` függvényt definiálni, és azt használni. 
Ez egyrészt rövidebb is, mint mindenhol `System.out.println`-eket irogatni, másrészt ha később valamit módosítanánk a kiíratási logikán, azt csak egy helyen kell cserélni.
Hogy kényelmes legyen, egy olyan metódust definiálunk, mely változó számú argumentumot fogad el, és azokat szimplán az `System.out`-ra írja ki:

```java
private void print(Object... text) { for (Object s : text) System.out.print(s); }
```

Ezután jöhet a két tervezett konstruktor, melyek beállítják a modellt, és kiírják az üdvözlő üzenetet:

```java
    public UI(GameLogic model) {
        this.model = model;
        print("Welcome to the game!\n\n");
    }

    public UI(String mapFileName) throws Exception {
        this(new GameLogic(mapFileName));
    }
```

Itt ahelyett, hogy a kiíratás, modellbeállítás logikát megismételtük volna a második konstruktorban, csupán felparaméterezve meghívjuk az elsőt.

Az állapotkiírás gyakorlatilag fentebb már elkészült.
A végleges változat használva a fenti `print`-et:

```java
    private void printState() {
        print("\n\n", this.model.getHero(), "\n");
        Monster monster = this.model.getMonsterInFrontOfHero();
        if (monster != null) print("There is a monster in front of you: ", monster, "\n");
        else print("There is nothing in front of you.\n");
    }
```

A `Scanner` objektum létrehozásának eltávolításával az `askNextMove` metódus csupán egy kiíratásra és egy visszatérésre fogyott, amit csak egy helyen használunk, a `nextStep`-ben, így a tartalmát szimplán beemelhetjük oda:

```java
    private void nextStep(){
        print("Attack(A) or move(N/E/W/S)? ");
        String command = this.scanner.next();
        switch (command) {
            case "n", "N", "e", "E", "w", "W", "s", "S" -> {
                if (!this.model.moveHero(command)) print("You cannot move there.\n");
            }
            case "a", "A" -> this.model.attack();
            default -> print("Unknown command, use N/E/W/S or A.\n");
        }
    }
```

Mozgás esetében itt jön jól a `GameLogic.moveHero` visszatérési értéke, ami alapján visszajelezhetünk, ha nem sikerült a lépés.

Szemfülesebb olvasók észrevehették, hogy a konstruktort leszámítva minden metódus privát az eredetileg tervezett helyett. 
Ennek oka, hogy a fentebb javasolt "levezénylő" metódust is megírjuk, és ebben az esetben nem is akarjuk, hogy valaki kívülről a megadott folyamattól eltérően meghívja bármelyik fenti függvényt.

```java
    public void run() {
        printState();
        while (!model.isGameOver()) {
            nextStep();
            printState();
        }
        if (this.model.getHero().isAlive()) print("The hero cleansed the world of monsters!\n");
        else print("The hero died, the monsters reign over the world.\n");
    }
```

A játék tervezett logikája szépen lekövethető ebből a 6 sorból, anélkül hogy a megvalósítás részletei előttünk lennének. 

Már csak az maradt hátra, hogy valahol létrehozzunk egy ilyen view-t és modellt, majd elindítsuk a játékot:

```java
class Main {
    public static void main(String[] args) throws Exception{
        new UI("maps/minimal.xml").run();
    }
}
```

A teljes kód [itt](src/0240_Map/) érhető el.

## Játék, végre

A [`minimal.xml`](src/0240_Map/maps/minimal.xml)-ben megadott játék tényleg nagyon minimalista:

```xml
<game>
    <map>
########
#_H__1_#
########
    </map>
    <hero name="Rosie" health="25" damage="1" defense="0" />
    <monsters>
        <monster type="1" name="Goblin" health="20" damage="1" defense="0" />
    </monsters>
</game>
```

A fenti program egy minta futása:

```
Welcome to the game!



Rosie (HP: 25, DMG: 1, DEF: 0)
There is nothing in front of you.
Attack(A) or move(N/E/W/S)? 
Unknown command, use N/E/W/S or A.


Rosie (HP: 25, DMG: 1, DEF: 0)
There is nothing in front of you.
Attack(A) or move(N/E/W/S)? N
You cannot move there.


Rosie (HP: 25, DMG: 1, DEF: 0)
There is nothing in front of you.
Attack(A) or move(N/E/W/S)? E


Rosie (HP: 25, DMG: 1, DEF: 0)
There is nothing in front of you.
Attack(A) or move(N/E/W/S)? e


Rosie (HP: 25, DMG: 1, DEF: 0)
There is nothing in front of you.
Attack(A) or move(N/E/W/S)? e


Rosie (HP: 25, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 20, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? e


Rosie (HP: 25, DMG: 1, DEF: 0)
There is nothing in front of you.
Attack(A) or move(N/E/W/S)? w


Rosie (HP: 25, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 20, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 24, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 19, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 23, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 18, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 22, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 17, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 21, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 16, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 20, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 15, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 19, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 14, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 18, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 13, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 17, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 12, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 16, DMG: 1, DEF: 0)
There is a monster in front of you: Goblin (HP: 11, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 35, DMG: 2, DEF: 1)
There is a monster in front of you: Goblin (HP: 10, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 35, DMG: 2, DEF: 1)
There is a monster in front of you: Goblin (HP: 8, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 35, DMG: 2, DEF: 1)
There is a monster in front of you: Goblin (HP: 6, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 35, DMG: 2, DEF: 1)
There is a monster in front of you: Goblin (HP: 4, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 35, DMG: 2, DEF: 1)
There is a monster in front of you: Goblin (HP: 2, DMG: 1, DEF: 0)
Attack(A) or move(N/E/W/S)? a


Rosie (HP: 35, DMG: 2, DEF: 1)
There is nothing in front of you.
The hero cleansed the world of monsters!
```

# Záró gondolatok

Működik a játékunk, még ha fapadosan is, így jogosan örülünk. 
Azonban pár gondoltot érdemes összegyűjteni, mert van még mit kalapálni:
 - Több hibalehetőséget nem kezeltünk le rendesen.
 - Nem szép a N/E/W/S karakteres megoldás. 
 - Sokat növelne a komfortfokozatunkon ha "látnánk" valamit magunk körül.
 - Nem látjuk jelenleg, hányas szintű a karakterünk.
 - Célszerű volna, ha ki is tudnánk menteni a játékunk állapotát.

De ezek már a következő fejezetre maradnak, ahogy a `GameLogic.getHero()` kapcsán felvetődött kérdések is. 


