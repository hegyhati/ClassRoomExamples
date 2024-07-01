# PótpótZH

## Feladat

A feladat egy olyan raktárkezelő program készítése, ami több helyszínen tud termékeket kezelni. És adatbázisként egy `json` file-t használ.

Az egyszerűség kedvéért jelenleg csak 2 fix helyszínt kell tudnia kezelni a programnak. (Ezek a `locations.json` fileból kerüljenek beolvasásra). Adatbázisként is ez a file szolgál.

A feladat egy olyan CLI alkalmazás készítése, ami az egyes helyszíneken való raktárkészlet kezelését könnyíti meg.

### Főoldal

Az alkalmazást elindítva a felhasználónak legyen lehetősége egy listából kiválasztani az éppen aktuális helyszínt.
Amennyiben a programot a `-l <id>` argumentummal indítjuk el, ez a kérdezés ne történjen meg.

Miután a helyszínt megadtuk, az alkalmazás listázza ki az elérhető termékeket.

### Részletek

A termékek listájából, ha a felhasználó kiválaszt egyet, akkor egy új almenübe kerüljünk a következő funkciókkal:

- mennyiség csökkentése (kérdezze meg, hogy mennyivel)
- mennyiség növelése (kérdezze meg, hogy mennyivel)
- adott mennyiség áthelyezése másik helyszínre (kérdezze meg, hogy mennyi)
- átnevezés
- termék törlése

Ezen felül írja ki a termékből elérhető mennyiséget is.

### Új termék

Új termék felvételére is teremtse meg a lehetőséget.

A program `-n` kapcsolóval való indítása esetén kérje be a következő adatokat a program:

- termék neve
- termék mennyisége
- termék azonosítója (ha nincs megadva, generálja automatikusan a program)
- termék helyszíne (listából lehessen kiválasztani)

Az adatok megadását követően a program kérdezze meg, hogy a felhasználó szeretne-e felvenni további termékeket.
Amennyiben nem, akkor a program lépjen ki.

### Statisztika

A programot a `-stats` kapcsolóval elindítva készítsen egy grafikont, amin látszik, hogy melyik helyszínen az egyes termékekből mekkora mennyiség található. (két al-grafikon, ahol `bar` diagramon fel vannak tüntetve a termékek nevei és a mennyiségük)

## EXTRA

Kényelmi funkciók megvalósítása.

A programban legyen lehetőség a mennyiségek csökkentésére a `-m` kapcsoló megadásával. A kapcsoló megadásakor a program várjon egy kötelező `<id>` argumentumot és egy mennyiséget pl: `-10`, `+10`.

A program ekkor írja ki, hogy melyik termék és hogyan változott `Termék 1: 10 -> 20`
