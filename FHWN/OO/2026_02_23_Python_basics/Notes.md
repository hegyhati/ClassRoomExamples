# Python Grundlagen

## Prolog 
(Nicht [dieser Prolog](https://de.wikipedia.org/wiki/Prolog_(Programmiersprache)))

### Was ist Python?

Eine andere Programmiersprache. 

### Warum lernen wir Python?

Weil C nicht sehr geeignet für objektorientierte Programmierung ist. 

### Was ist objektorientierte Programmierung?

Wir werden alle Klassen in diesem Semester brauchen, um diese Frage (teilweise) beantworten zu können. 
Aber kurzgesagt🐦: ein Stil, wie man den Code schreiben und strukturieren kann. 

### Und ist dieser Stil in C nicht möglich?

Es ist (z.B. [GTK](https://www.gtk.org/)), aber die Sprache unterstützt diesen Stil nicht (sehr).
Man kann mit einem Motorsäge Brot schneiden, aber... 

### Ist dieser Stil wichtig? 

Ja, der objektorientierte Stil ist sehr wichtig. 
Aber der richtige Begriff ist nicht *Stil*, sondern *Paradigma*. 
Wir werden von nun das verwenden, und die Abkürzung OO für Objektorientierte [Paradigma]. 

### Warum ist das objektorientierte Paradigma wichtig?

Dieses Paradigma ist (stand heute) dasjenige, das zuverlässig für große, komplexe Systeme verwendet werden kann. 

### Ich habe es gelesen, dass "OO is dead" und dass man heute das funktionale Paradigma lernen sollte.

Du wirst sehen, dass es in diesem Bereich viele heiße Debatten gibt, wie zum Beispiel OO gegen FP. 
Funktionale Programmierung und ihre Ideen sind heutzutage sehr populär und genutzt, aber fast alle großen Softwares sind tatsächlich in OO geschrieben. 

Allerdings sind Paradigmen nicht exklusiv.
Eine Programmiersprache kann sozusagen eine Multi-Paradigma-Sprache sein.

### So wie Python?

Genau, Python unterstützt objektorientierte, funktional und prozedural. 

### Prozedural?

Was du schon mit C gelernt hast. 

### Und sind diese drei alle Paradigmen, die es gibt? 

Nein, gibt es andere, z. B. [dieser Prolog](https://de.wikipedia.org/wiki/Prolog_(Programmiersprache)) unterstützt logische Programmierung. 

Aber das ist nicht wirklich wichtig für uns jetzt, was wichtiger ist:

## Python ist eine interpretierte Sprache

### Interpretierte Sprache?

Als wir in der Klasse "Grundlage der Informatik" [gelernt haben](../../Misc/2025_11_05_GDI_Flipflops_CPU/notes.md) gelernt haben, dass der Computer Machinencode benötigt, um ausgeführt werden zu können. 
Wir haben gesehen, wie ein C-code in Machinencode umgewandelt wird.
Dieser Prozess heißt Kompilierung, und das Program, das dies macht, nennt man Compiler.

![Compilation process](pics/compilation.jpg)
(Kannst du den versteckten Witz finden?)

Was bei C passiert ist, dass der gesammte Code zuerst umgewandelt wird, und dann kann die Binärdatei selbst ausgeführt werden.
Bei interpretierten Sprachen ist der Process anders: ein anderes Programm, der sogenannte Interpreter, liest den (z.B. Python) Code Zeile für Zeile, und gibt dem Computer dieselben Anweisungen in Machinencode.

TODO: ![Interpretation process](pics/interpretation.jpg)

> [!NOTE]
> Eine Sprache selbst ist nicht wirklich kompiliert oder interpretiert. 
> Zum Beispiel, man könnte auch ein Programm schreiben, das C-Code interpretieren kann. 
> Aber diese Bezeichnungen werden oft verwendet, weil eine Sprache meistens nur auf eine Weise genutzt wird.


TODO: C in Cpython, a picture showing cpython.c --gcc--> cpython. 

Es gibt viele allgemeine Unterschiede zwischen kompilierten und interpretierten Sprachen.
In dieser Tabelle gibt es einige, die meistens zutreffen:

TODO: difference in tablesm then about REPL, and when to use it. 

## Python erste Schritte

Es wäre unorthodox, nicht mit "Hello World" zu beginnen:

<table><tr><th>C</th><th>Python</th></tr><tr><td>

```c
#include <stdio.h>

int main() {
    printf("Hello World!");
    return 0;
}
```

</td><td>

```python
print("Hello World!")
```

</td></tr></table>

Einige Notizen:

 - Keine Semikolon.
 - `print('Hello World!')` passt auch. In Python können sowohl `'` als auch `"` verwendet werden, um ein Stringliteral zu erstellen. Aber sei einfach konsequent. `"` und `'` willkürlich gemischt im selben Code zu verwenden, ist ein absolutes No-Go.

> [!Important] 
> `'a'` ist dasselbe wie `"a"`, also kein einzelnes Zeichen sondern ein String. Python hat keinen Zeichentyp nur Strings.

 - `print` in Python fügt automatisch einen Zeilenumbruch hinzu. Falls man das nicht möchte, sollte man `print("Hello World!", end="")` verwenden.
