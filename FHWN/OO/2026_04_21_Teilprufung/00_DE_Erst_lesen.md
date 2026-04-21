# Objektorientierte Programmierung – Mechatronik – Programmierprüfung 1


> [!NOTE]
> Da diese Beschreibung Tabellen und Bilder enthält, liest man sie am besten im „Rendered Mode“.
> `ctrl`+`shift`+`v`

## Allgemeine Regeln

 - Zeitlimit: 2,5 Stunden
 - Erlaubte Hilfsmittel:
   - alle handschriftlichen/gedruckten Notizen
   - [Vorlesungsunterlagen](https://github.com/hegyhati/ClassRoomExamples/tree/master/FHWN/OO)
   - jede Python-Datei aus früheren Übungen
   - jede statische Website, insbesondere z. B.:
     - [Offizielle Python-Dokumentation](https://docs.python.org/3/)
     - [W3Schools](https://www.w3schools.com/python/)
     - [GeeksForGeeks](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)
     - [RealPython](https://realpython.com/)
   - [PythonTutor](https://pythontutor.com/visualize.html#)
   - Die einzige erlaubte Suchmaschine ist [DuckDuckGo](https://duckduckgo.com/) – siehe Details unten
   - Grundsätzlich alles, **außer einer anderen Person oder irgendeiner Form von KI**, d. h. kein Coding‑Agent, keine Copilot‑Completion, kein ChatGPT usw.
   - Falls du dennoch Fragen hast, frage jederzeit während der Prüfung.
 - Die Bildschirme werden aufgezeichnet; ein Verstoß gegen die vorherige Regel führt zum sofortigen Nichtbestehen der Lehrveranstaltung.
 - Abgabe:
   - Kein Zippen; lade alle `.py`‑Dateien hoch, an denen du gearbeitet hast, und nur diese.
   - Du darfst zusätzliche `.py`‑Dateien zum Testen oder Ausprobieren erstellen, aber alles muss in den ursprünglich vorgegebenen Dateien abgegeben werden.
   - Eine frühere Abgabe ist erlaubt.
   - Wir können jederzeit während der Prüfung verlangen, einen Snapshot des aktuellen Dateistands hochzuladen.
 - Du darfst die gegebenen Unit‑Tests löschen oder auskommentieren und eigene Tests schreiben; wir betrachten nur die geforderten Funktionen.
 - Die Signaturen der geforderten Funktionen/Methoden dürfen nicht geändert werden, und es darf keine Seiteneffekte (`input` oder `print`) in der abgegebenen Version geben.
 - Es dürfen nur Annahmen getroffen werden, die explizit angegeben sind. Alle anderen Randfälle müssen behandelt werden.

### DuckDuckGo einrichten

Gehe zu [DuckDuckGo](https://duckduckgo.com/) und klicke auf das Hamburger‑Icon (`≡`):

![DDG startpage](resources/duckduckgo/duckduckgo1.png)

Klicke dort auf `Settings` und wähle anschließend `AI Features`:

![DDG settings](resources/duckduckgo/duckduckgo2.png)

Schalte hier `Duck.ai` aus und setze `Search assist` auf `never`.

Danach kannst du DDG zum Suchen verwenden:

![DDG AI](resources/duckduckgo/duckduckgo3.png)


## Die Aufgabe

### Endziel

Ziel dieses Projekts ist es, eine Anwendung zu erstellen, die SVG‑„Kunst“ im Stil von [De Stijl](https://en.wikipedia.org/wiki/De_Stijl) „komprimieren“ kann, indem vollständig überdeckte Rechtecke entfernt werden.

Im Verzeichnis [resources/compression/](resources/compression/) findest du zwei Beispiele zufällig generierter „Kunst“-Grafiken im SVG‑Format.

| Datei | [original.svg](resources/compression/example2/original.svg) | [filtered_by_individual_cover.svg](resources/compression/example2/filtered_by_individual_cover.svg) | [filtered_by_probabilistic_method.svg](resources/compression/example2/filtered_by_probabilistic_method.svg) | 
| --- | --- | --- | --- |
| Bild | ![original.svg](resources/compression/example2/original.svg) | ![filtered_by_individual_cover.svg](resources/compression/example2/filtered_by_individual_cover.svg) | ![filtered_by_probabilistic_method.svg](resources/compression/example2/filtered_by_probabilistic_method.svg) | 
| Beschreibung | Ursprüngliche Eingabedatei mit vielen Quadraten, die nicht sichtbar sind, da sie von anderen Quadraten überdeckt werden | Version, in der jene Quadrate entfernt wurden, die vollständig von einem einzelnen anderen Quadrat überdeckt sind | Version, in der auch jene Quadrate entfernt wurden, die von zwei oder mehr anderen Quadraten überdeckt sind | 
| Anzahl Quadrate | 1000 | 212 | 55 |
| Dateigröße (kB) | 65 | 15 | 4 |

Die drei Bilder sehen gleich aus, haben aber sehr unterschiedliche Größen. Wie die Kompression funktioniert, wird im [letzten Schritt](09_compress_by_cover.py) detailliert beschrieben.

### Schritte

Wie zuvor angekündigt, ist dieses Projekt als eine Reihe kleiner Schritte aufgebaut, die in den `.py`‑Dateien zu finden sind.  
Du wirst niemals mehr Informationen zur Lösung einer Aufgabe benötigen als jene, die in der jeweiligen Datei angegeben sind. (Es ist nicht notwendig, die letzten Schritte zu verstehen, um die ersten Schritte zu lösen.)

Zwischen den Schritten gibt es Abhängigkeiten:

![Dependencies](resources/dependencies.svg)

Durchgezogene Pfeile bedeuten notwendige Abhängigkeiten. Gepunktete Pfeile bedeuten, dass die Tests in 05/06/07 so geschrieben sind, dass sie erwarten, dass die Klasse `Rectangle` im Konstruktor ein Farbargument hat – Details dazu findest du in den jeweiligen Dateien.


![Good Luck!](resources/good_luck.svg)