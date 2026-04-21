""" EN

Crate a `Rectangle` class with the constructor and the given method.

The constructor receives two (x,y)-tuples for the topleft and bottomright corner of the rectangle.

The coordinates in the project will always be (x,y) tuples in the SVG coordinate system, where (0,0) is the topleft corner of the image, and x increases to the right, and y INCREASES DOWNWARDS. 

Like this:

(0,0) --- (1,0) --- (2,0) --- ... 
  |         |         |
(0,1) --- (1,1) --- (2,1) --- ... 
  |         |         |
(0,2) --- (1,2) --- (2,2) --- ... 
  |         |         |
(0,3) --- (1,3) --- (2,3) --- ... 

The constructor should naturally store the rectangle.

The `contains` method receives a coordinate and return, whether it is within/covered by the rectangle. (Corners and sides are also covered.)

"""

""" DE

Erstelle eine Klasse `Rectangle` mit dem Konstruktor und der angegebenen Methode.

Der Konstruktor erhält zwei (x,y)-Tupel für die linke obere und die rechte untere Ecke des Rechtecks.

Die Koordinaten im Projekt sind immer (x,y)-Tupel im SVG-Koordinatensystem, wobei (0,0) die linke obere Ecke des Bildes ist, x nach rechts zunimmt und y NACH UNTEN ZUNIMMT.

So:

(0,0) --- (1,0) --- (2,0) --- ... 
  |         |         |
(0,1) --- (1,1) --- (2,1) --- ... 
  |         |         |
(0,2) --- (1,2) --- (2,2) --- ... 
  |         |         |
(0,3) --- (1,3) --- (2,3) --- ... 

Der Konstruktor soll das Rechteck entsprechend speichern.

Die Methode `contains` erhält eine Koordinate und gibt zurück, ob diese innerhalb des Rechtecks liegt bzw. vom Rechteck abgedeckt ist. (Ecken und Seiten zählen ebenfalls als abgedeckt.)

"""

class Rectangle:

    def __init__(self, topleft:tuple[float,float], bottomright:tuple[float,float]):
        pass

    def contains(self,point:tuple[float,float]) -> bool:
        pass
    

# Tests     
import random
def rand(a,b) -> float:
    return round(random.uniform(a,b), ndigits=2)

import unittest
class Test_Rectangle(unittest.TestCase):
    OK = "\033[92m [OK] \033[0m"
    FAIL = "\033[91m [FAIL] \033[0m"


    testcases = [
        ( (0,0), (2,2) ),
        ( (0,0), (100,100) ),
        ( (-100,-100), (0,0) ),
        ( (-100,-100), (50,50) ),
        ( (-100,-100), (-50,-50) ),
        ( (-10,10), (10,100) ),
        ( (rand( 0,50),rand(0,50)), (rand(50,100),rand(50,100)) ),
        ( (rand( 0,50),rand(0,50)), (rand(50,100),rand(50,100)) ),
        ( (rand(-100,0),rand(-100,0)), (rand(0,100),rand(0,100)) ),
        ( (rand(-100,0),rand(-100,0)), (rand(0,100),rand(0,100)) ),
        ( (rand(-100,-50),rand(-100,-50)), (rand(-50,50),rand(-50,50)) ),
    ]
    
    def test_middle_point(self):
        print("\n=== Testing Rectangle creation and middle point containment ===")
        for tl,br in self.testcases:
            mp = ( round((tl[0]+br[0])/2, ndigits=2), round((tl[1]+br[1])/2,ndigits=2) )
            print(f"\tRectangle({str(tl):^20},{str(br):^20})  middle point: {str(mp):20}", end=" ", flush=True)
            try:
                r = Rectangle(tl,br)
                value = r.contains(mp)
                self.assertTrue(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
    
    def test_bottomleft(self):
        print("\n=== Testing Rectangle creation and middle point containment ===")
        for tl,br in self.testcases:
            bl = ( tl[0], br[1] )
            print(f"\tRectangle({str(tl):^20},{str(br):^20})  bottom-left point: {str(bl):20}", end=" ", flush=True)
            try:
                r = Rectangle(tl,br)
                value = r.contains(bl)
                self.assertTrue(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
    
    def test_random_inside(self):
        print("\n=== Testing Rectangle creation and random inside point containment ===")
        for tl,br in self.testcases:
            rp = ( rand(tl[0],br[0]), rand(tl[1],br[1]) )
            print(f"\tRectangle({str(tl):^20},{str(br):^20})  random inside point: {str(rp):20}", end=" ", flush=True)
            try:
                r = Rectangle(tl,br)
                value = r.contains(rp)
                self.assertTrue(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

    
    
    def test_random_to_the_left(self):
        print("\n=== Testing Rectangle creation and point to the left containment ===")
        for tl,br in self.testcases:
            rp = ( rand(-200,tl[0]), rand(tl[1],br[1]) )
            print(f"\tRectangle({str(tl):^20},{str(br):^20})  random point to the left: {str(rp):20}", end=" ", flush=True)
            try:
                r = Rectangle(tl,br)
                value = r.contains(rp)
                self.assertFalse(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

if __name__ == '__main__':
    unittest.main(verbosity=0)