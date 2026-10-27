""" EN 

Write a `Turtle` class, that simulates a turtle / Logo drawing on a coordinate system:
 - The turtle is initially at (x=0, y=0), and looks  "north" (alpha = 90 degrees or pi/3 rad), and pen is always down, i.e., every movement of the turtle leaves a trace.
 - The turtle has the following commands for movement/drawing:
   - `.fd(distance)`: the turtle moves forward in a straight line the given distance, and leaves mark.
   - `.rt(degree)` / `.lt(degree)`: the turtle turns with `degree` degrees to right/left.
 - The turtle object should also provide the method:
   - `save_to_svg(filename)` saves the drawing made by the turtle in an SVG file with the given name.

The template for the SVG file:

```
<svg width="(maxx - minx)" height="(maxy - miny)" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(-minx, maxy) scale(1,-1)">
    <line x1="start_x" y1="start_y" x2="end_x" y2="end_y" style="stroke:black;stroke-width:2" />
  </g>
</svg>
```

Where minx, maxx, etc. are the minimal/maximal x/y coordinates where the turtle has been, and a <line> represents a single movement. 

The output of the examples are in the provided SVG files.

Tips: 
 - Besides maintaining the turtles position and direction, it is a good idea to also keep track of the bounds (minx, etc.). 
 - To be able to generate the SVG file, the turtle has to remember all the lines drawn (all the movements).
 - The math module provides useful trigonametric functions (pay attention to rad-degree conversion):
    `math.cos(r)`     Return the cosine of r radians.
    `math.sin(r)`     Return the sine of r radians.
    `math.radians(d)` Convert angle d from degrees to radians.

"""


""" DE

Schreibe eine `Turtle`-Klasse, die eine Turtle- / Logo-Zeichnung auf einem Koordinatensystem simuliert:
 - Die Turtle befindet sich anfangs bei (x=0, y=0), blickt nach "north" (alpha = 90 Grad oder pi/3 rad), und der Stift ist immer unten, d. h. jede Bewegung der Turtle hinterlässt eine Spur.
 - Das Turtle-Objekt hat die folgenden Befehle für Bewegung/Zeichnen:
   - `.fd(distance)`: die Turtle bewegt sich die angegebene Strecke geradeaus und hinterlässt eine Spur.
   - `.rt(degree)` / `.lt(degree)`: die Turtle dreht sich um `degree` Grad nach rechts/links.
 - Das Turtle-Objekt soll außerdem die folgende Methode bereitstellen:
   - `save_to_svg(filename)` speichert die von der Turtle erzeugte Zeichnung in einer SVG-Datei mit dem angegebenen Namen.

Die Vorlage für die SVG-Datei:

```
<svg width="(maxx - minx)" height="(maxy - miny)" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(-minx, maxy) scale(1,-1)">
    <line x1="start_x" y1="start_y" x2="end_x" y2="end_y" style="stroke:black;stroke-width:2" />
  </g>
</svg>
```

Dabei sind minx, maxx usw. die minimalen/maximalen x-/y-Koordinaten, an denen die Turtle gewesen ist, und ein `<line>` repräsentiert eine einzelne Bewegung.

Die Ausgaben der Beispiele befinden sich in den bereitgestellten SVG-Dateien.

Tipps:
 - Zusätzlich zum Verwalten der Position und Richtung der Turtle ist es sinnvoll, auch die Grenzen (minx usw.) zu speichern.
 - Um die SVG-Datei erzeugen zu können, muss die Turtle sich alle gezeichneten Linien merken (alle Bewegungen).
 - Das Modul math stellt nützliche trigonometrische Funktionen bereit (achte auf die Umrechnung zwischen Bogenmaß und Grad):
    `math.cos(r)`     Return the cosine of r radians.
    `math.sin(r)`     Return the sine of r radians.
    `math.radians(d)` Convert angle d from degrees to radians.

"""
import math

class Turtle:
  def __init__(self):
    pass

  def fd(self, distance):
    pass

  def rt(self, degree): 
    pass

  def lt(self, degree): 
    pass

  def save_to_svg(self, filename):
    pass


def test_square(): 
  t = Turtle() 
  for _ in range(4):          # 4 times the turtle
    t.fd(100)                 #   - moves 100 forward then
    t.rt(90)                  #   - turns 90 degrees right
  t.save_to_svg("square.svg") # should be a 100x100 picture with a square

def test_triangle(): 
  t = Turtle() 
  t.rt(30)                    # Turtle turns 30 degrees right
  for _ in range(3):          # 3 times the turtle
    t.fd(100)                 #   - moves 100 forward then
    t.rt(120)                 #   - turns 120 degrees right
  t.save_to_svg("triangle.svg") # should be a 100x96 picture with a triangle

def test_sierpinsky():
  def sierpinski(t, side, depth):
    if depth == 0:
      for _ in range(3):
        t.fd(side)
        t.rt(120)
      return

    sierpinski(t, side / 2, depth - 1)
    t.fd(side / 2)
    sierpinski(t, side / 2, depth - 1)
    t.rt(120)
    t.fd(side / 2)
    t.lt(120)
    sierpinski(t, side / 2, depth - 1)
    t.lt(120)
    t.fd(side/2)
    t.rt(120)

  t = Turtle()
  t.rt(30)
  sierpinski(t, 1024, 8)
  t.save_to_svg("sierpinsky.svg")

if __name__ == "__main__":
    test_square()
    test_triangle()
    test_sierpinsky()