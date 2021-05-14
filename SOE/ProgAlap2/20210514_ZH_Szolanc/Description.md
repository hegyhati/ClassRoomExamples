# Programozás alapjai 2. -  PótZH-2
2021.05.14

## 0. Bevezető

A feladat egy szólánc játék elkészítése. A játék lényege, hogy van egy véletlenszerű kezdő szó, majd minden új szó elejének meg kell egyeznie az utolsó szó végével. További szabály még, hogy egy szót csak egyszer lehet felhasználni, és csak értelmes magyar szavakat lehet használni.

 # 1. Háttérlogika osztály

Készüljön egy `WordChain` osztály, mely a játék logikáját valósítja meg. 
Az osztály használja a mellékelt [`wordlist.json`](wordlist.json) fájlt, mely tartalmaz ~58000 magyar szót egy listában.

Inicializáláskor várjon egy paramétert, mely megadja, hogy a szavaknak milyen hosszan kell átfedni. Ha ez 1 vagy 3, akkor például `altat` után jöhet `tataroz`, de ha 2, akkor nem, akkor `atka` lehet egy következő szó (vagy például `atya`, tehát nem kell kezelni a magyar összetett betűket).
Ezen kívül állítson be egy véletlenszerű szót első szónak.

Az osztály a következő metódusokkal rendelkezzen:
 - `length`: visszaadja, hogy eddig milyen hosszú a szólánc
 - `append`: megpróbál hozzáfűzni egy szót a lánchoz, de kivételt dob, ha:
    - értelmetlen szót adunk meg
    - a megadott szó nem passzol az ulsó szóhoz
    - a megadott szót már használtuk
 
Az osztály megvalósítása során a szabályok:
 - semmelyik függványnek nem lehet semmilyen kiiratása a végleges változatban. 
 - egyik metódus sem használhat globális változókat, függvényeket, csak a sajátjait.
 - belső adatszerkezet, argumentumok típusa szabadon megválasztható, további privát metódusok kódszervezés jelleggel hozzáadhatók, publikusok nem.

# 2. Grafikus felület

Készüljön egy grafikus felület, ahol látjuk az eddigi szóláncot, valamint megpróbálhatunk hozzáfűzni egy újat. Ha megfelel, bekerül a listába, ha nem, akkor kapjunk a hiba típusáról hibaüzenetet.

Valahol jelenjen meg az is, hány pontnál járunk (azaz milyen hosszú a lánc).

A felület inicializáláskor opcionálisan megkapja az átfedés hosszát. Ha nincs megadva, akkor ezt állítsa 2-re.

A `WordChain` osztály logikáját tilos duplikálni.
