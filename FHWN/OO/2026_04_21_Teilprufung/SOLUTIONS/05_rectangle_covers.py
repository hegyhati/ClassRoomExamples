"""

DEPENDS on 04

Optional: Only 02 is enough if you extend the constructor with a disregarded last argument so that the tests below don't crash.

Copy-paste your code from 04 (or 02), and extend the Rectangle class with a `covers(self, other:"Rectangle") -> bool` method, that expects another rectangle, and returns, whether that rectangle is completely covered by self.

"""

""" DE

ABHÄNGIG VON 04

Optional: 02 ist ausreichend, wenn du den Konstruktor um ein zusätzliches, ignoriertes letztes Argument erweiterst, sodass die untenstehenden Tests nicht abstürzen.

Kopiere deinen Code aus 04 (oder 02) hier hinein und erweitere die Klasse `Rectangle` um eine Methode  `covers(self, other: "Rectangle") -> bool`, die ein weiteres Rechteck erwartet und zurückgibt, ob dieses Rechteck vollständig von `self` überdeckt wird.

"""

import json

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

    def contains(self,point:tuple[float,float]) -> bool:
        return self.__minx <= point[0] <= self.__maxx and self.__miny <= point[1] <= self.__maxy

    def get_color(self) -> str:
        return self.__color     
        
    def covers(self, other:"Rectangle") -> bool:
        return self.__minx <= other.__minx and self.__maxx >= other.__maxx and self.__miny <= other.__miny and self.__maxy >= other.__maxy
    

# Tests     
import random
def rand(a,b) -> float:
    return round(random.uniform(a,b), ndigits=2)

import unittest
class Test_Rectangle(unittest.TestCase):
    OK = "\033[92m [OK] \033[0m"
    FAIL = "\033[91m [FAIL] \033[0m"

    colors = ["green", "vihreä", "grön", "verde", "zielony", "zöld", "grün"]
    
    def test_self_cover(self):
        print("\n=== Testing self cover ===")
        for _ in range(10):
            (x,y,w,h) = (rand(10,50) for _ in range(4))
            c = random.choice(self.colors)
            print(f"\tRectangle(({x:6.2f},{y:6.2f}),({x+w:6.2f},{y+h:6.2f}), {c:10}) covers itself", end=" ", flush=True)
            try:
                r = Rectangle( (x,y), (x+w,y+h), c)
                value = r.covers(r)                
                self.assertTrue(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

    def test_middle_rectangle_cover(self):
        print("\n=== Testing middle being covered ===")
        for _ in range(10):
            (x,y,w,h) = (rand(10,50) for _ in range(4))
            (x2,y2) = (x+w/4, y+h/4)
            c = random.choice(self.colors)
            print(f"\tRectangle(({x:6.2f},{y:6.2f}),({x+w:6.2f},{y+h:6.2f}),...) covers Rectangle(({x2:6.2f},{y2:6.2f}),({x2+w/2:6.2f},{y2+h/2:6.2f}),...)", end=" ", flush=True)
            try:
                r = Rectangle( (x,y), (x+w,y+h), c)
                r2 = Rectangle( (x2,y2), (x2+w/2,y2+h/2), "")
                value = r.covers(r2)                
                self.assertTrue(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
    
    def test_random_cover(self):
        print("\n=== Testing random covered ===")
        for _ in range(10):
            (x,y,w,h) = (rand(10,50) for _ in range(4))
            x2 = rand(x,x+w)
            y2 = rand(y,y+h)
            w2 = rand(0,x+w-x2)
            h2 = rand(0,y+h-y2)
            print(f"\tRectangle(({x:6.2f},{y:6.2f}),({x+w:6.2f},{y+h:6.2f}),...) covers Rectangle(({x2:6.2f},{y2:6.2f}),({x2+w2:6.2f},{y2+h2:6.2f}),...)", end=" ", flush=True)
            try:
                r = Rectangle( (x,y), (x+w,y+h), "")
                r2 = Rectangle( (x2,y2), (x2+w2,y2+h2), "")
                value = r.covers(r2)                
                self.assertTrue(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

    def test_random_not_cover(self):
        print("\n=== Testing random not covered ===")
        for _ in range(10):
            (x,y,w,h) = (rand(10,50) for _ in range(4))
            (x2,y2,w2,h2) = (rand(10,50) for _ in range(4))
            x2 = rand(0,x-1)
            print(f"\tRectangle(({x:6.2f},{y:6.2f}),({x+w:6.2f},{y+h:6.2f}),...) does not cover Rectangle(({x2:6.2f},{y2:6.2f}),({x2+w2:6.2f},{y2+h2:6.2f}),...)", end=" ", flush=True)
            try:
                r = Rectangle( (x,y), (x+w,y+h), "")
                r2 = Rectangle( (x2,y2), (x2+w2,y2+h2), "")
                value = r.covers(r2)                
                self.assertFalse(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

        
if __name__ == '__main__':
    unittest.main(verbosity=0)