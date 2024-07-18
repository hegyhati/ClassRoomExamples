# BevProg cheat sheet

## Skeleton 

Minden feladat esetében az alábbi skeletonból indulhatunk ki:

```html
<html>
    <head>
        <script>
            // JS kod (mukodes)
        </script>
    </head>
    <body>
        HTML kod (feluleti elemek, megjelenes)
    </body>
</html>
```

## Alap HTML elemek

Bővebb lista, részletesebb leírások a [W3Schools](https://www.w3schools.com/html/) oldalán, de az általunk használt fontosabb dolgok egyben:

### SPAN 
```
    <span> szoveg </span>
```
"Nem csinál semmit", de használhatjuk, ha egy adott részhez `id`-t szeretnénk rendelni később

### Listák

Pottyos lista:
```html
    <ul>
        <li>Elso elem</li>
        <li>Masodik elem</li>
    </ul>
```

Sorszámozott lista:
```html
    <ol>
        <li>Elso elem</li>
        <li>Masodik elem</li>
    </ol>
```

### Sortörés
```html
    <br />
```

### Beviteli mező
Egyszerű szövegbeviteli mező:
```html
    <input id = "fieldid" >
```

Alapértelmezetten szöveg (`type="text"`), de állítható másra is, pl az alábbi számot kér be (de megenged beírni alapértelmezetten mást is):

```html
    <input type = "number" id = "fieldid" >
```

### Gomb

```html
    <button onclick="function_name()"> Gomb szovege </button>
```

## JS alapok

### Változó létrehozása

```js
    let valtozo_neve = kezdeti_ertek;
```

Változóknak lehet különböző típusa, pl:
```js
    let szoveg_valtozo = "Szoveg konstansok mindig macskakormok vagy aposztrofok kozott"
    let szam_valtozo = 12.3 // Egysoros komment ket per jel utan
    let logikai_valtozo = true // masik lehetseges ertek a false
```

Ezek között lehet konvertálni, pl:
```js
    let szoveg_valtozo = "12.23"
    let szam_valtozo = Number(szoveg_valtozo)
```

### Elágazás
```js
    if ( /* logikai kerdes */ ) {
        // mi tortenjen ha igaz
    } else {
        // mi tortenjen ha hamis
    }
```

### Egyszerű ciklus
```js
    while ( /* logikai kerdes */ ) {
        // Ismetlendo utasitas, amig igaz
    }
```

### Függvények
Argumentum nélküli egyszerű függvény:
```js
    function fuggveny_neve () {
        // Utasitasok
    }
```

Melyet `fuggveny_neve()` -vel hívhatunk meg a kódban máshonnét.

### Fapados interakció

Egyszerű kiiratás:

```js
    alert("Kiiratando szoveg")
```

Ha szeretnénk benne változók értékeit megjeleníteni, akkor  `` ` ``-et kell használnunk, és a változók körül `${}`-et:

```js
    alert(`Az ${a} es ${b} szamok osszege ${a+b}`)
```

Egyszerű beolvasás, ami mindig szöveg formában adja vissza a felhasználó által adott értéket, tehát ha számot kérünk be, akkor konvertálni kell:
```js
    let szoveg_valtozo = input("Kiirando bekero szoveg)
    let szam_valtozo = Number(input("Szamot bekero szoveg"))
```

## HTML - JS együtt

### Függvény bekötése gombkattintásra

```html
<html>
    <head>
        <script>
            function fuggveny_neve () {
                // ...
            }
        </script>
    </head>
    <body>
        ...
        <button onclick="fuggveny_neve()">Gomb szovege</button>
    </body>
</html>
```

Fontos, hogy a `fuggveny_neve` pontosan ugyanaz legyen mindkét helyen

### Érték kiolvasása `input` -ból

```html
<html>
    <head>
        <script>
            let szoveg_valtozo = document.getElementById("input_id").value
        </script>
    </head>
    <body>
        ...
        <input id="input_id">
    </body>
</html>
```

Fontos, hogy az `input_id` pontosan ugyanaz legyen, mind a két helyen.

Hasonló a kód, ha egy nem `input` elemből akarunk kiolvasni, hanem pl egy `span`-ből:
```html
<html>
    <head>
        <script>
            let szoveg_valtozo = document.getElementById("input_id").innerHTML
        </script>
    </head>
    <body>
        <span id="input_id">Kiolvasando szoveg</span>
    </body>
</html>
```

`value` helyett `innerHTML`, és hasonlóan működik `<b>`, `<h1>` vagy bármilyen más tag-re is.

### Új érték kiírása

```html
<html>
    <head>
        <script>
            document.getElementById("span_id").innerHTML = "valamilyen szoveg"
        </script>
    </head>
    <body>
        <span id="span_id"></span>
    </body>
</html>
```

Ha hozzáfűzni szeretnénk a kiírt szöveghez, nem felülírni, akkor `=` helyett `+=`, ezt gyakran listáknál használtuk, pl:

```html
<html>
    <head>
        <script>
            document.getElementById("lista_id").innerHTML += `<li>${valtozo}</li>`
        </script>
    </head>
    <body>
        <ul id="lista_id"></span>
    </body>
</html>
```

## Összetettebb eszközök

### Tömbök

Üres tömb létrehozása:

```js
    tomb_valtozo = []
```
Tömb x. elemének lekérdezése (indexelés 0-tól indul):
```js
    tomb_valtozo[x]
```

Hozzáfűzés a tömb végére:
```js
    tomb_valtozo.push("uj elem")
```

Tömb mérete a `tomb_valtozo.length`-ben elérhető.

Annak ellenőrzése, hogy egy adott érték benne van-e a tömbben:

```js
    if (tomb_valtozo.indexOf("keresett elem") != -1 ){
        // utasitasok, ha benne van a tombben
    } else {
        // utasitasok, ha nincs benne a tombben
    }
```
