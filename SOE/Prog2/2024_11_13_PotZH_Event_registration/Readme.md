## 1. ZH pótlása

A feladat egy rendezvényszervező weboldal elkészítése Flask használatával.

A felhasználókat nem kell autentikálni, bárki számára elérhetőek az alábbi funkciók:

- Rendezvények megtekintése
- Jelentkezés rendezvényre
- Új rendezvény meghirdetése

A rendezvények és a jelentkezők adatai egy SQLite adatbázisban legyenek tárolva.
Ehhez tetszőleges python csomag használható.

A Flask végpontok az `app.py` fájlban legyenek definiálva.
Itt ne legyenek adatbázisműveletek, azok a `db.py` modulban legyenek implementálva.
Néhány példakód segítségképp megadásra került, de ezeket nem kötelező felhasználni, szabadon módosíthatók.


### Rendezvények megtekintése

A főoldalon legyenek kilistázva a meghirdetett rendezvények, két csoportban: jövőbeli és múltbeli rendezvények listája.

Jelenjen meg minden rendezvénynél:

- Név
- Helyszín
- Dátum
- Jelentkezők száma / max. létszám

A jövőbeli rendezvények között a betelt létszámúak halványabb betűszínnel jelenjenek meg

A név legyen egy link, ami a rendezvény **részletező oldalára** visz.

#### Részletező oldal

Itt jelenjenek meg a rendezvény részletes adatai, valamint a jelentkezők listája: név, e-mail cím.

Ha a rendezvény kezdési ideje még nem jött el, jelenjen meg egy form is, ahol lehet rá jelentkezni.


### Jelentkezés rendezvényre

A jelentkezéshez meg kell adni a nevet és az e-mail címet.
Ha a név-email kombináció már szerepel a rendezvény jelentkezői között, vagy betelet a megadott létszám, vagy már elmúlt a kezdési időpont, a jelentkezés kerüljön elutasításra és jelenjen meg a megfelelő hibaüzenet.

Az e-mail cím kerüljön validálásra a [UserCheck API](https://docs.usercheck.com/reference/email-endpoint) segítségével.
Ha 400-as státuszú válasz érkezik rá, akkor hibás a formátum, ezért a jelentkezés kerüljön elutasításra és jelenjen meg egy hibaüzenet.


### Új rendezvény meghirdetése

A `/new` oldalon lehessen új rendezvényt meghirdetni az adatok megadása után:

- Szervező neve
- Szervező e-mail címe
- Helyszín
- Időpont
- Maximális létszám (a szervező nem számít bele)

Egyik mező sem maradhat üres, az e-mail cím itt is kerüljön validálásra, az időpont nem lehet múltbeli, a létszámkorlátnak pedig pozitív egész számnak kell lennie.
Hiba esetén jelenjen meg a megfelelő hibaüzenet, különben kerüljön hozzáadásra a rendezvény az adatbázishoz.
