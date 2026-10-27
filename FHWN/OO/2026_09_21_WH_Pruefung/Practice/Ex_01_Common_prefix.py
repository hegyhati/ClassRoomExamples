""" EN
Write a function that returns the longest common prefix in a case-insesitive way of two strings.

Bonus: Write the function that returns the longest common substring.
"""


""" DE
Schreibe eine Funktion, die den längsten gemeinsamen Präfix zweier Zeichenketten case-insensitive ermittelt.

Bonus: Schreibe eine Funktion, die die längste gemeinsame Teilzeichenkette zurückgibt.
"""

def longest_common_prefix(w1:str, w2:str) -> str:
    pass

def longest_common_substring(w1:str, w2:str) -> str:
    pass


# Tests     
import unittest
class Test_XML_Attribute_Extractor(unittest.TestCase):
    OK = "\033[92m [OK] \033[0m"
    FAIL = "\033[91m [FAIL] \033[0m"
    
    def test_longest_common_prefix(self):
        print("\n=== Testing longest common prefix ===")
        for w1,w2,prefix in [
            ("apple", "banana", ""),
            ("geometry", "geology", "geo"),
            ("Network", "negative", "ne"),

        ] : 
            print(f"\t{w1:15} {w2:15}  ->  '{prefix:5}'", end=" ", flush=True)
            try:
                value = longest_common_prefix(w1, w2)
                self.assertEqual(value, prefix)  
            except Exception:
                print(f"{self.FAIL} got: '{value}'", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
    
        
    def test_longest_common_substring(self):
        print("\n=== Testing longest_common_substring ===")
        for w1,w2,substring in [
            ("apple", "banana", "a"),
            ("geometry", "geology", "geo"),
            ("Network", "negative", "ne"),
            ("music", "amusement", "mus")

        ] : 
            print(f"\t{w1:15} {w2:15}  ->  '{substring:5}'", end=" ", flush=True)
            try:
                value = longest_common_substring(w1, w2)
                self.assertEqual(value, substring)  
            except Exception:
                print(f"{self.FAIL} got: '{value}'", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
    
            
     
if __name__ == '__main__':
    unittest.main(verbosity=0)