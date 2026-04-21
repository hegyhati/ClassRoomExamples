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

import random
import json

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
    



def write_to_svg(filename:str, width:float, height:float, rectangles:list[Rectangle]) -> None:
    with open(filename, "w") as f:
        f.write(f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n')
        for rectangle in rectangles:
            f.write(rectangle.to_svg()+'\n')
        f.write('</svg>\n')

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

import os

def fetch_width_height(filename:str) -> tuple[float,float]: 
    with open(filename) as f:
        for line in f:
            if "<svg " in line:
                return get_float_value(line,"width"), get_float_value(line,"height")

def filter_by_individual_cover(filename:str, suffix:str="_fbic") -> None:
    w,h = fetch_width_height(filename)
    rectangles = load_from_svg(filename)
    filtered:list[Rectangle] = []
    for idx1 in range(len(rectangles)):
        for idx2 in range(idx1+1, len(rectangles)):
            if rectangles[idx2].covers(rectangles[idx1]):
                break
        else:
            filtered.append(rectangles[idx1])
    name,ext = os.path.splitext(filename)
    write_to_svg(name+suffix+ext,w,h,filtered)

TRIES = 10000
def probabilistic_filter(filename:str, suffix:str="_pf") -> None:
    w,h = fetch_width_height(filename)
    rectangles = load_from_svg(filename)
    filtered:list[Rectangle] = []
    for idx1 in range(len(rectangles)):
        for _ in range(TRIES):
            point = rectangles[idx1].get_random_point()
            for idx2 in range(idx1+1, len(rectangles)):
                if rectangles[idx2].contains(point):
                    break
            else:
                filtered.append(rectangles[idx1])
                break
    name,ext = os.path.splitext(filename)
    write_to_svg(name+suffix+ext,w,h,filtered)


if __name__ == "__main__":
    filter_by_individual_cover("resources/compression/example1/test1.svg")
    probabilistic_filter("resources/compression/example1/test1.svg")

    