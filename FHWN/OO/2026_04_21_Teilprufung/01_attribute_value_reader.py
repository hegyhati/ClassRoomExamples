""" EN

Write the body of the two functions below.


`get_str_value` should return the value of an xml attribute as a `str`.

For example: 
    - xml_tag = '<html lang="en">' with key = "lang" should give back "en"
    - xml_tag = '<div id="footer" class="md-5">' with key = "id" should give back "footer"
    - xml_tag = '<div id="footer" class="md-5">', with key = class", " should give back -5"
    - xml_tag = '<circle r="30" cx="50" cy="15" fill="blue" />' with key = "r" should give back "30"
    - xml_tag = '<circle r="30" cx="50" cy="15" fill="blue" />' with key = "cx" should give back "50"
    - xml_tag = '<circle r="30" cx="50" cy="15" fill="blue" />' with key = "cy" should give back "15"

The function should return `None` if that tag is not present.

You can assume, that the name of the attribute(`key`) followed by a "=" is not a substring of anything (tag name, value), so this type of input will not happen:

xml_tag = <aafoo=aa foo="something" foo2="something else that has foo= in it"> 


`get_float_value` behaves the same, but returns a float, if the key exists. 
You can assume, that the value can be safely converted to a float.

"""

""" DE

Schreibe den Rumpf der beiden untenstehenden Funktionen.


`get_str_value` soll den Wert eines XML-Attributs als `str` zurückgeben.

Zum Beispiel:
    - xml_tag = '<html lang="en">' mit key = "lang" soll "en" zurückgeben
    - xml_tag = '<div id="footer" class="md-5">' mit key = "id" soll "footer" zurückgeben
    - xml_tag = '<div id="footer" class="md-5">' mit key = "class" soll "md-5" zurückgeben
    - xml_tag = '<circle r="30" cx="50" cy="15" fill="blue" />' mit key = "r" soll "30" zurückgeben
    - xml_tag = '<circle r="30" cx="50" cy="15" fill="blue" />' mit key = "cx" soll "50" zurückgeben
    - xml_tag = '<circle r="30" cx="50" cy="15" fill="blue" />' mit key = "cy" soll "15" zurückgeben

Die Funktion soll `None` zurückgeben, falls dieses Attribut nicht vorhanden ist.

Du kannst davon ausgehen, dass der Name des Attributs (`key`) gefolgt von einem "=" kein Teilstring von irgendetwas anderem ist (Tag-Name, Wert), d.h. folgende Art von Eingabe kommt nicht vor:

xml_tag = <aafoo=aa foo="something" foo2="something else that has foo= in it"> 


`get_float_value` verhält sich genauso, gibt aber einen Float zurück, falls key vorhanden ist.
Du kannst davon ausgehen, dass der Wert sicher in einen Float konvertiert werden kann.

"""

def get_str_value(xml_tag:str, key:str) -> str | None:
    pass
    
def get_float_value(xml_tag:str, key:str) -> float | None:
    pass
    
    
# Tests     
import unittest
class Test_XML_Attribute_Extractor(unittest.TestCase):
    OK = "\033[92m [OK] \033[0m"
    FAIL = "\033[91m [FAIL] \033[0m"
    
    def test_str(self):
        print("\n=== Testing existing str attribute reading ===")
        for xml_tag,attribute_name,expected_value in [
            ('<html lang="en">', "lang", "en"),
            ('<div id="footer" class="md-5">', "id", "footer"),
            ('<div id="footer" class="md-5">', "class", "md-5"),
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "r", "30"),
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "cx", "50"),
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "cy", "15"),
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "fill", "blue"),
            ('<trkpt lat="47.680133" lon="16.578213">', "lat", "47.680133"),
            ('<trkpt lat="47.680133" lon="16.578213">', "lon", "16.578213"),
        ] : 
            print(f"\t{xml_tag:50} {attribute_name:10} {expected_value:10}", end=" ", flush=True)
            try:
                value = get_str_value(xml_tag, attribute_name)
                self.assertEqual(value, expected_value)  
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
    
    def test_non_existent_str(self):
        print("\n=== Testing non-existent str attribute reading ===")
        for xml_tag, wrong_attribute_name in [
            ('<html lang="en">', "id"),
            ('<div id="footer" class="md-5">', "style"),
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "circle"),
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "blue"),
            ('<trkpt lat="47.680133" lon="16.578213">', "elav"),
            ('<trkpt lat="47.680133" lon="16.578213">', "LAT"),
        ] : 
            print(f"\t{xml_tag:50} {wrong_attribute_name:10}", end=" ", flush=True)
            try:
                value = get_str_value(xml_tag,wrong_attribute_name)
                self.assertIsNone(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
    
    def test_float(self):
        print("\n=== Testing existent float attribute reading ===")
        for xml_tag,attribute_name,expected_value in [
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "r", 30.0),
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "cx", 50.0),
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "cy", 15.0),
            ('<trkpt lat="47.680133" lon="16.578213">', "lat", 47.680133),
            ('<trkpt lat="47.680133" lon="16.578213">', "lon", 16.578213),
        ] : 
            print(f"\t{xml_tag:50} {attribute_name:10} {expected_value:10}", end=" ", flush=True)
            try:
                value = get_float_value(xml_tag, attribute_name)
                self.assertAlmostEqual(value, expected_value, delta="0.01")
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
            
    
    def test_non_existent_float(self):
        print("\n=== Testing non-existent str attribute reading ===")
        for xml_tag, wrong_attribute_name in [
            ('<html lang="en">', "id"),
            ('<div id="footer" class="md-5">', "style"),
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "circle"),
            ('<circle r="30" cx="50" cy="15" fill="blue" />', "blue"),
            ('<trkpt lat="47.680133" lon="16.578213">', "elav"),
            ('<trkpt lat="47.680133" lon="16.578213">', "LAT"),
        ] : 
            print(f"\t{xml_tag:50} {wrong_attribute_name:10}", end=" ", flush=True)
            try:
                value = get_float_value(xml_tag,wrong_attribute_name)
                self.assertIsNone(value)
            except Exception:
                print(f"{self.FAIL} got: {value}", flush=True)
                raise
            else:
                print(self.OK, flush=True)        
        print(f"=== All tests {self.OK} ===\n\n")
            
     
if __name__ == '__main__':
    unittest.main(verbosity=0)