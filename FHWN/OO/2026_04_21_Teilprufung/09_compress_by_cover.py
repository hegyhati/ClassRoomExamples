""" EN

DEPENDS on everything (05,06,07,08)

Copy-paste all of your previous code, only start working on this if all of the previous tasks are finished.

Implement the teo functions below.

Both of them should:
 1. open the file provided in the first argument
 2. filter our covered (non visible) rectangles
 3. save the remaining rectangles in a file, whose name should have the provided suffix (e.g.: original.svg -> original_fbdic.svg) 

The filtering method for each function:

`filter_by_individual_cover` checks whether a rectangle is completely covered by another (later) rectangle by itself. If yes, this rectangle can be removed.

`probabilistic_filter` generates TRIES = 10000 random inside points of a rectangle. If ALL of them are contained by ANY of the later rectangles, the rectangle can be removed.

Test the functions manually on any of the provided SVG files.

"""

"""
ABHÄNGIG VON ALLEM (05, 06, 07, 08)

Kopiere deinen gesamten bisherigen Code hier hinein und beginne erst mit dieser Aufgabe,
wenn alle vorherigen Aufgaben abgeschlossen sind.

Implementiere die zwei untenstehenden Funktionen.

Beide Funktionen sollen:
 1. die im ersten Argument angegebene Datei öffnen
 2. überdeckte (nicht sichtbare) Rechtecke herausfiltern
 3. die verbleibenden Rechtecke in einer Datei speichern, deren Name das angegebene
    Suffix enthält (z.B.: original.svg -> original_fbdic.svg)

Die jeweilige Filtermethode:

`filter_by_individual_cover`  
prüft, ob ein Rechteck vollständig von einem anderen (späteren) einzelnen Rechteck
überdeckt wird. Ist das der Fall, kann dieses Rechteck entfernt werden.

`probabilistic_filter`  
erzeugt `TRIES = 10000` zufällige Punkte innerhalb eines Rechtecks.
Wenn ALLE diese Punkte von IRGENDEINEM der späteren Rechtecke enthalten sind,
kann das Rechteck entfernt werden.

Teste die Funktionen manuell mit einer der bereitgestellten SVG-Dateien.

"""

def filter_by_individual_cover(filename:str, suffix:str="_fbic") -> None:
    pass

TRIES = 10000
def probabilistic_filter(filename:str, suffix:str="_pf") -> None:
    pass




    