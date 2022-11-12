# Próba ZH
2021.11.29.

## Mit ír ki az alábbi program?
```javascript
let x = 10
while ( x != 1 ){
    console.log(x)
    if ( x % 2 == 1 ) x = 3 * x + 1
    else x /= 2
}
```

## Programozás
Készíts weboldalt, ahol egy megépítendő lakás szobáit lehet felvenni egy listába. Mindegyiknek van neve, valamint az hogy hányszor hány méteres. A listában a felvitt szobák így jelenjenek meg:

 - Nappali, 15 nm: 3x5
 - Hálószoba, 8 nm: 4x2
 - ...

Bónusz: Egy külön helyen legyen összesítve a ház teljes alapterülete.

Bónusz2: Az alapterület mellett írja ki azt is, hogy hányféleképpen jöhet ki az az alapterület. Pl:

Alapterület : 48 nm
 - 1 x 48
 - 2 x 24
 - 3 x 16
 - 4 x 12
 - 6 x 8

