# Igaz-hamis kérdések

1. Egy MILP modellben minden változónak binárisnak kell lennie.
2. LP modellekben legalább annyi korlátozásnak kell lenni, mint ahány változó van.
3. Előfordulhat, hogy egy LP modellnek pontosan 42 megoldása van.
4. A szimplex módszer őnmagában elég MILP feladatok megoldására.
5. A (szimplex) első fázis feladata, hogy megtalálja az optimális megoldást.
6. A GMPL case-insensitive nyelv.
7. MILP-eket könnyebben (gyorsabban) meg lehet oldani, mint LP-ket.

# Gyakorlati feladat

## Bemelegítő / elégséges szint

A célunk a Gazdinfós képzés terembeosztását megcsinálni.

Adottak:
 - Termek, és minden teremre:
   - a kapacitás
   - a bérleti díj / rezsiköltség egy órára
 - A kurzusok, és minden kurzusra:
   - az óraszám
   - a kurzust felvett hallgatók száma

Egyelőre csak egy napot szeretnénk beosztani, reggel 8-tól delután 4-ig. A cél, hogy minél kevesebb terembérleti díjat kelljen fizetni. Ebben a körben még nem kell megmondani, melyik óra mikor kezdődik, csak hogy melyik kurzus hol lesz.

## Lehetséges bővítések

1. Azt is pontosan meg kell mondani, hogy melyik óra mikor kezdődjön. 
2. Az előzőre épülve: adott az oktatóknak egy halmaza, valamint minden tárgyhoz, hogy ki tartja. Értelemszerűen egy oktató nem tud egyszerre két helyen lenni.
3. Mindegyik kurzushoz adott, hogy melyik évfolyam számára van, és a hallgatók sem tudnak egyszerre két helyen lenni.
4. Nem egy napot, hanem egy egész hetet kell beütemezni, és minden oktatóhoz adott, hogy melyik napokon ér rá, melyiken nem.
5. Vannak géptermek és sima termek, és vannak kurzusok, amik géptermeket igényelnek.
6. A cél nem a terembérleti díj minimalizálása, hanem a hallgatók által átlagosan az egyetemen töltött idő minimalizálása. Ehhez minden évfolyamhoz adott egy hallgatói létszám. 
