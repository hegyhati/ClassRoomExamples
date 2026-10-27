""" EN 
Write a `Turtle` class, that simulates a turtle drawing on a coordinate system. 

The provided main function should work without any change, and save the drawing in SVG format.

The "commands" for the Turtle are the same as usual for the Logo programming language:
 - fd: move forward
 - lt/rt: left/right turn
 - pen up/down: after pen-up, the turtle movement does not leave a mark until pen-down.

SVG template:

<svg height="200" width="300" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="0" x2="300" y2="200" style="stroke:red;stroke-width:2" />
</svg> 


"""

""" DE
Schreibe eine Klasse `Turtle`, die eine zeichnende Schildkröte auf einem Koordinatensystem simuliert.

Die bereitgestellte main-Funktion soll ohne Änderungen funktionieren und die Zeichnung im SVG-Format speichern.

Die Befehle für die Turtle sind wie in der Programmiersprache Logo üblich:
 - fd: vorwärts bewegen
 - lt/rt: links-/rechtsdrehung
 - pen up/down: nach pen-up hinterlässt die Turtle bei Bewegungen keine Spur, bis pen-down aufgerufen wird.

SVG-Vorlage:

<svg height="200" width="300" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="0" x2="300" y2="200" style="stroke:red;stroke-width:2" />
</svg>
"""


t = Turtle()

t.pen_down()
t.fd(40)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(50)
t.lt(180)
t.fd(10)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(30)
t.lt(90)
t.pen_up()
t.fd(10)
t.lt(90)
t.fd(20)
t.pen_down()
t.fd(10)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(10)

t.save("house.svg")