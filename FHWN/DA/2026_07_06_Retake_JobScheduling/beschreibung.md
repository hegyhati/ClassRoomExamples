# Job Scheduling


## Gesamtziel

Die Aufgabe ist es, alle Jobs aus einer Datei **auf einer einzelnen Maschine** zu planen.

Jeder Job hat:
 - eine Bearbeitungszeit: die Zeit, die auf der Maschine benötigt wird
 - eine Deadline: der Zeitpunkt, bis zu dem der Job abgeschlossen sein soll
 - Abhängigkeiten: andere Jobs, die vor diesem Job abgeschlossen sein müssen.

Das Ziel ist, die **gesamte Verspätung (total tardiness)** zu minimieren.
Die Verspätung ist 0, wenn ein Job vor seiner Deadline fertig wird, sonst `completion_time - deadline`.

## Eingabedateien

Es gibt 3 Eingabedateien zum Testen, die folgendes Format haben:

```
JOBS <count>
<id> <processing_time> <deadline> | <dep_id> <dep_id> ... |
<id> <processing_time> <deadline> | <dep_id> <dep_id> ... |
<id> <processing_time> <deadline> | <dep_id> <dep_id> ... |
```

Du kannst annehmen, dass die IDs Ganzzahlen in aufsteigender Reihenfolge sind, beginnend bei 0.

## Allgemein

 - Code, der nicht kompiliert oder einen Segmentation Fault verursacht, ergibt 0 Punkte.
 - Code mit Memory Leaks ergibt 50% der Punkte.
 - `main` darf nicht verändert werden, ausser beim Namen der Testdatei.
 - Du darfst alle anderen Funktionen ändern, Hilfsfunktionen hinzufügen usw.
 - `debug(...)` verhält sich wie `printf`, kann aber mit einer einzigen Makro-änderung deaktiviert werden.
 - Fehlerbehandlung ist nicht nötig (Datei fehlt, Dateiformat falsch usw.).

## Aufgaben

### Grundlegende Structs & Funktionen - 3 Punkte


```C
typedef struct {
    // TODO
} Jobs;

Jobs* read_jobs(const char *filename)
{
    FILE *f = fopen(filename, "r");
    int jobcount, jobid, proctime, deadline, dependency; // buffer variables
    Jobs* jobs = NULL;

    fscanf(f, "JOBS %d", &jobcount);
    debug(" | %3d jobs found in file %s\n",jobcount, filename);
    // TODO

    for (int i = 0; i < jobcount; ++i) {
        fscanf(f, " %d %d %d | ", &jobid, &proctime, &deadline);
        debug(" | Job %3d has processing time of %2d and deadline of %3d, its dependencies are: ", jobid, proctime, deadline);
        //TODO 

        while (fscanf(f, " %d", &dependency) == 1) {
            debug(" Job %3d,", dependency);
            // TODO
        }
        fscanf(f, " |");
        debug("\n");
    }
    fclose(f);
    return jobs;
}

void deallocate_jobs(Jobs** pjobs) {
    // TODO
}
```

Entwerfe die Struct so, dass sie alle oben beschriebenen Informationen enthält. Erweitere danach die Parsing-Funktion und schreibe eine Funktion, die den allokierten Speicher wieder freigibt.

**Achte besonders** auf Zeiger.
In `main` sollen nur Zeiger auf Structs gespeichert / an Funktionen übergeben / usw. werden.

Minus 1 Punkt, wenn die Abhängigkeitslogik nicht gespeichert wird.

### `JobOrder` Struct & Freigabefunktion

Das ist nur ein einfaches Integer-Array, das die IDs der Jobs in der Reihenfolge speichern kann, in der die Maschine sie ausführt.

```c
typedef struct {
    int jobcount;
    int* jobids; 
} JobOrder;

void deallocate_joborder(JobOrder** porder) {
    if (*porder) {
        free((*porder)->jobids);
        free(*porder);
        *porder = NULL;
    }
}
```
### Berechnung der Verspätung - 3 Punkte

Diese Funktion bekommt sowohl die Jobdaten als auch eine Reihenfolge (beides als Zeiger!) und berechnet Start- / Endzeit jedes Jobs, danach die gesamte Verspätung. Die Maschine startet bei Zeit 0.

```c
int total_tardiness(const Jobs* const jobs, const JobOrder* const order) {
    // TODO
    return -1;
}
```

Diese Funktion muss nicht prüfen, ob Abhängigkeiten eingehalten sind.

Beispiel:

| Job | proctime | deadline |
| --- | --- | --- |
| 0 | 3 |  5 |
| 1 | 6 | 9 |
| 2 | 4 | 6 |


Wenn die Job-Reihenfolge `0,2,1` ist, dann:

| Job | start | proctime | end | deadline | tardiness |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 3 | 0+3 = 3 | 5 | 0 |
| 2 | 3 | 4 | 3+4 = 7 | 6 | 7-6 = 1 |
| 1 | 7 | 6 | 7+6 = 13 | 9 | 13-9 = 4 |


Die gesamte Verspätung ist 0+1+4 = 5.


### EDD-Jobreihenfolge OHNE Abhängigkeiten - 4 Punkte

EDD (Earliest Due Date) ist eine einfache Strategie, die Jobs in aufsteigender Reihenfolge ihrer Deadline sortiert. Für das obige Beispiel wäre die EDD-Reihenfolge `0,2,1`.

Implementiere diese Logik in der folgenden Funktion.
Wenn zwei Jobs die gleiche Deadline haben, darfst du die Reihenfolge beliebig wählen.

In diesem Teil musst du Abhängigkeiten **NICHT** berücksichtigen, aber die Funktion soll in höchstens `O(jobcount * log(jobcount))` Zeit laufen (im Durchschnitt).

```c
JobOrder* EDD(const Jobs * const jobs ) {
    JobOrder* order = NULL;
    // TODO 
    return order;
}
```

### SPT-Jobreihenfolge MIT Abhängigkeiten - 5 Punkte

SPT (Shortest Processing Time) ist eine weitere einfache Strategie, die in jedem Schritt den verfügbaren Job mit der kürzesten Bearbeitungszeit wählt.
Die SPT-Reihenfolge für das obige Beispiel wäre `0,2,1`; diese wurde auch als Beispiel für die Verspätungsberechnung verwendet.

Für diese Reihenfolge **müssen die Abhängigkeiten berücksichtigt werden**.
Wenn im obigen Beispiel Job 2 von Job 1 abhängt, dann gilt:
 - Anfangs können nur Job 0 und Job 1 gestartet werden, da sie keine Abhängigkeiten haben.
 - Job 0 hat die kleinere Bearbeitungszeit, also wird er zürst ausgeführt.
 - Danach kann Job 2 noch nicht gewählt werden, weil er von Job 1 abhängt; damit ist Job 1 jetzt der Job mit minimaler Bearbeitungszeit.
 - Danach kann schliesslich Job 2 ausgeführt werden.


```c
JobOrder* SPT(const Jobs * const jobs ) {
    JobOrder* order = NULL;
    // TODO 
    return order;
}
```

Für diese Strategie gibt es keine Laufzeitbeschränkung.
