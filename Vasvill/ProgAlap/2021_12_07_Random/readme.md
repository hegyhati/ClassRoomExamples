# Uj anyag

 - `import random`
 - `random.randint(min,max)`
 - `random.randrange(min,max+1)`
 - `random.uniform(min,max)`
 - `random.gauss(average,deviation)`
 - `random.shuffle(list)`
 - `random.choice(list)`
 - `random.choices(list,k=count)`
 - `random.sample(list,k=count)`

# Forrasok
 - [Python referencia](https://docs.python.org/3/library/random.html)
 - [W3Schools](https://www.w3schools.com/python/module_random.asp)
 - [GeeksforGeeks] (https://www.geeksforgeeks.org/python-random-module/)

# Gyakorlofeladatok

### Ismetles
A program dobaljon egy hatoldalu dobokockaval (es irja ki a dobasokat) addig, amig egyszer olyat nem dob, ami mar volt.
Peldakimenetek lehetnek:
 - `1,4,3,5,1`
 - `1,4,3,4`

Segitseg: hasonlit a "kerjunk be szamokat addig, amig ismetlodes nincs" feladathoz, csak most nem bekerjuk, hanem `randint`/`randrange`-dzsel generaljuk.

### Ko-papir-olloo
Ket jatekos veletlenszeruen jatszik ko-papir-ollot. Irjuk ki, melyikojuk melyiket valasztotta. Ha van nyertes, irjuk ki, ha nem, akkor ujra.

pl:
```
Jatekos 1: Ko
Jatekos 2: Papir
Jarekos 2 nyert.
```
vagy:
```
Jatekos 1: Ollo
Jatekos 2: Ollo
Ujra.
Jatekos 1: Ko
Jaetkos 2: Ko
Ujra.
Jatekos 1: Papir
Jatekos 2: Ollo
Jatekos 2 nyert.
```

Segitseg: `choice`-ot erdemes hasznalni, es az indexekkel lehet konnyebb leellenorizni, hogy ki nyert.

### Kockapoker/yatzee 
A program dobjon 5 db hatoldalu dobokockaval, majd irja ki a dobasokat egy sorban. Ezutan irja ki, ha van:
 - Kockapoker: mind az 5 megegyezik.
 - Drill: van 3 egyforma
 - Ketpar: van 2-2 egyforma
 - Par: van 2 egyforma
 - Sor: kijott az 1-2-3-4-5 vagy a 2-3-4-5-6

Segitseg: a tesztelesekre erdemes kulon-kulon fuggvenyeket irni, amik megkapjak a dobasok listajat, es ebbol mondanak egy igent,nemet. A dobasokat erdemes lehet sorba rendezni az ellenorzesekhez.

### Szamkitalalo
A program gondoljon egy szamra, nekunk addig kell tippelnunk, mig ki nem talaljuk. Minden tipp utan a proogram megmondja, hogy eltalaltuk, vagy annal nagyobb, kisebb.

Segitseg: teszteleshez erdemes "csalni" ugy, hogy rogton kiirjuk a gondolt szamot.
