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

import random

def get_str_value(xml_tag:str, key:str) -> str | None:
    parts = xml_tag.split(" "+key)
    return None if len(parts) == 1 or not parts[1].strip().startswith("=") else parts[1].split('"')[1]

def get_float_value(xml_tag:str, key:str) -> float | None:
    return float(value) if (value:=get_str_value(xml_tag,key)) is not None else None

def is_valid_color(colorname:str) -> bool:
    with open("colors.json") as f:
        colors = json.load(f)
    return colorname.lower().strip() in colors

class Rectangle:
    __minx: float
    __maxx: float
    __miny: float
    __maxy: float
    __color: str

    def __init__(self, topleft:tuple[float,float], bottomright:tuple[float,float], color:str):
        self.__minx = topleft[0]
        self.__miny = topleft[1]
        self.__maxx = bottomright[0]
        self.__maxy = bottomright[1]
        self.__color = color if is_valid_color(color) else "black"

    def to_svg(self) -> str:
        return f'<rect x="{self.__minx}" y="{self.__miny}" width="{self.__maxx-self.__minx}" height="{self.__maxy-self.__miny}" fill="{self.__color}" />'
    
    def covers(self, other:"Rectangle") -> bool:
        return self.__minx <= other.__minx and self.__maxx >= other.__maxx and self.__miny <= other.__miny and self.__maxy >= other.__maxy
    
    def get_random_point(self) -> tuple[float,float]:
        return random.uniform(self.__minx, self.__maxx), random.uniform(self.__miny,self.__maxy)

    def contains(self,point:tuple[float,float]) -> bool:
        return self.__minx <= point[0] <= self.__maxx and self.__miny <= point[1] <= self.__maxy

    def get_color(self) -> str:
        return self.__color 
    

import json
def load_from_svg(filename:str) -> list[Rectangle]:
    rectangles = []
    with open(filename) as f:
        for line in f:
            if "<rect" in line:
                x = get_float_value(line,"x")
                y = get_float_value(line,"y")
                w = get_float_value(line,"width")
                h = get_float_value(line,"height")
                c = get_str_value(line,"fill")
                if x is not None and y is not None and w is not None and h is not None and c is not None:
                    rectangles.append(Rectangle((x,y),(x+w,y+h),c))
    return rectangles


    
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