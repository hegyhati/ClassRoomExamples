# Adatstruktúrák és Algoritmusok Minta ZH

Rendelkezésre álló idő: 60 perc
Semmilyen segédeszköz nem használható.

## 0. Feladat: [I/H] 
Mely állítások igazak, hamisak az alábbiak közül?
 - A merge sort egy már (jó irányban) rendezett tömbön O(n) idő alatt fut le.
 - A quick sort minden esetben O(nlogn) idő alatt lefut.
 - Láncolt lista végére gyorsabb a beillesztés, mint a végére.
 - Dinamikus tömbből aszimptotikusan lassabb kitörölni a középső elemet, mint láncolt listából.
 - A selection sort gyorsabban fut egy jól rendezett tömbön, mint egy véletlenszerűen megkeverten.
 - Összehasonlításon alapuló rendező algoritmusok esetében a legjobb worst case futási idő O(n^2).
 - Bináris keresőfában a legkisebb elem átlagosan O(1) időben megadható.

## 1. Feladat: O(?)
Milyen aszimptotikus futási ideje van (legrosszabb esetben) az alábbi kódrészletnek `n=len(l)` függvényében? A választ indokolja.

```python
l2 = l[:]
for idx in range(len(l)//2):
    if l[idx] != l[-idx-1]:
        if l[idx] not in l2: l2.append(l[idx])
        if l[-idx-1] not in l2: l2.append(l[-idx-1])
        l[idx] = l[-idx-1] = (l[idx]+l[-idx-1]) // 2
```

## 2. Feladat: HEAP

Adott egy `MIN-HEAP` a `[6,8,9,11]` elemekkel. Hogy néz ki a kupac tartalma az alábbi műveletek után? (tömb és fa):
 1. `push(5)`
 2. `push(-2)`
 3. `pop_min()`
 4. `push(99)`


## 3. Feladat: Sort
Rendezze az alábbi tömböt merge sorttal: `[1,8,6,4,9,23,2,7,55,-9,5]`. A rendezés köztes lépései látszódjanak.

## 4. Feladat: Sort 2
Írja le a quick sort műküdési elvét, legjobb, legrosszabb, átlagos futási idejét. 
Bónusz: adja meg az algoritmus pseudo kódját / python implementációját.

## 5. Feladat: BFS
Adott egy üres bináris keresőfa, mi a fa állapota (ábrákkal) az alábbi lépések után?
 1. `push(9)`
 2. `push(6)`
 3. `push(-6)`
 4. `push(63)`
 5. `push(16)`
 6. `push(61)`
 7. `push(8)`
 8. `delete(16)`
 9. `push(5)`
 10. `push(7)`
 11. `push(15)`
 12. `push(16)`
 13. `delete(9)`
 14. `delete(8)`


