# Igaz-hamis kérdések

1. Egy MILP modellben minden változónak egészértékűnek kell lennie.
2. LP modellekben legalább annyi egyenlőtlenségnek kell lenni, mint ahány egyenlet van.
3. Nem lehet optimális megoldás egy LP/MILP feladat esetében az, ha minden változó értéke 0.
4. A big-M korlátozások csak LP modellekben fordulhatnak elő.
5. A (szimplex) második fázis feladata, hogy találjon egy bázismegoldást.
6. GMPL-ben a var deklarációknak mindenképp a param-ok után kell lennie.
7. A magyar módszert a set covering (halmzlefedési) feladat megoldására dolgozták ki.

# Gyakorlati feladat

## Bemelegítő / elégséges szint

Célunk egy cég esetén úgy eldönteni az elvállalt munkákat, hogy közben a profitunkat maximalizáljuk.

A cégünk egyetlen nyersanyagból, szuperbigyóból gyárt különböző termékeket. A termelésünket megadott mennyiségű napra szeretnénk megtervezni. Minden napra adott, hogy mennyi szuperbigyó érkezik aznap be hozzánk. (A szupebigyót kilóban, nem darabban mérjük.)

Vannak megrendelések, amikről eldönthetjük, hogy elvállaljuk-e őket, vagy sem. Minden megrendeléshez adott, hogy melyik nap kellene legyártani, hogy mennyi szuperbigyóra van hozzá szükség, és hogy mennyi profitot eredményezne. 

Szuperbigyót természetesen tudunk raktározni.

## Lehetséges bővítések

1. A szuperbigyó raktározásra van felső kapacitásunk. Ha egy nap ennél több marad meg belőle, akkor az elveszik.
2. Többféle nyersanyaggal dolgozunk, és minden termékhez adott, hogy melyikből mennyit használ, valamint mindegyikről adott, hogy menyit raktározunk el. 
3. A szuperbigyóra (vagy adott esetben a többi nyersanyagra is) adott, hogy hány napig lehet raktározni anélkül, hogy megromlana.
4. Adott áron tudunk venni plusz szuperbigyót bármelyik nap.
5. Minden megrendeléshez adott, hogy hány óráig tart elkészíteni, és egy nap maximum 16 órányit tudjuk dolgoztatni a gépet.