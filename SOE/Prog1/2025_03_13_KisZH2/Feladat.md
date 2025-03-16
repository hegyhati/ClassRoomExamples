# Programozás 1 - KisZH2

Adott egy `trains.json` fájl, amiben vonatjáratok adatai vannak eltárolva.
A teljes json egy lista, amiben minden dictionary egy járat:

```json
{
    "train_id": 23,
    "seat_resevation": false,
    "departure": "06:41",
    "stations": [
      "D",
      "F",
      "G",
      "H",
      "K",
      "V",
      "X",
      "Y",
      "Z"
    ]
  },
```

Itt a `stations` egy lista, ami tartalmazza az állomásokat, ahol megáll a vonat.

## Feladat

Írj programot, amely beolvassa a json tartalmát, majd bekéri az indulás óráját (egész szám),
és kiírja azon állomások neveit, amiket érint legalább egy olyan vonat, ami a megadott órában indul.
Minden érintett állomást csak egyszer írjon ki, tetszőleges sorrendben.
Ha nincs ilyen állomás, akkor írja ki, hogy "No trains at this time.".

Példák:

```
Hour of departure? 8
Destinations:
Bicske
Sopron
Fertoszentmiklos
Komarom
Tata
```

```
Hour of departure? 14
No trains at this time.
```
