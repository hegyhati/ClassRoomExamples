# Bevezetes a programozasba ZH
2021.12.12

## Kód interpretálás
Mit ír ki az alábbi program?

```javascript
let text = "God Gjetost Abundant?!"
let a = 0
let b = 1
console.log(a, text[a])
while ( b < text.length ){
  console.log(b, text[b])
  b += a
  a = b-a
}
```

## Kód készítés
Készíts honlapot, mely a télapónak segít a listájáinak összeállításában.
 - Legyen egy hely, ahol meg lehet adni a gyerek nevét.
 - Vagy legyen egy hely, ahol ki lehet választani, hogy jó vagy rossz volt, és egy gomb, amivel hozzá lehet adni a kiválasztott listához.
 - Vagy legyen két gomb, az egyik a jó, a másik a rossz gyerekek listájához adja hozzá.
 - Legyen listája a jó és a rossz gyerekeknek.
 - Dobd fel az oldalt valami mókás karácsonyi képpel. 
  
Bónusz: valahol írja ki, hogy a gyerekek hány százaléka jó. 
