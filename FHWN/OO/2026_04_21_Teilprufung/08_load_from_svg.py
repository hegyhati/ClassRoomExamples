"""

DEPENDS on 04 and 01

Copy-paste your code from 04/05/06/07 and 01, and implement the `load_from_svg(filename:str) -> list[Rectangle]` function, that opens up the provided file, and looks for lines that represent a rectangle:

<rect x="..." y="..." width="..." height="..." fill="..." />

where x and y are the coordinates of the TOPLEFT corner, fill is the color of the rectangle, width/height are the dimensions along the x/y axis.

For each such line, it creates a new Rectangle object, and returns all of them in a list.

You can assume, that 
 - the file exists, 
 - it is readable, 
 - it is a proper SVG, and
 - has only one xml tag per line.

"""

""" DE

ABHÄNGIG VON 04 und 01

Kopiere deinen Code aus 04/05/06/07 sowie aus 01 hier hinein und implementiere die Funktion  
`load_from_svg(filename: str) -> list[Rectangle]`.

Diese Funktion soll die angegebene Datei öffnen und nach Zeilen suchen, die ein Rechteck beschreiben:

<rect x="..." y="..." width="..." height="..." fill="..." />

Dabei sind `x` und `y` die Koordinaten der **linken oberen Ecke**, `fill` ist die Farbe des Rechtecks und `width`/`height` sind die Abmessungen entlang der x- bzw. y-Achse.

Für jede solche Zeile soll ein neues `Rectangle`-Objekt erzeugt werden.  
Die Funktion gibt schließlich alle erzeugten Rechtecke in einer Liste zurück.

Du kannst davon ausgehen, dass:
- die Datei existiert,
- sie lesbar ist,
- es sich um korrektes SVG handelt und
- pro Zeile genau ein XML-Tag enthalten ist.

"""

def load_from_svg(filename:str) -> list[Rectangle]:
    pass


    
import unittest
class Test_load_svg(unittest.TestCase):
    OK = "\033[92m [OK] \033[0m"
    FAIL = "\033[91m [FAIL] \033[0m"
    
    def test_rectangle_count(self):
        print("\n=== Testing number of rectangles in example files ===")
        for (filename,count) in [
            ("resources/compression/example1/test1.svg", 500),
            ("resources/compression/example1/test2.svg", 160),
            ("resources/compression/example1/test3.svg", 56),
            ("resources/compression/example2/original.svg", 1000),
            ("resources/compression/example2/filtered_by_individual_cover.svg", 212),
            ("resources/compression/example2/filtered_by_probabilistic_method.svg", 55),
            ("resources/svg_output/chessboard_should_be.svg", 64),
            ("resources/svg_output/fibonacci_should_be.svg", 15),
            ("resources/good_luck.svg", 35),
        ]:            
            print(f"\t Number of rectangles in {filename:70} should be {count:4}", end=" ", flush=True)
            try:
                value = len(load_from_svg(filename))
                self.assertEqual(count,value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

    def test_example1_test1_colors(self):
        print("\n=== Testing the color of some rectangles in example1/test1 ===")
        rectangles = load_from_svg("resources/compression/example1/test1.svg")
        for (idx,color) in [
            (0,"darkgrey"),
            (1,"wheat"),
            (-4,"sienna")
        ]:            
            print(f"\t Color of the rectangle by index {idx:3} should be {color:15}", end=" ", flush=True)
            try:
                value = rectangles[idx].get_color()
                self.assertEqual(color,value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

if __name__ == '__main__':
    unittest.main(verbosity=0)