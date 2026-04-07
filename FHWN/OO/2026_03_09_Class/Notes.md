# Notes

`dict`s sind nützlich, um Daten zu gruppieren, die zusammengehören. 
Dann kann man all diese Daten einfach auf einmal an eine Funktion übergeben.

Es passiert oft, dass mehrere Dictionaries mit denselben Schlüsseln und derselben Struktur verwendet werden sollen.
Dann wäre es nützlich, diese Struktur zu definieren und durchzusetzen.

Benutzerdefinierte Typen, also Klassen, sind eine Antwort auf diese Anforderung.
In C haben wir dafür `struct` verwendet. 
Klassen ermöglichen viel mehr, und wir werden einige davon gleich auch diskutieren.

> [!Note]
> [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple) und [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict) in Python können etwas Ähnliches schaffen. 


<table><tr><th style="width: 33%;">C - <code>struct</code></th><th style="width: 33%;">Python - <code>dict</code></th><th style="width: 33%;">Python - <code>class</code></th></tr><tr><td style="vertical-align: top;">

```c
struct Warrior {
    char[16] name;
    int health;
    int damage;
};
```

</td><td style="vertical-align: top;">

```python
# No type definition
```

</td><td style="vertical-align: top;">

```python
class Warrior:
    name: str
    health: int
    damage: int
```

</td></tr><tr><td style="vertical-align: top;">

```c
struct Warrior friend;
struct Warrior foe;
```

</td><td style="vertical-align: top;">

```python
friend = {}
foe = {}
```

</td><td style="vertical-align: top;">

```python
friend = Warrior()
foe = Warrior()
```

</td></tr><tr><td style="vertical-align: top;">

```c
strcpy(friend.name, "Lan Mandragoran");
friend.health = 50;
friend.damage = 10;

strcpy(foe.name, "Demandred");
foe.health = 80;
foe.damage = 7;
```

</td><td style="vertical-align: top;">

```python
friend["name"] = "Lan Mandragoran"
friend["health"] = 50
friend["damage"] = 10

foe["name"] = "Demandred"
foe["health"] = 80
foe["damage"] = 7
```

</td><td style="vertical-align: top;">

```python
friend.name = "Lan Mandragoran"
friend.health = 50
friend.damage = 10

foe.name = "Demandred"
foe.health = 80
foe.damage = 7
```

</td></tr><tr><td style="vertical-align: top;">

```c
foe.health = -= friend.damage;
```

</td><td style="vertical-align: top;">

```python
foe["health"] -= friend["damage"]
```

</td><td style="vertical-align: top;">

```python
foe.health -= friend.damage
```

</td></tr></table>


Einige wichtige Begriffe:
- Eine **Klasse** (`Warrior`) ist ein neuer Typ, den wir definieren.
- **Instanzen** (`friend` und `foe`) dieser Klasse sind die Variablen, die wir erstellen und die diesen Typ haben.
- Die Instanzen aller Klassen werden Objekte genannt.
- `name`, `health`, `damage`, also die Daten einer Instanz, haben mehrere Bezeichnungen: Feld (field), Member, Instanzvariable oder **Attribut**.

Es gibt einige wesentliche Unterschiede zwischen dem Dict‑ und dem Klassen‑Ansatz. 
Aber bevor das:

> [!IMPORTANT]
> Wie wir sehen werden, unterstützt Python eine „lose“ objektorientierte Programmierung.
> Einige Prinzipien, die von anderen (strengeren) Sprachen durchgesetzt werden, sind es in Python nicht.
> Oft ist es jedoch gute Praxis, ihnen trotzdem zu folgen.
> Wir werden versuchen, dies jedes Mal durch "kann nicht" und "sollte nicht" zu betonen.

**Struktur**

Die Struktur eines `dict`s ist nicht fest.
Unter der Struktur verstehen wir hier die Schlüssel, die eine Variable hat, die Typen der Werte, usw.
Man kann (vorerst) Klassen so verstehen wie dicts, bei denen die Schlüssel (Attributen) bei der Definition festgelegt sind und später nicht mehr geändert werden können.

> [!Caution]
> Python unterstützt keine strikt erzwungene Klassen‑OO, sondern eine sehr dynamische, klassenbasierte objektorientierte Programmierung.
> Deshalb kann man Attribute von Instanzen zur Laufzeit ändern oder hinzufügen:
>
> ```python
> foe.superpower = "True power"
> del friend.name
> ```
>
> Aber das **sollte** man meistens **NICHT** machen.

**Typsicherheit**

Typ‑Annotationen können nur zeigen, dass zum Beispiel ein Funktionsparameter ein `dict` sein soll.
Man kann aber nicht annotieren, ob es sich um ein Warrior‑`dict` oder ein Potion‑`dict` handeln soll.
Dadurch kann leicht ein Fehler entstehen, wenn man ein `dict` mit einer anderen Struktur an eine Funktion übergibt.
`mypy` kann solche Fehler nicht melden, da beide Parameter vom Typ dict sind – nur Schlüssel und Werte unterscheiden sich.
Bei Klassen passiert das nicht: `mypy` kann diese Fehler einfach melden:

```py
# warrior.py

def drink_potion(warrior:dict, potion:dict) -> None:
    warrior["health"] += potion["effect"]

friend = {
    "name" : "Lan Mandragoran",
    "health" : 50,
    "damage" : 10
}

roots = {
    "name" : "Crimsonthorn root from Nynaeve al'Meara",
    "effect" : 10
}

drink_potion(roots,friend)

```

Die Parameter werden verwechselt, `mypy` meldet nichts, und dann stürzt das Programm ab:


```
$ python3 -m mypy warrior.py
Success: no issues found in 1 source file
$ python3 warrior.py 
Traceback (most recent call last):
  File "/home/hegyhati/git/ClassRoomExamples/FHWN/OO/2026_03_09_Class/warrior.py", line 15, in <module>
    drink_potion(roots,friend)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "/home/hegyhati/git/ClassRoomExamples/FHWN/OO/2026_03_09_Class/warrior.py", line 2, in drink_potion
    warrior["health"] += potion["effect"]
    ~~~~~~~^^^^^^^^^^
KeyError: 'health'
$ 
```

Bei Klassen werden solche Fehler von `mypy` gemeldet:

```py
def drink_potion(warrior:Warrior, potion:Potion) -> None:
    warrior.health += potion.effect

class Warrior:
    name : str
    health : int
    damage : int

class Potion:
    name : str
    effect : int


friend = Warrior()
friend.name = "Lan Mandragoran"
friend.health = 50
friend.damage = 10


roots = Potion()
roots.name = "Crimsonthorn root from Nynaeve al'Meara"
roots.effect = 10

drink_potion(roots,friend)
```

Dann `mypy` meldet die Fehler:
```
$ python3 -m mypy warrior.py
warrior.py:24: error: Argument 1 to "drink_potion" has incompatible type "Potion"; expected "Warrior"  [arg-type]
warrior.py:24: error: Argument 2 to "drink_potion" has incompatible type "Warrior"; expected "Potion"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
$
```

Typsicherheit ist da für Attributen auch. 
`friend.health = "50"` wurde auch gemeldet werden:
```
foo.py:16: error: Incompatible types in assignment (expression has type "float", variable has type "int")  [assignment]
```

## Konmstruktor

Es gibt zwei Probleme mit den folgenden Zeilen:

```py
friend = Warrior()
friend.name = "Lan Mandragoran"
friend.health = 50
friend.damage = 10
```

Erstens ist es mühsam, das zu tippen, und zweitens:


```py
friend = Warrior()
# Hat friend ein "health" oder "damage"? Falls ja, was ist das Wert?
friend.name = "Lan Mandragoran"
friend.health = 50
friend.damage = 10
```

In der zweiten Zeile befindet sich das Objekt `friend` in einem inkonsistenten Zustand.

> [!Important]
> Beim Zustand (state) eines Objekts nennen wir die Werte seiner Attribute.

Der Konstruktor löst beide dieser Probleme: 

```py
class Warrior:
    name : str
    health : int
    damage : int

    def __init__(self, name:str, initial_health:int, damage:int):
        self.name = name
        self.health = initial_health
        self.damage = damage

friend = Warrior("Lan Mandragoran", 50, 10)
# Oder bei Namen:
foe = Warrior(
    initial_health = 80,
    damage = 7,
    name = "Demandred"
)
```

`__init__` ist eine Funktion, die einmal eingedrückt ist, so sie gehört zur `Warrior`‑Klasse.
Funktionen, die zu einer Klasse gehören, werden **Methoden** genannt.
`__init__` ist eine spezielle Methode, da sie immer (einmal) ausgeführt wird, wenn eine neue Instanz erstellt wird.

> [!TIP]
> Wir haben bereits über Methoden gelernt: die Methoden von `list`, `dict` und `str`.
> Eigentlich sind diese drei auch nicht speziell, sondern einfach Klassen und haben Funktionen/ Methoden wie `append`, `sort`, `upper`, `split` usw.

In jeder Methode ist das erste Argument die Instanz selbst, die beim Aufruf nicht übergeben werden muss.
Konventionell nennen wir dieses Argument immer `self`.
(Man darf einen anderen Namen benutzen, sollte es aber nicht tun.)

## Methode

Man kann weitere Methoden definieren und aufrufen, die auf den Attributen einer Instanz arbeiten:

```py
class Warrior:
    name : str
    health : int
    damage : int

    def __init__(self, name:str, initial_health:int, damage:int):
        self.name = name
        self.health = initial_health
        self.damage = damage

    def is_alive(self) -> bool:
        return self.health > 0
    
    def drink_potion(self, potion:Potion) -> None:
        if self.is_alive():
            self.health += potion.effect

    def attack(self, other:"Warrior") -> None:
        if self.is_alive() and other.is_alive():
            other.health -= self.damage


friend = Warrior("Lan Mandragoran", 50, 10)
foe = Warrior("Demandred", 80, 7)

while (friend.is_alive() and foe.is_alive()):
    friend.attack(foe)
    foe.attack(friend)

if friend.is_alive():
    winner = friend
    loser = foe
else:
    # einfacher
    winner,loser = foe, friend

print(f"{winner.name} hat {loser.name} besiegt.)")
```

## Abstraktion und Kapselung

Beachte, dass diese Zeilen nicht wissen, wie ein Warrior einen anderen angreift oder wie entschieden wird, ob ein Warrior noch lebt:

```py
while (friend.is_alive() and foe.is_alive()):
    friend.attack(foe)
    foe.attack(friend)
```

Man kann die Logik für Angriffe z. B. so verändern, dass es eine Trefferchance von 30% gibt:

```py
import random

class Warrior:
    ...
    def attack(self, other:"Warrior") -> None:
        if self.is_alive() and other.is_alive():
            if random.uniform(0,100) < 30: 
                other.health -= self.damage
```

Dann arbeiten diese Zeilen weiter, und die Logik bleibt korrekt:

```py
while (friend.is_alive() and foe.is_alive()):
    friend.attack(foe)
    foe.attack(friend)
```

> [!important]
> Das ist das **Abstraktionsprinzip**: Der Aufrufer muss nicht wissen, wie ein Objekt intern gespeichert ist oder wie eine Methode arbeitet.
> Der Aufrufer kann der Methode vertrauen, dass sie tut, was sie tun muss, und sich einfach darauf verlassen.


Schauen wir uns nun diese Zeilen an:

```py
print(f"{winner.name} hat {loser.name} besiegt.)")
```

Hier greifen wir direkt auf das Attribut name dieser Objekte zu.
Das ist nicht schön, und man sollte das wirklich nicht machen, außer wenn es absolut notwendig ist.

> [!Important]
> Das nächste OO‑Prinzip, die Kapselung:
> Nicht nur muss der Aufrufer nicht wissen, was sich im Inneren befindet, sondern er darf darauf auch keinen Zugriff haben.

Für dieses Ziel können wir Folgendes tun:

```py
class Warrior:
    ...
    def get_name(self) -> str:
        return self.name

...
print(f"{winner.get_name()} hat {loser.get_name()} besiegt.)")
```

Der Vorteil davon ist, dass wir den Namen des Attributs intern frei ändern oder das Verhalten der `get_name`‑Methode anpassen können, ohne den Code zu zerstören, der unsere Klasse verwendet.

Jetzt befolgen wir dieses Prinzip bewusst, und es wird uns (noch) nicht von der Sprache aufgezwungen.

Andere Sprachen haben oft ein `private`‑Keyword dafür. 
Leider können wir das in Python nicht direkt verwenden.
Python bietet jedoch etwas Ähnliches, nämlich Unterstriche am Anfang eines Attributnamens:

```py
class Foo:
    public_attribute : int
    _not_so_public_attribute : int
    __almost_private_attribute : int

    def some_method(self):
        self.public_attribute = 1 # OK
        self._not_so_public_attribute = 1 # OK
        self.__almost_private_attribute = 1 # OK
        

foo = Foo()
foo.public_attribute = 1 # OKish - aber immer noch verletzt die Kapselung
foo._not_so_public_attribute = 1 # Kein Fehler, aber sollte man das WIRKLICH NICHT tun
foo.__almost_private_attribute = 1 # Gibt ein Fehler bei Ausführung
```  

> [!TIP]
> Eine gute Faustregel: Verwende immer doppelte Unterstriche für Attribute, außer du hast einen wirklich, wirklich guten Grund, es nicht zu tun.

Methoden können ähnlicherweise mit `_` oder `__` anfangen.

> [!important]
> Die Methoden, die kein `_` haben, werden oft öffentliche (public) Methoden genannt und bilden zusammen häufig das Interface der Klasse.
> Dieses kann als eine Art Vertrag zwischen den zwei Entwicklern betrachtet werden, die die Klasse erstellen und verwenden.

## `__str__`

TODO





