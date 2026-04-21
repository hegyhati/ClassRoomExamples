""" EN

Implement the function below, that receives a colorname, and returns whether it is a valid color name in an SVG. 

The valid color names are listed in `colors.json`, and are not to be copied here. 
(You have to open the file from the code.)

"""

""" DE

Implementiere die untenstehende Funktion, die einen Farbnamen erhält und zurückgibt, ob es sich um einen gültigen Farbnamen in SVG handelt.

Die gültigen Farbnamen sind in `colors.json` aufgelistet und dürfen hier nicht kopiert werden.  
(Du musst die Datei aus dem Code heraus öffnen.)

"""

import json

def is_valid_color(colorname:str) -> bool:
    pass

# Tests     
import unittest
class Test_Rectangle(unittest.TestCase):
    OK = "\033[92m [OK] \033[0m"
    FAIL = "\033[91m [FAIL] \033[0m"


    good = [ "red", "green", "paleturquoise", "gold" ]
    bad = ["rot", "gRüN", " PIROS", "re d", ".red" ]
    
    def test_good_colors(self):
        print("\n=== Testing valid colors ===")
        for color in self.good:
            try:
                c = f'"{color}"'
                print(f'\t{c:20}', end=" ")
                value = is_valid_color(color)
                self.assertTrue(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
    
    def test_good_colors_with_capital_second_letter(self):
        print("\n=== Testing valid colors witch capital second letter ===")
        for color in self.good:
            try:
                color = color[:1]+color[1].upper()+color[2:]
                c = f'"{color}"'
                print(f'\t{c:20}', end=" ")
                value = is_valid_color(color)
                self.assertTrue(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
    
    def test_good_colors_with_additional_spaces(self):
        print("\n=== Testing valid colors witch additional spaces ===")
        for idx,color in enumerate(self.good):
            try:
                color = " " * idx + color + (20-len(color)-idx)*" "
                c = f'"{color}"'
                print(f'\t{c:30}', end=" ")
                value = is_valid_color(color)
                self.assertTrue(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")

if __name__ == '__main__':
    unittest.main(verbosity=0)