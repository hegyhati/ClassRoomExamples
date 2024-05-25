# Gyakorlati optimalizalas modszerei ZH
2024.05.24

#### [2p] Mik az előnyei, hátrányai egy részletesebb modellnek egy egyszerűbbel szemben?

#### [3p] Egy optimalizálási feladatot meg lehet oldani kielégíthetőségi feladatokra való megoldóval. [I/H]
Indoklás:

#### [2p] Lehet-e egy LP feladatnak pontosan kettő optimális megoldása? [I/H]
Indoklás:

#### [2p] Mit fejez ki az alábbi korlátozás? [single selection]
```ampl
s.t. Foo {p in Products} : sum {t in Tools} compatible[p,t] * bought[t] >= 2;
```
 - Minden termékhez legalább két eszköz használható
 - Legalább két eszközt meg kell venni
 - A megvett eszközök közül legalább kettőnek használhatónak kell lennie minden termékhez.
 - Minden megvett eszközt legalább két termékhez kell tudni használni.

#### [1p] Az elitizmus lényege, hogy keresztezéshez csak a legjobb egyedeket használjuk. [I/H]

#### [2p] Mely módszerek garantálják az optimális megoldás megtalálását? [multiple selection]
 - Genetikus algoritmus
 - Korlátprogramozás
 - Lineáris programozás
 - Lokális keresés

#### [1p] Melyik állítás igaz? [single selection]
 - Az alldifferent korlátozás csak arra jó, hogy rövidebben le tudjuk írni, hogy egyes változók páronként nemegyenlők
 - Az alldifferent korlátozással hatékonyabb lesz a megoldás, mint ha páronkénti nemegyenlő korlátozásokat írnánk

#### [2p] Mi az, ami korlátprogramozásban megengedett, de MILP-ben nem? [multiple selection]
 - Változók összeszorzása a korlátozásokban
 - Változóval való tömbindexelés
 - Törtszám típusú változók
 - Nemegyenlő korlátozás (!=)