# Levelező minta ZH 
2025.04.18.

# Igaz-Hamis állítások
Adottak az alábbi állítások. Döntse el, hogy igazak-e vagy hamisak.
 - A bináris keresőfa magassága legrosszabb esetben $O(n)$.
 - Dinamikus tömbben adott indexű elem keresése $O(1)$ időben végezhető.
 - Láncolt listában minimum keresése $O(n)$ időben végezhető.
 - Min-kupacban minimum keresése $O(\log(n))$ időben végezhető.
 - Adjacencia mátrixban egy csúcs szomszédainak kilistázása $O(n)$ időben végezhető.
 - A Kruskal algoritmus csak páros gráfokhoz adja meg a minimális feszítőfát.
 - Dijkstra algoritmusa működik negatív élt tartalmazó gráfokon, ha körmentesek.
 - A Counting sort helyben rendez.

# Aszimptotikus jelölések
Adottak az alábbi függvények, illetve függvényhalmazok. Kösse össze azokat, ahol a tartalmazás fennáll. 
| Függvények | <span style="display:inline-block; width:100px; visibility:hidden;"></span>| Függvényhalmazok |
|------------|---|------------------|
| $n^2$ || $o(n)$ |
| $n^3$ || $O(n^2)$ |
| $n^2 + 123n$ || $\Theta(n^3)$ |
| $n^2 \log n$ || $\omega(n^4)$ |
| $\log(n^2)$ || $\Omega(n^5)$ |
| $n + \log(n)$ || 

# Bináris keresőfa
Készítsen egy bináris keresőfát a következő számok sorrendben történő beillesztésével: 15, 23, 7, 12, 24, 36, 48, 25, 6. 
Rajzolja fel a fa ezen állapotát, majd mindegyik alábbi lépés után is, azokat sorrendben végrehajtva:
 - 12 törlése
 - 18 beszúrása
 - 7 törlése
 - 15 törlése

A végleges fában adja meg a csúcsok pre-, in- és postorder bejárásának sorrendjét.

# Kupac
Készítsen max-kupacot az alábbi tömbből a tanult eljárással:
```
[23, 11, 24, 51, 35, 19, 2, 16, 35]
```
Rajzolja fel a kupac ezen állapotát, majd mindegyik alábbi lépés után is, majd háromszor törölje ki a legnagyobb elemet a kupacból, és rajzolja fel a kupac ezen állapotát.

# Rendezések
Nevezzen meg egy olyan rendező algoritmust, mely legrosszabb esetben $O(n^2)$ időben rendez.

Nevezzen meg egy **másik** rendező algoritmust, mely stabil.

Nevezzen meg egy **harmadik** rendező algoritmust, mely mindkét tulajdonsággal rendelkezik. 

Végül nevezzen megy egy negyediket, mely egyikkel sem.

# Partícionálás
A tanult algoritmussal partícionálja az alábbi tömböt. (A pivot az utolsó elem.)
```
[23, 11, 24, 51, 35, 19, 2, 16, 35]
```

# Láncolt lista
Adott az alábbi egyszerű láncolt lista elem:
```c
typedef struct LLnode {
    int data;
    struct LLnode *next;
} LLNode;
```
Készítsen függvényt az alábbi szignatúrával, mely a Stalin sort algoritmust valósítja meg, azaz kitörli a nem növekvő sorrendben lévő számokat. Feltételezheti, hogy a lista nem üres.
```c
void stalin_sort(LLNode *head);
```
Példa:
```
head -> 1 -> 8 -> 3 -> 14 -> 5 -> NULL
stalin_sort(head);
head -> 1 -> 8 -> 14 -> NULL
```

# Mélységi bejárás
Az `B` csúcsból indulva végezze el a mélységi bejárást az alábbi gráfban, és adja meg az egyes csúcsok érkezési és távozási idejét. A gyerekek bejárásának sorrendje ábécé szerint történik. 

![Mélységi bejárás](dfs.svg)

# Minimális feszítőfa

Adja meg a minimális feszítőfát az alábbi gráfban Prim algoritmusával, a `B` csúcsból indulva. 

![Minimális keresőfa](mst.svg)

