# Algorithmen und Datenstrukturen Test 2 Beispiel

## Theorie 

### T1. Sortiertheorie - 2p

Nennen Sie einen Sortieralgorithmus, der eine lineare Best-Case-Laufzeit hat. Erklären Sie in wenigen Sätzen warum.

### T2. Ja/Nein Fragen - 3p
Geben Sie an, ob die folgenden Aussagen wahr oder falsch sind, und begründen Sie Ihre Antwort in einem einzigen Satz.

 -  Quicksort benötigt (asymptotisch) mehr Speicher als Heapsort.
 -  Insertionsort kann für kein Array schneller sein als Quicksort.
 -  In einem Max-Heap sollte das linke Kind immer kleiner sein als das rechte Kind.

## Praxis

### P1. BST Operationen - 4p

Beginnen Sie mit folgendem Baum: `19-(6-(3-()-(5))-())-(34-()-(63))`  
(Die Notation lautet: `Elternknoten-(linkes Kind)-(rechtes Kind)`)

Führen Sie die folgenden Operationen aus und zeichnen Sie den Zustand des Baums nach jeder Operation:

 - `push(42)`
 - `push(7)`
 - `delete(6)`
 - `delete_max()`

Geben Sie für den finalen Baum an:
 
 - Preorder-Traversierung: 
 - Inorder-Traversierung: 
 - Postorder-Traversierung: 

### P2. Heap Operationen - 4p

Beginnen Sie mit folgendem Max-Heap: `[55,21,34,13,2,5,8,1,3]`

Führen Sie die folgenden Operationen aus und zeichnen Sie den Zustand des Heaps nach jeder Operation:
 - `push(35)`
 - `push(21)`
 - `pop_max()`
 - `push(7)`
 - `pop_max()`
 - `pop_max()`

## Codeanalyse und Korrektur - 4p

Welcher Sortieralgorithmus ist unten implementiert:

```C
void magic_sort(int* array, int size) {
    int *p, *c, t;
    for(c=array; c<array+size; ++c) {
        for(p=array; p<array+size; ++p) {
            if (*p < *c) {
                t = *p;
                *p = *c;
                *c = t;
            }
        }
    }
}
```

Warum ist er falsch? Korrigieren Sie ihn.

Wie ist die Laufzeit im Best-/Average-/Worst-Case?