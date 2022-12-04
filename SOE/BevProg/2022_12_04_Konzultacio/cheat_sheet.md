# Cheat sheet

## JS 

Valtozo letrehozasa: 
```javascript
let valtozonev
```

Bemenet bekeres:
```javascript
valtozonev = prompt("Szoveg a bekereshez")
valtozonev = Number(prompt("Ha szamot szeretnenk"))

```

Kiiratas:
```javascript
alert("Szoveg, amit ki akarunk iratni")
alert(valtozonev)
```

Fuggveny:
```js
function fuggvenynev(argumentumlista){
    utasitasok
}
```

## HTML

Skeleton:
```html
<html>
    <head>
        <script src="valami.js"></script>
        <title>Az oldalam cime</title>
    </head>
    <body>
        A honlap tartalma
    </body>
</html>
```

Beviteli mezo:

```html
<input id="azonosito">
```

Lista:
```html
<ul>
    <li>elso elem</li>
    <li>masodik elem</li>
</ul>
```

Nyomogomb:
```html
<button onclick="fuggvenynev()">Gomb szovege</button>
```

## HTML + JS

Nyomogomb osszekotese fuggvennyel:

```html
    <button onlclick="FOO()">Gombszoveg</button>
```
```js
    function FOO(){
        Ez lesz vegrehajtva a gombra kattintaskor
    }
```

