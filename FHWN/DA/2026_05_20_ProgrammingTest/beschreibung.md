# Allgemeine Regeln

 - Verfügbare Zeit: 8:30-10:30
 - Den Raum verlassen = Abgabe.
 - Keine externen Ressourcen erlaubt.
 - Von anderen kopieren führt sofort zu 0 Punkten.
 - Code kompiliert nicht: 0 Punkte.
 - Code verursacht einen Segfault: 0 Punkte.
 - Code hat Memory Leaks: Punkte halbiert.
 - Nicht alle Aufgaben müssen gelöst werden, du kannst auswählen, auf welche Aufgaben du dich konzentrierst. Siehe unten.
 - Arbeite nur in der Datei `test.c` und lade am Ende auch nur diese auf Moodle hoch.
 - `main` darf überhaupt nicht verändert werden, du musst Platzhalter bereitstellen, damit die oben genannten Kriterien auch für nicht korrekt implementierte Funktionen erfüllt werden.
 - Lies die Beschreibungen sorgfältig. Es ist besser Fragen früher zu stellen und Unklarheiten zu beseitigen, falls etwas nicht vollständig verstanden wurde.
 - Wenn ihr einen Tippfehler/Fehler seht, sagt uns sofort Bescheid. Falls es tatsächlich einer ist, werden wir ihn an alle weitergeben.

# Hundeschutzheim

Wir sind die IT-Leute eines Hundeschutzheims und müssen mehrere Aufgaben erledigen, die uns aufgetragen wurden.

## Die „Datenbank“

Wir haben zwei Dateien, die Informationen über die Hunde und frühere Vorfälle enthalten.

### `dog_data.txt`

Die Datei hat folgende Struktur und enthält den Namen, das Alter und die Rasse jedes Hundes in unserem Heim.

```
Number of dogs: 123
Name: Peppy_Sadie Age: 2 Breed: Australian_Cattle_Dog
Name: Jolly_Athena Age: 3 Breed: Boston_Terrier
Name: Noisy_Winston Age: 8 Breed: Brittany
Name: Grouchy_Archie Age: 3 Breed: Cocker_Spaniel
Name: Bouncy_Annie Age: 7 Breed: Rottweiler
...
```

### `incident_data.txt`

Auch wenn Hunde die Besten sind, mögen sie sich leider nicht immer, und es kann zu Streitigkeiten kommen, wenn Freiwillige mit ihnen spazieren gehen.  
Diese Datei enthält ein Protokoll solcher Ereignisse in folgendem Format:

```
2025-01-01: Mellow_Ellie attacked Tiny_Tank
2025-01-04: Rowdy_Chloe attacked Wacky_Callie
2025-01-07: Grumpy_Josie attacked Mighty_Lucky
2025-03-01: Snuggly_Lola attacked Curious_Otis
2025-04-05: Grumpy_Zeus attacked Tiny_Zeus
...
```

### Weitere Eingaben

Du kannst Größe/Inhalt der Eingaben gerne ändern, wenn es beim Debuggen hilft. Mit `python3 generate.py` kannst du neue Eingabedateien beliebiger Größe (bis zu 5000 Hunde) generieren.

## Aufgaben

### Geordnete Liste der Hunde

Die meisten Menschen bevorzugen jüngere Hunde bei der Adoption.  
Deshalb sollen wir eine nach Alter sortierte Liste der Hunde bereitstellen.  
Da viele Hunde gleich alt sind, sollen Hunde innerhalb derselben Altersgruppe zusätzlich nach Namen sortiert werden.

### Größere Zwinger

Aktuell lebt jeder Hund in einem sehr kleinen Einzelzwinger.  
Es wäre schöner, ihnen mehr Platz zum Herumlaufen zu geben, aber wegen Platzmangel ist das nur möglich, wenn mehrere Hunde gemeinsam in größere Zwinger gesetzt werden.

Natürlich wollen wir keine Kämpfe, und um die Anzahl der Zwinger zu minimieren, müssen wir die Hunde geschickt aufteilen.  
Zwei Hunde dürfen nicht im selben Zwinger sein, wenn einer von ihnen den anderen irgendwann zuvor angegriffen hat.  
Außerdem wollen wir nicht zwei Hunde derselben Rasse in denselben Zwinger setzen. (Damit wir bei "Der Labrador aus Zwinger 3" eindeutig wissen, welcher Hund gemeint ist.)

## Der Code und die Punkte

### Grundgerüst, Bibliotheken, Sonstiges

 - Verwende die bereitgestellte Datei [`test.c`](test.c) als Grundgerüst.
 - Die Funktion `main` darf überhaupt nicht verändert werden.
 - Wenn du einen Teil der Prüfung nicht löst, dann sollen die Funktions-Stubs zumindest so funktionieren, dass der Code kompiliert und keinen Speicher verliert.
 - Du darfst beliebige zusätzliche Funktionen hinzufügen und jede Funktion der Standard-C-Bibliothek verwenden.
 - Verwende keine Makros und arbeite nur in einer einzigen Datei. (Und lade am Ende auch nur diese Datei auf Moodle hoch.)

Diese Bibliotheken werden benötigt:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
```

Alle Strings (Hundename) sind kürzer als 31 Zeichen, daher kannst du diesen Typ verwenden:

```c
typedef char string[32];
```

Zum Vergleichen von Strings kann die eingebaute Funktion `strcmp` verwendet werden. Manpage dazu:

```
strcmp(3)                   Library Functions Manual                  strcmp(3)

NAME
       strcmp, strncmp - compare two strings

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       int strcmp(const char *s1, const char *s2);
       int strncmp(const char s1[.n], const char s2[.n], size_t n);

DESCRIPTION
       The strcmp() function compares the two strings s1 and s2.  The locale is
       not  taken into account (for a locale-aware comparison, see strcoll(3)).
       The comparison is done using unsigned characters.

       strcmp() returns an integer indicating the result of the comparison,  as
       follows:

       •  0, if the s1 and s2 are equal;

       •  a negative value if s1 is less than s2;

       •  a positive value if s1 is greater than s2.
```

### Dogs und DogList - grundlegende Structs

Verwende folgende Struct zum Speichern der Daten eines Hundes:

```c
typedef struct {
    string name;
    int age;
    string breed;    
} Dog;
```

Entwirf die Struct `DogList` so, dass sie alle Daten aller Hunde enthält, und spätere Funktionen (wie Sortieren) nur eine solche Struct als Argument erhalten.
Schreibe eine Funktion, die allen Heap-Speicher freigibt, und eine Funktion, die die Anzahl der Hunde zurückgibt:

```c
typedef struct {
    // TODO
} DogList;

void free_dog_data(DogList* pdl) {
    // TODO
}

int get_dog_count(DogList dl) { 
    /* TODO */
}
```

Du kannst jede Datenstruktur verwenden. Beachte, dass die Anzahl der Hunde NICHT begrenzt ist.

Erweitere die folgende Funktion so, dass sie die Daten aus [`dog_data.txt`](dog_data.txt) lädt.
Alle Daten aus der Datei wurden bereits in die Buffer-Variablen eingelesen; du musst sie nur zum Füllen einer `DogList` verwenden.


```c
DogList load_dog_data(const char* dogfile) {
    /* Buffer variables for reading */
    int bint1, bint2;
    string bstring1, bstring2;

    DogList dl;
    FILE* f = fopen(dogfile, "r");
    fscanf(f," Number of dogs: %d ", &bint1);
    // TODO
    for (int i=0; i<bint1; ++i) {
        fscanf(f," Name: %s Age: %d Breed: %s ",
            bstring1,
            &bint2,
            bstring2
        );
        // TODO
    }
    fclose(f);
    return dl;
}
```

Erstelle eine einfache Ausgabe der Liste für einfacheres Debugging.

```c
void debug_dog_list(DogList dl){
    // TODO
}
```

Das alles ist **3 Punkte** wert.

### Sortieren nach Alter und anschließend nach Name

Schreibe die oben beschriebene Sortierung (zuerst nach Alter aufsteigend, dann nach Name lexikographisch aufsteigend).

```c
void sort_by_age_then_by_name(DogList dl) {
    // TODO
}
```

Du darfst KEIN Bubble- oder Shaker-Sort verwenden.

Je nach Implementierung gibt es unterschiedlich viele Punkte.

Grundsätzlich:
 - `O(n^2)` Sortierung: **5 Punkte**
 - `O(nlogn)` Sortierung: **9 Punkte**
 - Counting Sort: **11 Punkte**
 - Radix: **+2 Punkte**

Das erlaubt viele Kombinationen:
 - Sortierung nach beiden Feldern gleichzeitig mit:
   - einem `O(n^2)`-Algorithmus: **5 Punkte**
   - einem `O(nlogn)`-Algorithmus: **9 Punkte**
 - Verwendung von Radix Sort für die zwei Felder mit:
   - demselben `O(n^2)`-Algorithmus: **7 Punkte**
   - demselben `O(nlogn)`-Algorithmus: **11 Punkte**
   - zwei verschiedenen `O(n^2)`-Algorithmen: **12 Punkte**
   - einem `O(n^2)`- und einem `O(nlogn)`-Algorithmus: **16 Punkte**
   - zwei verschiedenen `O(nlogn)`-Algorithmen: **20 Punkte**
   - Counting Sort und einem `O(n^2)`-Algorithmus: **18 Punkte**
   - Counting Sort und einem `O(nlogn)`-Algorithmus: **22 Punkte**

Das bedeutet auch, dass du die maximalen 23 Punkte bereits mit den bisherigen Aufgaben erreichen kannst, oder du entscheidest dich hier für eine einfachere Lösung und holst zusätzliche Punkte im zweiten Teil:

### Hunde in Zwinger aufteilen

Ähnlich wie bei `DogList` sollst du die Struct `Conflicts` entwerfen, die Ladefunktion erweitern und eine weitere Funktion schreiben, die Speicher freigibt.  
Diese Struct muss nur speichern, ob zwei Hunde gemeinsam in einen Zwinger dürfen oder nicht; weitere Details über den Grund sind nicht notwendig.

Das ist ebenfalls **3 Punkte** wert.

```c
typedef struct {
    // TODO
} Conflicts;

Conflicts load_conflict_data(DogList dl, const char* logfile) {
    /* Buffer variables for reading */
    string bstring1, bstring2;

    Conflicts c;
    // TODO

    FILE* f = fopen("dog_data.txt", "r");
    while(2==fscanf(f," %*s %s attacked %s ", bstring1, bstring2)) {
        // TODO
    }
    fclose(f);
    return c;
}

void free_conflicts_data(Conflicts* pc) {
    // TODO
}
```

> [!Important]
> Du kannst davon ausgehen, dass sich die bereitgestellte `DogList` später nicht mehr verändert.  
> D. h. die Indizes der Hunde ändern sich nicht (alle Sortierungen passieren davor), du kannst den Graphen also auf Basis der Indizes aufbauen.

Du kannst diese bereitgestellte Funktion verwenden, falls hilfreich (vergiss nur nicht, den Speicher wieder freizugeben):

```c
int* initialize_array(int size, int value) {
    int* array = malloc(size * sizeof(int));
    for (int i=0; i<size; ++i)
        array[i] = value;
    return array;
}
```

Es gibt 3 verschiedene Algorithmen, um Hunde in Zwinger aufzuteilen.  
Du kannst entscheiden, welchen du implementierst – falls überhaupt.  
Alle Funktionen sollen einen Pointer auf ein `int`-Array zurückgeben, das an Index `i` die Nummer des Zwingers enthält, in den der Hund mit Index `i` gesetzt werden soll.

Beispiel:
 - Wenn meine DogList `[Athos, Porthos, Aramis, D'Artagnan]` ist
 - Und eine Funktion `[0,1,1,0]` zurückgibt
 - Bedeutet das, dass Athos und D'Artagnan in Zwinger 0 kommen und Porthos und Aramis in Zwinger 1.

#### Einfache Aufteilung - **8 Punkte**

```c
int* kennels_simple_opennew(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    // TODO
    return kennels;
}
```

Algorithmus:
 - Setze den ersten Hund in Zwinger 0.
 - Für jeden weiteren Hund prüfe, ob er in denselben Zwinger gesetzt werden kann.
   - falls ja, setze ihn dort hinein.
   - falls nein, betrachte den aktuellen Zwinger als abgeschlossen, öffne einen neuen und setze ihn dort hinein.

#### First Fit mit aktueller Reihenfolge - **11 Punkte**

```c
int* kennels_first_fit(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    // TODO
    return kennels;
}
```

Algorithmus:
 - Setze den ersten Hund in Zwinger 0.
 - Für jeden weiteren Hund setze ihn in den Zwinger mit dem kleinsten Index, in dem es keinen Konflikt gibt. (Versuche zuerst Zwinger 0, dann 1, dann 2 usw.)

#### First Fit mit cleverer Reihenfolge - **18 Punkte**

```c
int* kennels_clever_first_fit(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    // TODO
    return kennels;
}
```

Algorithmus:
 - Sortiere die Hunde zuerst mit einer „Selection-Sort-Variante“:
   - Verschiebe den Hund mit den wenigsten Konflikten an die letzte Position.
   - Finde den Hund mit den zweitwenigsten Konflikten und verschiebe ihn an die vorletzte Position. Aber(!) berücksichtige dabei nur Konflikte zwischen Hunden, die noch nicht ausgewählt wurden.
   - Wiederhole das für alle Hunde.
 - Verwende danach First-Fit wie im vorherigen Algorithmus beschrieben.

## Zusammenfassung der möglichen Punkte

Die maximal erreichbare Punktzahl beträgt **66**, was in einem Zeitrahmen von 2 Stunden natürlich unrealistisch ist. Die Punkte werden außerdem bei 23 gedeckelt.
Du kannst die Aufgaben auswählen, die für dich am sichersten/einfachsten sind.

Prüfungsteil | Sortierung nach Alter-Name | Hunde in Zwinger aufteilen |
--- | --- | ---| 
Grundlegende Structs, Funktionen | 3 | 3 |
Hauptaufgabe | 5 bis 22 | 9 + 11 + 18 |

Einige Beispiel-Szenarien:
 - Radix Sort mit Quick Sort für beide Felder + grundlegende Dinge aus dem zweiten Teil, aber keine Zwingeraufteilung: 3+2+9+3 = 17 Punkte.
 - Ein einzelner Merge Sort für den ersten Teil und der einfache Algorithmus für den zweiten: 3+9+3+8 = 23 Punkte.
 - Radix Sort mit Counting und Quick Sort, nichts aus dem zweiten Teil: 3+2+11+9 = 25 -> 23 Punkte.
 - Grundlegende Structs aus dem ersten Teil + einfaches First Fit aus dem zweiten: 3 + 3 + 11 = 17 Punkte.