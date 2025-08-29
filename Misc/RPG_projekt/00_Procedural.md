# Kiinduló procedurális implementáció

A jegyzet ezen részében tehát nem top-down előre megtervezzük a teljes programot, hanem inkább iteratív módon, lépésről lépésre bővítjük funkciókkal a játékunkat, és közben ismerjük meg az OO elveket, azok Java nyelven történő megvalósításának lehetőségeit. 

A kiinduló állapothoz feltételezzük, hogy az olvasó ismeri a procedurális programozás alapvető eszközeinek (elágazások, ciklusok, függvények) megfelelő használatát.
Ezen eszközök Java megfelelőit, valamint egy alkalmas fejlesztőkörnyezet beállítását az előző fejezetben tárgyaltuk.

Kezdésnek egy nagyon minimális szituációból induljunk ki:
 - Van egy hős és egy szörny.
 - Mindkettőnek van valamennyi életpontja, és sebzési értéke.
 - A program folytasson le egy *csatát* amiben felváltva üti meg egymást a két fél, kezdve a hőssel.
 - A program írjon ki köztes helyzetjelentéseket, majd a végén, hogy melyik fél győzött (maradt életben.)



## Első megvalósítás

Az előző fejezetben tárgyaltak szerint kódunkat egyetlen `Main.java` fájlban írjuk meg, az alábbi skeletont kiegészítve:

```java
class Main {
    public static void main(String[] args) {
        // Programkód helye
    }    
}
```

A hős és a szörny életerejének, valamint támadásának tárolására első körben egy `int` megfelel. 
Legyen a hős nagyobb életerejű, de kisebb támadású, pl:

```java
int heroHP = 8;
int heroDMG = 1;
int monsterHP = 5;
int monsterDMG = 2;
```

Naplózás jelleggel a kódban több helyen érdemes lehet majd kiírni a jelenlegi állapotot, melyhez a `System.out.printf` *utasítást* is használhatjuk. 

```java
System.out.printf("Hero (DMG: %d, HP: %d) vs. Monster (DMG: %d, HP: %d)\n", heroDMG, heroHP, monsterDMG, monsterHP);
```

> [!NOTE]
> Sejthető, illetve később majd látni fogjuk, hogy ez valójában nem a a nyelv részeként deklarált *utasítás*, de egyelőre megfelel ez az ismert terminológia.
> A `printf` működése ismerős lehet linux vagy C alapokkal rendelkezőknek. Python programozók számára az f-sztringekhez, % formázáshoz hasonlítható.

Először a hős támadja meg a szörnyet, ez meglehetősen egyszerűen kivitelezhető:

```java
monsterHP -= heroDMG;
```

Azonban figyelni kell arra is, hogy 0 alá ne csökkenjen az életerő, azaz:
```java
monsterHP -= heroDMG;
if (monsterHP < 0) {
    monsterHP = 0;
}
```

Ezt követően a szörny üt vissza hasonlóan:

```java
heroHP -= monsterDMG;
if (heroHP < 0) {
    heroHP = 0;
}
```

Mindezt addig kell ismételni, amíg mindkettő életben van, amit most egy végtelen `while` ciklussal és `break` utasításokkal oldunk meg. 

A végleges kód a kiíratásokkal kiegészítve, ami [itt](src/0000_init_base/Main.java) is megtalálható:

```java

class Main {

    public static void main(String[] args) {

        int heroHP = 8;
        int heroDMG = 1;
        int monsterHP = 5;
        int monsterDMG = 2;

        System.out.printf("Hero (DMG: %d, HP: %d) vs. Monster (DMG: %d, HP: %d)\n", heroDMG, heroHP, monsterDMG, monsterHP);

        while (true) {
            System.out.println("The hero attacks the monster...");
            monsterHP -= heroDMG;
            if (monsterHP < 0) {
                monsterHP = 0;
            }
            System.out.printf("Hero (DMG: %d, HP: %d) vs. Monster (DMG: %d, HP: %d)\n", heroDMG, heroHP, monsterDMG, monsterHP);
            if (monsterHP == 0) {
                System.out.println("The hero won the battle \\o/");
                break;
            }
            System.out.println("The monster attacks the hero...");
            heroHP -= monsterDMG;
            if (heroHP < 0) {
                heroHP = 0;
            }
            System.out.printf("Hero (DMG: %d, HP: %d) vs. Monster (DMG: %d, HP: %d)\n", heroDMG, heroHP, monsterDMG, monsterHP);
            if (heroHP == 0) {
                System.out.println("The hero lost the battle :-(");
                break;
            }
        }
    }
}
```

A programot lefordítva (`javac Main.java`) majd futtatva (`java Main`) a következő kimenetet kapjuk:

```
Hero (DMG: 1, HP: 8) vs. Monster (DMG: 2, HP: 5)
The hero attacks the monster...
Hero (DMG: 1, HP: 8) vs. Monster (DMG: 2, HP: 4)
The monster attacks the hero...
Hero (DMG: 1, HP: 6) vs. Monster (DMG: 2, HP: 4)
The hero attacks the monster...
Hero (DMG: 1, HP: 6) vs. Monster (DMG: 2, HP: 3)
The monster attacks the hero...
Hero (DMG: 1, HP: 4) vs. Monster (DMG: 2, HP: 3)
The hero attacks the monster...
Hero (DMG: 1, HP: 4) vs. Monster (DMG: 2, HP: 2)
The monster attacks the hero...
Hero (DMG: 1, HP: 2) vs. Monster (DMG: 2, HP: 2)
The hero attacks the monster...
Hero (DMG: 1, HP: 2) vs. Monster (DMG: 2, HP: 1)
The monster attacks the hero...
Hero (DMG: 1, HP: 0) vs. Monster (DMG: 2, HP: 1)
The hero lost the battle :-(
```

## Procedurális szépítések

Bár még 40 soros sincs a programunk, érdemes egy pillanatra megállni, és kritikus szemmel megnézni a kódunkat, hogy van-e olyan *code smell* amiről már korábbi programozási tanulmányaink során tanultunk. 
Egy ekkora kódnál még talán indokolatlannak tűnhet refaktorálás, de a sok tervezett funkciót fejben tartva nem árt, ha már most kritikusak vagyunk a saját kódunkkal szemben. 

Az informatikus szakmában sok helyen megfogadandó ökölszabály, hogy ha bármi redundánsan több helyen szerepel, akkor többek között nem szép a kód, hibalehetőséget rejt magában, és nehéz karbantartani. 
Területtől függően ezért használunk makrókat, függvényeket, sablonokat, stb.

> [!TIP]
> Továbbolvasás előtt próbáld meg azonosítani és orvosolni ezeket a *csúnyaságokat* önállóan.

Két ismétlődés szembetűnő:
1. Az állapot kiírásának formátuma három helyen szerepel a kódban.
2. Az életerő csökkentés logikája két helyen (és irányban) szerepel. 

Az elsőt könnyedén kiszervezhetjük egy függvénybe, aminek azonban meg kell kapnia a hős és a szörny adatait:

```java
static void printStatus(int heroHP, int heroDMG, int monsterHP, int monsterDMG) {
    System.out.printf("Hero (DMG: %d, HP: %d) vs. Monster (DMG: %d, HP: %d)\n", heroDMG, heroHP, monsterDMG, monsterHP);
}
```

Azonban ezen függvényen belül is ismétlődik az a logika, hogy milyen formában van egy lény kiírva, ami könnyedén egy további függvénybe kiszervezhető:

```java
static String unitDisplayText(String name, int DMG, int HP) {
    return String.format("%s (DMG: %d, HP: %d)", name, DMG, HP);
}

static void printStatus(int heroHP, int heroDMG, int monsterHP, int monsterDMG) {
    System.out.printf("%s vs. %s\n", unitDisplayText("Hero", heroDMG, heroHP), unitDisplayText("Monster", monsterDMG, monsterHP));
}
```

Itt a [`String.format`](https://www.baeldung.com/string/format)-ot használtuk, ami a `System.out.printf`-hez hasonlóan működik, de a standard outputra való kiírás helyett visszaadja a formázott szöveget. 

A támadási logikának egy lehetséges kiszervezése a következő, ahol a függvény a támadó és a védekező adatai alapján adja vissza a védekező új (támadás utáni) életerejét:

```java
static int hpAfterAttack(int currentHP, int attackerDMG) {
    if (attackerDMG >= currentHP) {
        return 0;
    } else {
        return currentHP - attackerDMG;
    }
}
```

Ezek után a `main` függvény a következőre redukálódik:

```java
public static void main(String[] args) {

    int heroHP = 8;
    int heroDMG = 1;
    int monsterHP = 5;
    int monsterDMG = 2;
    
    printStatus(heroHP, heroDMG, monsterHP, monsterDMG);

    while (true) {
        System.out.println("The hero attacks the monster...");
        monsterHP = hpAfterAttack(monsterHP, heroDMG);
        printStatus(heroHP, heroDMG, monsterHP, monsterDMG);
        if (monsterHP == 0) {
            System.out.println("The hero won the battle \\o/");
            break;
        }
        System.out.println("The monster attacks the hero...");
        heroHP = hpAfterAttack(heroHP, monsterDMG);
        printStatus(heroHP, heroDMG, monsterHP, monsterDMG);
        if (heroHP == 0) {
            System.out.println("The hero lost the battle :-(");
            break;
        }
    }
}
```

A teljes kód egyben [itt](src/0010_init_functions/Main.java) elérhető, és az előző változattal teljesen megegyező kimenetet kapunk. 


## Védekezés logika

Bár még biztosan volna mit csiszolni a fenti kódon, de úgy ítéljük meg, hogy egyelőre jó lesz, itt az idő új funkciót fejleszteni. 
Az ilyen játékokban általában van egy *védekezése* is a lényeknek, ami minél nagyobb, annál kisebb sebzést tud bevinni egy támadó. 
Ennek általában egy komplex képlete van, de első körben nem akarjuk túlbonyolítani a dolgot, a védekezés legyen egy egész szám, amivel a bevitt támadás értéke csökken.

Adjunk mondjuk egy 1-es védelmet a hősünknek, a szörnynek pedig ne legyen:

```java
int heroDEF = 1;
int monsterDEF = 0;
```

A támadási logikában természetesen megjelennek ezek az új értékek, lényegében az `attackerDMG` helyére `(attackerDMG-defenderDEF)` kerül:

```java
static int hpAfterAttack(int defenderHP, int attackerDMG, int defenderDEF) {
    if ((attackerDMG-defenderDEF) >= defenderHP) {
        return 0;
    } else {
        return defenderHP - (attackerDMG-defenderDEF);
    }
}
```

Ennek megfelelően változnak a `main`-ben ennek a függvénynek a meghívásai, valamint a kiíratáshoz kötődő függvények is kibővülnek két paraméterrel (teljes kód [itt](src/0020_init_defense_logic_BAD/Main.java)):

```java
printStatus(heroHP, heroDMG, heroDEF, monsterHP, monsterDMG, monsterDEF);

while (true) {
    System.out.println("The hero attacks the monster...");
    monsterHP = hpAfterAttack(monsterHP, heroDMG, heroDEF);
    printStatus(heroHP, heroDMG, heroDEF, monsterHP, monsterDMG, monsterDEF);
    if (monsterHP == 0) {
        System.out.println("The hero won the battle \\o/");
        break;
    }
    System.out.println("The monster attacks the hero...");
    heroHP = hpAfterAttack(heroHP, monsterDMG, monsterDEF);
    printStatus(heroHP, heroDMG, heroDEF, monsterHP, monsterDMG, monsterDEF);
    if (heroHP == 0) {
        System.out.println("The hero lost the battle :-(");
        break;
    }
}
```

Bár első ránézésre minden rendben levőnek tűnik, sajnos két sebből is vérzik ez a program.

> [!TIP]
> Továbbolvasás előtt próbáld megtalálni a két logikai hibát és kijavítani.

Az egyik hiba hamar szembetűnik a programot futtatva:

```
Hero (DMG: 1, HP: 8, DEF: 1) vs. Monster (DMG: 2, HP: 5, DEF: 0)
The hero attacks the monster...
Hero (DMG: 1, HP: 8, DEF: 1) vs. Monster (DMG: 2, HP: 5, DEF: 0)
The monster attacks the hero...
Hero (DMG: 1, HP: 6, DEF: 1) vs. Monster (DMG: 2, HP: 5, DEF: 0)
The hero attacks the monster...
Hero (DMG: 1, HP: 6, DEF: 1) vs. Monster (DMG: 2, HP: 5, DEF: 0)
The monster attacks the hero...
Hero (DMG: 1, HP: 4, DEF: 1) vs. Monster (DMG: 2, HP: 5, DEF: 0)
The hero attacks the monster...
Hero (DMG: 1, HP: 4, DEF: 1) vs. Monster (DMG: 2, HP: 5, DEF: 0)
The monster attacks the hero...
Hero (DMG: 1, HP: 2, DEF: 1) vs. Monster (DMG: 2, HP: 5, DEF: 0)
The hero attacks the monster...
Hero (DMG: 1, HP: 2, DEF: 1) vs. Monster (DMG: 2, HP: 5, DEF: 0)
The monster attacks the hero...
Hero (DMG: 1, HP: 0, DEF: 1) vs. Monster (DMG: 2, HP: 5, DEF: 0)
The hero lost the battle :-(
```

Itt hamar szembetűnik, hogy a szörny egyáltalán nem sebződik, a hős pedig kettőt, pedig mindkettőnek egyet kellene. 
Némi kutakodás után feltűnhet, hogy a `main`-ben tévesen a támadó védekezési értékét adtuk át harmadik paraméternek, nem pedig a védekezőét:

```java
monsterHP = hpAfterAttack(monsterHP, heroDMG, /* !!! */ heroDEF /* monsterDEF helyett !!! */);
heroHP = hpAfterAttack(heroHP, monsterDMG, /* !!! */ monsterDEF /* heroDEF helyett !!! */);
```

Apró és buta dolog, de könnyen elképzelhető, hogy ha sokszor kerülünk ilyen szituációba, néhányszor mindenképp el fogunk vétni ilyen hibát. 
Vegyük észre, hogy a program működik, szintaktikailag helyes, első ránézésre jónak tűnő eredményeket is ad. 
Ha nem 1-1 helyett 2-0 lett volna a tényleges sebzés, hanem mondjuk 12-14 helyett 11-15, akkor valószínűleg kevésbé ordított volna ez a hiba. 

> [!NOTE]
> Hasonló függvényekre általában érdemes éppen ezért úgynevezett egységteszteket (unit test) írni, azokat a *CI pipeline*ban automatikusan futtatni. 
> Ezek tárgyalása nem jelen fejezet része, de érdemes utánaolvasni. 

Egy programozási *technika* értéke sok esetben az, hogy konzekvens követésével bizonyos típusú hibák esélyét csökkenteni vagy akár megszüntetni lehet. 
A következő alfejezetben erre még visszatérünk.

> [!NOTE]
> Uncle Bob (Robert C. Martin, Agile Manifesto egyik aláírója, a [Clean code könyv](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) szerzője) a [The Future of Programming Languages at the Confluence of Paradigms](https://www.youtube.com/watch?v=ya1xDCCMh7g) előadásában a paradigmákat *magunkra erőszakolt megkötések halmazaként* definiálja, melyeknek hasonlóan az a célja, hogy bizonyos hibákat kiküszöböljön. 

A másik hiba kevésbé észrevehető, de ha egy védekezési érték nagyobb, mint a támadási, akkor a megtámadott lény az `(attackerDMG-defenderDEF)` miatt *gyógyul*, ami nyilván nem helyes működés.
Ez szerencsére könnyen javítható:

```java
static int hpAfterAttack(int defenderHP, int attackerDMG, int defenderDEF) {
    int damage = attackerDMG > defenderDEF ? attackerDMG - defenderDEF : 0;
    if ( damage >= defenderHP) {
        return 0;
    } else {
        return defenderHP - damage;
    }
}
```

De ha már a `damage` kiszámolásához használtuk az [ternáris operátort](https://en.wikipedia.org/wiki/Ternary_conditional_operator), akkor:

```java
static int hpAfterAttack(int defenderHP, int attackerDMG, int defenderDEF) {
    int damage = attackerDMG > defenderDEF ? attackerDMG - defenderDEF : 0;
    return damage < defenderHP ? defenderHP - damage : 0;
}
```

A teljes kód [itt](src/0021_init_defense_logic/Main.java) érhető el, és végre a hősünk diadalmaskodik:

```
Hero (DMG: 1, HP: 8, DEF: 1) vs. Monster (DMG: 2, HP: 5, DEF: 0)
The hero attacks the monster...
Hero (DMG: 1, HP: 8, DEF: 1) vs. Monster (DMG: 2, HP: 4, DEF: 0)
The monster attacks the hero...
Hero (DMG: 1, HP: 7, DEF: 1) vs. Monster (DMG: 2, HP: 4, DEF: 0)
The hero attacks the monster...
Hero (DMG: 1, HP: 7, DEF: 1) vs. Monster (DMG: 2, HP: 3, DEF: 0)
The monster attacks the hero...
Hero (DMG: 1, HP: 6, DEF: 1) vs. Monster (DMG: 2, HP: 3, DEF: 0)
The hero attacks the monster...
Hero (DMG: 1, HP: 6, DEF: 1) vs. Monster (DMG: 2, HP: 2, DEF: 0)
The monster attacks the hero...
Hero (DMG: 1, HP: 5, DEF: 1) vs. Monster (DMG: 2, HP: 2, DEF: 0)
The hero attacks the monster...
Hero (DMG: 1, HP: 5, DEF: 1) vs. Monster (DMG: 2, HP: 1, DEF: 0)
The monster attacks the hero...
Hero (DMG: 1, HP: 4, DEF: 1) vs. Monster (DMG: 2, HP: 1, DEF: 0)
The hero attacks the monster...
Hero (DMG: 1, HP: 4, DEF: 1) vs. Monster (DMG: 2, HP: 0, DEF: 0)
The hero won the battle \o/
```

## Előrelátó próbálkozás

Az előző alfejezetben már láttuk, milyen hibát okozhat, hogy egyesével adogatjuk át a lények adatait, és véletlenül felcserélünk kettőt.
Bár hibát nem vétettünk, de a különösen rendszerető olvasók szépérzékét valószínűleg bántja, hogy a `printStatus` függvény `HP`/`DMG`/`DEF` sorrendben vár adatokat, a `unitDisplayText` viszont (`name`)/`DMG`/`HP`/`DEF` sorrendben, ahogy a kiíratás történik. 
Könnyen elhihető, hogy ha nem vagyunk konzekvensek, hamar a fentihez hasonló hibába futhatunk, ahogy bővülnek a funkciók, vagy a lényekhez tartozó adatok.

A bővülő adatokkal kapcsolatban egy másik kellemetlen érzésünk is adódik: folyamatosan nő a használt függvények paramétereinek száma.
Márpedig lesz (lehet) még a mi hősünknek maximális életpontja, manája, mágikus sebzése, sebzési sebessége, kritikus sebzés esélye, stb. 
Ha ezeket mind egyesével adogatnánk át, a függvényeinknek több száz paramétere lenne, ami nyilván teljesen átláthatatlanná és hibaesélyessé tenné a dolgokat.

Felvetődik az a természetes igény, hogy ezeket az egymással összetartozó adatokat valamilyen módon egy *csomagban* kellene tárolni, és függvényeknek továbbadni. 
Jelenlegi Java tudásunkkal egyetlen ilyen eszköz áll rendelkezésre: a tömb. 

> [!TIP]
> Továbbolvasás előtt refaktoráld a kódot úgy, hogy tömböket használjon a lény adatainak tárolására. 

A lények adatait ilyen módon könnyedén el tudjuk tárolni:

```java 
int[] heroData = {8, 1, 1};
int[] monsterData = {5, 2, 0};
```

Ezek után sokkal egyszerűbbé válik például a `printStatus` függvény meghívása:

```java
printStatus(heroData, monsterData);
```

és definíciója is:

```java
static void printStatus(int[] heroData, int[] monsterData) {
    System.out.printf("%s vs. %s\n", unitDisplayText("Hero", heroData), unitDisplayText("Monster", monsterData));
}
```

A tömbök az egyszerű úgynevezett *mutable* (módosítható) típusok, ami lehetőséget ad arra, hogy a támadási logikát tartalmazó függvény módosítsa az átadott lény adatait, így `hpAfterAttack` helyett egy letisztultabb `attack` függvényt tudunk már írni:

```java
static void attack(int[] attacker, int[] defender) {        
    int damage = attacker[1] > defender[2] ? attacker[1] - defender[2] : 0;
    defender[0] -= damage;
    if (defender[0] < 0) {
        defender[0] = 0;
    }
}
```

> [!NOTE]
> Vegyük észre, hogy az előző változattal ellentétben, itt már sokkal nehezebben tudjuk elkövetni azt a hibát, hogy a támadó védekezési értét használjuk, hiszen:
> - Híváskor csak két paramétert adunk át: egyben a támadót és védekezőt.
> - A függvény belsejében pedig már árulkodna, ha az első sorban a támadó támadását a támadó védekezésével hasonlítanánk össze. 

> [!CAUTION]
> Itt egy nagyon fontos technikai részlet felett (függvény argumentum másolódik-e) nagyvonalúan átsiklottunk, hogy ne vegye el a fókuszt más dolgokról.
> Ennek precíz letisztítását később meg fogjuk ejteni.

Ezeket az új függvényeket felhasználva a `main` függvényben a csata sokkal letisztultabbá válik: 

```java
while (true) {
    printStatus(heroData, monsterData);
    System.out.println("The hero attacks the monster...");
    attack(heroData, monsterData);
    if (monster[0] == 0) {
        System.out.println("The hero won the battle \\o/");
        break;
    }
    printStatus(heroData, monsterData);
    System.out.println("The monster attacks the hero...");
    attack(monsterData, heroData);
    if (hero[0] == 0) {
        System.out.println("The hero lost the battle :-(");
        break;
    }
}
```

A `unit[0]==0`-nál egy jól megválasztott nevű függvény meghívása beszédesebb, valamint jó ezt a logikát is külön választani:

```java
static boolean isAlive(int[] unit) {
    return unit[0] > 0;
}
```

Illetve az oda-vissza támadás logikája a támadó-védekező felcserélésén és a naplózó üzeneten kívül ugyanaz, így akár egy ilyen ciklusra is cserélhető:

```java
for (int turn = 0; isAlive(heroData) && isAlive(monsterData) ; turn += 1) {
    if (turn % 2 == 0) {
        System.out.println("The hero attacks the monster...");
        attack(heroData, monsterData);
    } else {
        System.out.println("The monster attacks the hero...");
        attack(monsterData, heroData);
    }
    printStatus(heroData, monsterData);
}
```

Így a fejezet végére az utolsó változatunk, mely [itt](src/0030_init_array/) is megtalálható:

```java
class Main {

    static String unitDisplayText(String name, int[] unitData) {
        return String.format("%s (HP: %d, DMG: %d, DEF: %d)", name, unitData[0], unitData[1], unitData[2]);
    }

    static void printStatus(int[] heroData, int[] monsterData) {
        System.out.printf("%s vs. %s\n", unitDisplayText("Hero", heroData), unitDisplayText("Monster", monsterData));
    }

    static void attack(int[] attacker, int[] defender) {        
        int damage = attacker[1] > defender[2] ? attacker[1] - defender[2] : 0;
        defender[0] -= damage;
        if (defender[0] < 0) {
            defender[0] = 0;
        }
    }

    static boolean isAlive(int[] unit) {
        return unit[0] > 0;
    }

    public static void main(String[] args) {

        // Always HP first, DMG second, DEF third.
        int[] heroData = {8, 1, 1};
        int[] monsterData = {5, 2, 0};

        printStatus(heroData, monsterData);

        
        for (int turn = 0; isAlive(heroData) && isAlive(monsterData) ; turn += 1) {
            if (turn % 2 == 0) {
                System.out.println("The hero attacks the monster...");
                attack(heroData, monsterData);
            } else {
                System.out.println("The monster attacks the hero...");
                attack(monsterData, heroData);
            }
            printStatus(heroData, monsterData);
        }

        if (isAlive(heroData)) {
            System.out.println("The hero won the battle \\o/");
        } else {
            System.out.println("The hero lost the battle :-(");
        }
    }
}
```

A kódunk némileg hosszabb lett, azonban ahogy azt procedurális programozás során tanultuk: kisebb, átláthatóbb részekre van szétbontva. 
A leghosszabb függvényünk, a `main` rövidebb lett, a többi pedig a clean code fanatikusok sorszámlimitjét sem lépi át. 

Ahogy az előző alfejezet végén, itt is muszáj azonban kritikákat megfogalmazni:

1. Egyszerűsített a tömb, de nagyon kell rá figyelni, hogy a 0: `HP`, 1: `DMG`, 2: `DEF` sorrendet mindenhol konzekvensen tartsuk. Ha további paraméterei lesznek egy lénynek, ez (bár a korábbinál jobb,) továbbra is átláthatatlan kódot fog eredményezni. 
2. Egyszerű Java tömbökben különböző típusú adatok nem tárolhatók, így a kiíratásért felelős függvényeknél a lény neve külön van hozzácsapva a többi adathoz. Itt is érezzük, hogy a későbbiekben szükség lehet további más típusú (logikai, lebegőpontos, tömb, stb.) adatokra is, amik ugyanúgy a kód elcsúfulásához vezetnének.

Érezzük, hogy jó lenne valahogy *névvel* hivatkozni a lényhez tartozó inhomogén típusú adatokra, ami sok későbbi fejfájástól kímélne meg minket.
A pythonos olvasók `dict`-ért (esetleg *named tuple*-ért vagy *typed dict*-ért), webfejlesztők asszociatív tömbökért kiáltanak, azonban Java-ban nem adott ilyen *alapértelmezett*, alacsony szintű adatszerkezet.

> [!NOTE]
> Az említett `dict` és asszociatív tömb Java-beli legközelebbi megfelelője a `HashMap`, mellyel hamarosan találkozunk, de semmiképpen nem tekinthető alacsony szintű adatszerkezetnek, illetve bevezetéséhez a következő fejezet ismeretei szükségesek.
> C háttérismerettel rendelkezőknek hasonlóképp csalódniuk kell a `struct`-tal kapcsolatban. (C++, C# azonos nevű adatszerkezete pedig lényegében a következő fejezet új ismeretievel hozható párhuzamba.)

3. A fentiek mellett még fel kell rónunk a kódnak, hogy a játéklogika és a naplózás keveredik, ami szintén kerülendő, valamint illene nem kódba beégetett adatokkal dolgozni, hanem bemenetről, fájlból beolvasni azokat.

Észrevehető továbbá, hogy legyen szó akár az `isAlive`, `unitDisplayText` vagy az `attack` függvényről, ezek első argumentuma lényegében mindig egy lény, amivel az a függvény dolgozik.
Érződik, hogy ezek a függvények *hozzátartoznak* azokhoz az adatokhoz, amiket a tipikusan első paraméterben átadott `int unit[]` (szerűség) tárol. 

További észrevétel lehet, hogy a csatáért felelős `main` függvény pedig az adatok inicializálásától eltekintve a többi függvénnyel ellentétben *nem lát bele* és nem is foglalkozik a lény tömbünk belső sorrendjével. 
Ennek egyik következménye, hogy sokkal olvashatóbb ez a függvény, illetve ha változtatnánk az adatok sorrendjén vagy kiegészítenénk azt, akkor a `main` függvényhez jó eséllyel nem kellene hozzányúlni.


Viszont a Földet sem egy nap alatt teremtették, a fenti problémák kikalapálását meghagyjuk magunknak akkorra, amikor már a következő fejezet ismereteivel és ott bemutatott eszközökkel gazdagabbak leszünk.

## Konklúzió

Összefoglalásképp elmondható, hogy a kezdeti procedurális változat elkészítése, szépítése, apró bővítése után, valamint a jövőbeli fejlesztésekre kitekintve kialakult bennünk az igény egy olyan programozási eszközre, mely lehetővé teszi:
1. különböző típusú adatok *egybefoglalását*
2. az ezen részadatokra névvel történő hivatkozást
3. az ezeken dolgozó függvények *társítását*
4. a megvalósítás részleteinek *elfedését*
