# Programozas 1 - KisZH2 - Minta

Adott egy `data.json` file, amiben vonatjaratok adatai vannak eltarolva.
A teljes json egy lista, amiben minden dictionary egy jarat:

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

Itt a `stations` egy lista, ami tartalmazza az allomasokat, ahol megall a vonat.

## Feladat

Irj programot, mely beolvassa egy megallo nevet es kiirja azon jaratoknak az id-jet, amik megallnak az adott allomason es **nem** helyjegykotelesek (`seat_reservation`).


