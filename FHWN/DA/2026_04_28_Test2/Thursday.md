<style>
code:not(pre code) {
    color: blue !important;
}
</style>

# Algorithmen und Datenstrukturen Test 2 - 2025.05.07.

## Theorie 

### T1. Sortiertheorie - 2p

Nenne zwei Sortieralgorithmen, die gleiche Laufzeiten im Best- und Worst-Case haben. Erkläre in 2–3 Sätzen, warum das so ist.

### T2. Ja/Nein Fragen - 2p
Geben Sie an, ob die Aussagen wahr oder falsch sind, und begründen Sie Ihre Antwort in einem Satz.

 -  In einem Min-Heap ist das rechte Kind immer größer als sowohl der Elternknoten als auch das linke Kind.
 -  Merge Sort ist stabil.


## Praxis

### P1. BST Operationen - 3p

Beginnen Sie mit folgendem Baum: `19-(6-(3-1-())-())-34`  
(Die Notation lautet: `Elternknoten-(linkes Kind)-(rechtes Kind)`)

Führen Sie die folgenden Operationen aus und zeichnen Sie den Zustand des Baums nach jeder Operation:

 - `push(TT)`
 - `delete_max()`
 - `push(MM)`

Wobei TT.MM Ihr Geburtstag ist. Geben Sie die Postorder-Traversierung für den finalen Baum an.

### P2. Heap Operationen - 4p

Beginnen Sie mit folgendem Max-Heap: `[34,13,5,1,8,2]`

Führen Sie die folgenden Operationen aus und zeichnen Sie den Zustand des Heaps nach jeder Operation:
 - `push(21)`
 - `pop_max()`
 - `push(7)`
 - `pop_max()`
 - `pop_max()`

### P3. Partitionierung - 2p

Verwenden Sie die gelernte Methode, um diesen Abschnitt des Arrays Schritt für Schritt zu partitionieren:

`... | 1 , 7 , 2 , 3 , 9 , 4 | ...`

## Codeanalyse und Korrektur - 4p

```C
LLNode* foobar(LLNode* head) {
    LLNode* const other_head = head;
    while (head->next->value >= head->value)
        head = head->next;
    LLNode* other_last = head;
    head = head -> next;
    LLNode* tmp = head;
    while (tmp->next != NULL) {
        if (tmp->next->value < other_last->value) {
            tmp = tmp->next;
        } else {
            other_last->next = tmp->next;
            tmp->next = tmp->next->next;
            other_last = other_last->next;
        }
    } 
    other_last->next = NULL;
    return other_head;
}
```
Was ist die zurückgegebene verkettete Liste, wenn head auf die folgende verkettete Liste zeigt:

```
head -> 1 -> 3 -> 7 -> 4 -> 9 -> 3 -> NULL
```

Was macht diese Funktion allgemein (in einem Satz)?

Nennen Sie einige Fehler bzw. nicht behandelte Sonderfälle im Code.

Was ist die Laufzeit der Funktion?

Für welchen Sortieralgorithmus könnte diese Funktion nützlich sein? Wie/Warum?
