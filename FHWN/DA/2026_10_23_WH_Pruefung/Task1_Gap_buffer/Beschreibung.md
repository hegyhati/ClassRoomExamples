# Aufgabe 1 – Gap Buffer

## Motivation

Texteditoren (wie der, den du gerade verwendest) müssen den Inhalt der Textdatei irgendwie im Speicher ablegen.
Die naheliegendste erste Idee ist, ein dynamisches Array aus Zeichen für den Inhalt und eine einfache vorzeichenlose Ganzzahl als Indexvariable für die Cursorposition zu verwenden.
Diese Lösung ist jedoch wenig geeignet, wenn wir die typischen Operationen betrachten, die unterstützt werden müssen.

Wir konzentrieren uns auf drei grundlegende Operationen:
 - Cursor nach links/rechts bewegen
 - an der Cursorposition tippen
 - mit der Rücktaste löschen

Bei einer Implementierung mit einem dynamischen Array wäre das Bewegen O(1), da lediglich der Cursorindex erhöht oder verringert wird.
Das Löschen eines Zeichens oder das Einfügen eines neuen Zeichens würde jedoch aufgrund des Verschiebens des Bereichs hinter dem Cursor O(n) Zeit benötigen.

## Gap Buffer

Ein Gap Buffer ist eine einfache Lösung für dieses Problem. Das Speicherlayout besteht weiterhin aus einem dynamisch allozierten Array.
Alles vor dem Cursor befindet sich wie zuvor am Anfang des Arrays.
Der Trick besteht darin, dass sich der Teil der Datei rechts vom Cursor nicht direkt dahinter, sondern am Ende dieses Puffers befindet. Die "freien Bereiche" liegen in der Mitte.

Alle oben genannten Operationen lassen sich nun in O(1) Zeit implementieren:
 - Bewegen nach links/rechts: An den Grenzen des "freien Bereichs" wird jeweils ein Zeichen von links nach rechts beziehungsweise von rechts nach links verschoben/kopiert.
 - Tippen: Die eingegebenen Zeichen werden am linken Ende des "freien Bereichs" eingefügt.
 - Rücktaste: Das Zeichen links vom "freien Bereich" wird diesem hinzugefügt.

Dies wird unten veranschaulicht:

![gb.svg](gb.svg)

Beachte: Wenn der Puffer voll ist, muss er wie ein gewöhnliches dynamisches Array neu alloziert werden.

## Aufgabe

Implementiere die leeren Funktionen in [gap_buffer.c](gap_buffer.c).

`main` darf nicht geändert werden.

Die Funktion `debug` sollte den Zustand des Puffers so ausgeben, dass er sich debuggen lässt, d. h. man sollte den vorderen und hinteren Teil des Puffers sowie die Länge des "freien Bereichs" erkennen können.

Eine mögliche Ausgabe könnte so aussehen:

```
This!_____                                    ===>     This!|
This_____!                                    ===>     This|!
This is a ni_______!                          ===>     This is a ni|!
This is a nice Rap buffer______________!      ===>     This is a nice Rap buffer|!
This is a nice Rap buffe______________r!      ===>     This is a nice Rap buffe|r!
This is a nice Rap buff______________er!      ===>     This is a nice Rap buff|er!
This is a nice Rap buf______________fer!      ===>     This is a nice Rap buf|fer!
This is a nice Rap bu______________ffer!      ===>     This is a nice Rap bu|ffer!
This is a nice Rap b______________uffer!      ===>     This is a nice Rap b|uffer!
This is a nice Rap ______________buffer!      ===>     This is a nice Rap |buffer!
This is a nice Rap______________ buffer!      ===>     This is a nice Rap| buffer!
This is a nice Ra______________p buffer!      ===>     This is a nice Ra|p buffer!
This is a nice R______________ap buffer!      ===>     This is a nice R|ap buffer!
This is a nice Ga______________p buffer!      ===>     This is a nice Ga|p buffer!
This is a nice Gap______________ buffer!      ===>     This is a nice Gap| buffer!
This is a nice Gap ______________buffer!      ===>     This is a nice Gap |buffer!
This is a nice Gap b______________uffer!      ===>     This is a nice Gap b|uffer!
This is a nice Gap bu______________ffer!      ===>     This is a nice Gap bu|ffer!
This is a nice Gap buf______________fer!      ===>     This is a nice Gap buf|fer!
This is a nice Gap buff______________er!      ===>     This is a nice Gap buff|er!
This is a nice Gap buffe______________r!      ===>     This is a nice Gap buffe|r!
This is a nice Gap buffer______________!      ===>     This is a nice Gap buffer|!
This is a nice Gap buffer!______________      ===>     This is a nice Gap buffer!|
This is a nice Gap buffer! ;-) _________      ===>     This is a nice Gap buffer! ;-) |
```

Die linke Seite zeigt das Speicherlayout, die rechte Seite das, was wir im Texteditor sehen würden. `|` kennzeichnet dabei die Cursorposition. Es reicht beispielsweise, nur die linke Seite auszugeben, oder die rechte Seite und zusätzlich die Größe des freien Bereichs anzuzeigen.
