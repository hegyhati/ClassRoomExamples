""" EN

DEPENDS ON 02 and 03

Copy-paste your code from 02 and 03.

Extend the Rectangle class, so that:
 - the constructor expects one more argument (at the end): color:str
 - if the provided color is valid, the rectangle will have that color, otherwise set it to "black"
 - A `get_color(self) -> str` method should be added that returns the color of the rectangle

"""

""" DE

ABHÄNGIG VON 02 und 03

Kopiere deinen Code aus 02 und 03 hier hinein.

Erweitere die Klasse `Rectangle` so, dass:
 - der Konstruktor ein zusätzliches Argument (am Ende) erwartet: `color: str`
 - falls die angegebene Farbe gültig ist, erhält das Rechteck diese Farbe, andernfalls wird die Farbe auf `"black"` gesetzt
 - eine Methode `get_color(self) -> str` hinzugefügt wird, die die Farbe des Rechtecks zurückgibt

"""

# Rectangle method
    def get_color(self) -> str:
        pass
    

# Tests     

import unittest
class Test_Rectangle(unittest.TestCase):
    OK = "\033[92m [OK] \033[0m"
    FAIL = "\033[91m [FAIL] \033[0m"

    good_colors = ["rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen"]
    bad_colors = ["vihreä", "grön", "verde", "zielony", "zöld", "grün"]
    
    def test_good_colors(self):
        print("\n=== Testing valid colors ===")
        for color in self.good_colors:
            r = Rectangle((0,0),(1,1),color)
            value = r.get_color()
            print(f"\tRectangle(..., {color:15})", end=" ", flush=True)
            try:                
                self.assertEqual(value,color)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

    def test_bad_colors(self):
        print("\n=== Testing invalid colors ===")
        for color in self.bad_colors:
            r = Rectangle((0,0),(1,1),color)
            value = r.get_color()
            print(f"\tRectangle(..., {color:15})", end=" ", flush=True)
            try:                
                self.assertEqual(value,"black")
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

        
if __name__ == '__main__':
    unittest.main(verbosity=0)