## 1. zárthelyi feladat

Egy hírportál cikkeinek szűrését és megjelenítését végző parancssoros Python programot kell készíteni.

A cikkek tartalma és adatai a [cikkek.json](cikkek.json) fájlban, egy objektumokból álló tömbben vannak tárolva.
Az objektumok az alábbi kulcs-érték párokat tartalmazzák:

- `id`: a cikk egyedi azonosítója (`int`)
- `title`: a cikk címe (`str`)
- `content`: a cikk szövege (`str`)
- `tags`: a cikk témáját jelölő kulcsszavak címkék listája (`list[str]`)
- `date`: a cikk megjelenési dátuma YYYY-MM-DD formátumban (`str`)

A program indításkor olvassa be a fájlt, írja ki, hány cikket talált benne, majd jelenítse meg a főmenüt:

```
9 cikk sikeresen betöltve.
Válasszon menüpontot:
1: Keresés szöveggel
2: Szűrés címkére
3: Szűrés időintervallumra
0: Kilépés
Választás: 
```

Nem kell ellenőrizni, hogy számot adtak-e meg, csak azt, hogy milyen számot.

Az 1-3 menüpont elvárt működését a következő fejezetek taglalják.
A menüpont végrehajtása után jelenjen meg újra a főmenü, amíg a Kilépés (0) opciót nem választják.

### 1: Keresés szöveggel

A program kérje be a keresendő szöveget, ami egy egysoros string.
A `get_ids_by_text` függvény kapja meg a cikkek adatait, a keresendő stringet, és adja vissza a találatokat egy id-ket tartalmazó listaként.
Akkor számít egy cikk találatnak, ha a teljes keresendő string szerepel a címében vagy szövegében, a kis- és nagybetűket figyelmen kívül hagyva.

A `show_titles` függvény kapja meg a cikkek adatait és az eredménylistát, majd jelenítse meg az id-kat és a cikkek címeit, soronként egyet.

Példa:
```
Keresendő kifejezés: gól
1: Minden idők leggyorsabb német válogatott góljával verték meg a franciákat
3: 17 éves góljával verték a brazilok Angliát idegenben
```

Ezután a program kérje be az elolvasandó cikk id-ját, vagy 0-t a főmenübe való visszalépéshez:
```
Kérem az ID-t (vagy 0: vissza a menübe): 2
Nincs ilyen ID a találatok között!
Kérem az ID-t (vagy 0: vissza a menübe): 3
```

Nem kell ellenőrizni, hogy számot adtak-e meg, csak azt, hogy milyen számot.

A `show_article` függvény kapja meg a cikkek adatait és a kiválasztott id-t, majd jelenítse meg a cikket az alábbi formázással:

```
# <Cím>
*Megjelent: <dátum YYYY.MM.DD. formátumban>*

<Cikk szövege>

Címkék: <címkék felsorolása, vesszővel elválasztva>
```

Ezután jelenjen meg újra a főmenü.


### 2: Szűrés címkére

A `collect_tags` függvény kapja meg a cikkek adatait, és adja vissza az előforduló címkék (tag-ek) halmazát.

A program írja ki a címkék vesszővel elválasztott listáját, és kérjen be egyet a szűréshez.
Ha a megadott string nem egy létező címke vagy a "back" parancs, akkor ismételje meg a bekérést.

A `get_ids_by_tag` függvény kapja meg a cikkek adatait és a választott címkét, és térjen vissza azon cikkek id-jait tartalmazó listával, melyek tag-jei között szerepel a megadott címke.

Innentől a szöveges kereséshez hasonlóan kerüljön listázásra a találati lista és megjelenítésre a kiválasztott cikk, majd jelenjen meg a főmenü.

Példa:
```
Címkék:
felsőoktatás, Anglia, időjárás, Endrick, ISIS, Budapest, terrorizmus, vadvirág, sport, rendőrség, Kecskemét, poszméh, Svédország, baleset, zivatar, egyház, Franciaország, Németország, ELTE, méh, figyelmeztetés, foci, béremelés, Brazília, gyermek, haláleset, méhlegelő, pápa
Választott címke (vagy "back" a visszalépéshez): német
Nincs ilyen címke!
Választott címke (vagy "back" a visszalépéshez): Németország
Találatok:
1: Minden idők leggyorsabb német válogatott góljával verték meg a franciákat
8: Két embert letartóztattak Németországban a svéd parlament ellen tervezett merénylet miatt
```

### 3: Szűrés időintervallumra

A program kérje be az intervallum kezdő- és végdátumát YYYY-MM-DD formátumban.
A formátumot és a dátum érvényességét nem kell ellenőrizni.

A `get_ids_by_date` függvény kapja meg a cikkek adatait, valamint a kezdő- és végdátumot, és adja vissza azon cikkek id-jait egy listában, melyek a megadott zárt időintervallumban jelentek meg.
(Mivel a dátumok szabványos ISO formátumban vannak, elegendő stringként összehasonlítani őket.)

Innentől a szöveges kereséshez hasonlóan kerüljön listázásra a találati lista és megjelenítésre a kiválasztott cikk, majd jelenjen meg a főmenü.

Példa:
```
Kérem a kezdődátumot (YYY-MM-DD): 2024-01-01
Kérem a végdátumot (YYY-MM-DD): 2024-03-20
Találatok:
6: Nettó 280 ezret sem keres egy adjunktus, ezer ELTE-s követel béremelést
8: Két embert letartóztattak Németországban a svéd parlament ellen tervezett merénylet miatt
```
