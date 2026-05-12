# Algorithmen und Datenstrukturen Test 2 - 2025.05.06.

## Theorie 

### T1. Sortiertheorie - 2p

Nenne zwei Sortieralgorithmen, die unterschiedliche Laufzeiten im Best- und Worst-Case haben. Erkläre in 2–3 Sätzen, warum das so ist und worin der Unterschied besteht.

### T2. Ja/Nein Fragen - 2p
Geben Sie an, ob die Aussagen wahr oder falsch sind, und begründen Sie Ihre Antwort in einem Satz.

 -  Merge sort kann für kein Array langsamer sein als Insertion sort.
 -  Heapsort ist in-place.

## Praxis

### P1. BST Operationen - 3p

Beginnen Sie mit folgendem Baum: `19-(6-(3-1-())-())-34`  
(Die Notation lautet: `Elternknoten-(linkes Kind)-(rechtes Kind)`)

Führen Sie die folgenden Operationen aus und zeichnen Sie den Zustand des Baums nach jeder Operation:

 - `push(2)`
 - `delete_max()`
 - `push(7)`

Geben Sie die Preorder-Traversierung für den finalen Baum an.

### P2. Heap Operationen - 4p

Beginnen Sie mit folgendem Max-Heap: `[34,13,2,5,8,1]`

Führen Sie die folgenden Operationen aus und zeichnen Sie den Zustand des Heaps nach jeder Operation:
 - `push(21)`
 - `pop_max()`
 - `push(7)`
 - `pop_max()`
 - `pop_max()`

### P3. Partitionierung - 2p

Verwenden Sie die gelernte Methode, um diesen Abschnitt des Arrays Schritt für Schritt zu partitionieren:

```
... | 1 , 2 , 7, 3 , 9 , 4 | ...
```

## Codeanalyse und Korrektur - 4p

```C
int* foobar(int* array, int size) {
    int count = 0;
    for (int i = 0; i < size-1; ++i)
        if (array[i] > array[i+1])
            ++count;
    int* starts = malloc(count*sizeof(int));
    count = 0;
    starts[count++] = 0;
    for (int i = 0; i < size-1; ++i)
        if (array[i] > array[i+1])
            starts[count++] = i+1;
    return starts;   
}
```
Was ist die Zurückgabe für diesen Aufruf: `foobar({1,5,8,2,3,6,4,7,9},9)`

Was macht diese Funktion allgemein (in einem Satz)?

Warum ist er falsch? Korrigieren Sie ihn.

Was ist die Laufzeit der Funktion?

Für welchen Sortieralgorithmus könnte diese Funktion nützlich sein? Wie/Warum?
