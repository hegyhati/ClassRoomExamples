"""
Implement the function below, that expects a string, and a length.
The function should "left-pad" the string with spaces to achieve the desired (length).

E.g.: "todo", 6 => "  todo"

Complett specifications:
 - if the word is shorter than the provided length, left-pad it with spaces
 - if exactly the length, return the word as is
 - if it is longer, crop the end of the word and end it with … such that the required length is achieved
 - in case of non-positive lengths a ValueError should be raised
"""

def leftpad(word:str, length:int) -> str:
    if length < 1: raise ValueError
    return " "*(length-len(word)) + word if len(word) <= length else word[:(length-1)] + "…"
    
# Tests     
import unittest
import random
class Test_leftpad(unittest.TestCase):
    OK = "\033[92m [OK] \033[0m"
    FAIL = "\033[91m [FAIL] \033[0m"
    
    def test_00_fix(self):
        print("\n=== Testing leftpad where length is longer  than word ===")
        for word,length,expected_value in [
            ("left", 5, " left"),
            ("pad",  5, "  pad"),
            ("left", 10, "      left"),
            ("pad",  10, "       pad"),
        ] : 
            print(f"\t{word:10} {length:2}     '{expected_value}'" + " "*(15-length), end=" ", flush=True)
            try:
                value = leftpad(word, length)
                self.assertEqual(value, expected_value)  
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} Wooohooo!!! ===\n\n")

    def test_01_random_length(self):
        print("\n=== Testing leftpad return length whith foobar on random lengths ===")
        for _ in range(10):
            length = random.randint(1,20)
            print(f"\tLength: {length:2} ", end=" ", flush=True)
            try:
                value = leftpad("foobar", length)
                print(f"Got: '{value}'"+" "*(20-length), end=" ", flush=True)
                self.assertEqual(len(value), length)  
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} Wooohooo!!! ===\n\n")

    def test_03_random_word_with_own_length(self):
        print("\n=== Testing leftpad on random word with own length to equal itself  ===")
        for _ in range(10):
            word = "".join(chr(random.randint(65,90)) for _ in range(random.randint(5,15)))
            print(f"\tWord: '{word}' "+ " "*(15-len(word)), end=" ", flush=True)
            try:
                value = leftpad(word, len(word))
                print(f"Got: '{value}'"+ " "*(15-len(word)), end=" ", flush=True)
                self.assertEqual(value, word)  
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} Wooohooo!!! ===\n\n")

    def test_04_random_long_word_with_length_of_2(self):
        print("\n=== Testing leftpad on random long (>2 char) word with length of 2  ===")
        for _ in range(10):
            word = "".join(chr(random.randint(65,90)) for _ in range(random.randint(5,15)))
            print(f"\tWord: '{word}' "+ " "*(15-len(word)), end=" ", flush=True)
            try:
                value = leftpad(word, 2)
                print(f"Got: '{value}'"+ " "*(15-len(value)), end=" ", flush=True)
                self.assertEqual(value, word[0]+"…")  
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} Wooohooo!!! ===\n\n")

    def test_05_random_long_word_with_length_of_1(self):
        print("\n=== Testing leftpad on random long (>2 char) word with length of 1  ===")
        for _ in range(10):
            word = "".join(chr(random.randint(65,90)) for _ in range(random.randint(5,15)))
            print(f"\tWord: '{word}' "+ " "*(15-len(word)), end=" ", flush=True)
            try:
                value = leftpad(word, 1)
                print(f"Got: '{value}'"+ " "*(15-len(value)), end=" ", flush=True)
                self.assertEqual(value, "…")  
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} Wooohooo!!! ===\n\n")

    def test_06_empty_string_with_length_of_1(self):
        print("\n=== Testing leftpad on empty string word with length of 1  ===")
        self.assertEqual(leftpad("",1)," ")     
        print(f"=== Test {self.OK} Wooohooo!!! ===\n\n")

    def test_07_random_word(self):
        print("\n=== Testing length on random word with length of 10  ===")
        for _ in range(10):
            word = "".join(chr(random.randint(65,90)) for _ in range(random.randint(5,15)))
            print(f"\tWord: '{word}' "+ " "*(15-len(word)), end=" ", flush=True)
            try:
                value = leftpad(word, 10)
                print(f"Got: '{value}'", end=" ", flush=True)
                self.assertEqual(len(value), 10)  
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} Wooohooo!!! ===\n\n")
    
    def test_08_non_positive_lengths(self):
        print("\n=== Testing length on random word with invalid length  ===")
        for length in range(0,-5,-1):
            word = "".join(chr(random.randint(65,90)) for _ in range(random.randint(5,15)))
            print(f"\tLength: {length:2} Word: '{word}' "+ " "*(15-len(word)), end=" ", flush=True)
            try:
                with self.assertRaises(ValueError):
                    value = leftpad(word, length)                  
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} Wooohooo!!! ===\n\n")

     
if __name__ == '__main__':
    unittest.main(verbosity=0)