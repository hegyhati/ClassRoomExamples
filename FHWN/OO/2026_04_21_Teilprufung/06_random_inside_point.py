""" EN

DEPENDS on 04

Optional: Only 02 is enough if you extend the constructor with a disregarded last argument so that the tests below don't crash.

Copy-paste your code from 04/05 (or 02), and extend the Rectangle class with a `get_random_point(self) -> tuple[float,float]` method, that returns a random inside point from the rectangle. 

You can use the `uniform` function from the `random` module:
https://docs.python.org/3/library/random.html#random.uniform

"""

""" DE

ABHÄNGIG VON 04

Optional: 02 ist ausreichend, wenn du den Konstruktor um ein zusätzliches, ignoriertes letztes Argument erweiterst, sodass die untenstehenden Tests nicht abstürzen.

Kopiere deinen Code aus 04/05 (oder 02) hier hinein und erweitere die Klasse `Rectangle` um eine Methode `get_random_point(self) -> tuple[float, float]`, die einen zufälligen Punkt innerhalb des Rechtecks zurückgibt.

Du kannst dafür die Funktion `uniform` aus dem Modul `random` verwenden:
https://docs.python.org/3/library/random.html#random.uniform

"""

# Rectangle method
    def get_random_point(self) -> tuple[float,float]:
        pass

# Tests     
import random
def rand(a,b) -> float:
    return round(random.uniform(a,b), ndigits=2)

import unittest
class Test_Rectangle(unittest.TestCase):
    OK = "\033[92m [OK] \033[0m"
    FAIL = "\033[91m [FAIL] \033[0m"
    
    def test_random_containment(self):
        print("\n=== Testing if random point is inside ===")
        for _ in range(10):
            (x,y,w,h) = (rand(10,50) for _ in range(4))
            print(f"\tRectangle(({x:6.2f},{y:6.2f}),({x+w:6.2f},{y+h:6.2f}),...) covers ", end=" ", flush=True)
            try:
                r = Rectangle( (x,y), (x+w,y+h), "")
                p = r.get_random_point()
                print(f"({p[0]:6.2f},{p[1]:6.2f}) ", end="", flush=True)
                value = r.contains(p)                
                self.assertTrue(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
    
    def test_random_unformness(self):
        print("\n=== Testing if random point is inside ===")
        for _ in range(10):
            print(f"\tRectangle( (0,0) , (10,10) , ...) gets random point inside ", end=" ", flush=True)
            try:
                r = Rectangle((0,0),(10,10),"")
                x = rand(0,9)
                y = rand(0,9)
                print(f"({x:6.2f},{y:6.2f}) - ({x+1:6.2f},{y+1:6.2f}) at least 5 times in 1000 tries", end="", flush=True)
                count = 0
                for _ in range(5000):
                    p = r.get_random_point()
                    if x <= p[0] <= x+1 and y <= p[1] <= y+1:
                        count +=1               
                self.assertGreaterEqual(count,5)
            except Exception:
                print(f"{self.FAIL} got: {count}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

        
if __name__ == '__main__':
    unittest.main(verbosity=0)