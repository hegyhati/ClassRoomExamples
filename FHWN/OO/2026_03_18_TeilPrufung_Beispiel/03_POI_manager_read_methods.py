# Depends on 02

"""

Extend `POI_manager` with new methods:
 - `get_pois() -> set[str]` : returns the set of the names of POIs
 - `get_pos(str) -> tuple[float,float]|None : returns the position as a (lat,lon) `float` pair for the POI, or `None` if no POI with that name exists.

 """

# Copy-paste your class defition here from 02 and extend it with the new methods

class POI_Manager:
    pass


# Tests 

import unittest
class Test_POI_Manager_2(unittest.TestCase):

    def test_poi_list(self):
        poim = POI_Manager("poi_test.json")
        self.assertEqual(
            poim.get_pois(), 
            {"Herrentisch","Drei Säulen","Umbruch - Denkmal Paneuropäisches Picknick"},
            msg = "POI names from test_poi.json not returned correctly."
        )

    def test_existing_poi_positions(self):
        poim = POI_Manager("poi_test.json")
        for name, exp_pos in [
            ("Herrentisch", (47.6648127, 16.4217079)),
            ("Drei Säulen", (47.6393216, 16.4980057)),
            ("Umbruch - Denkmal Paneuropäisches Picknick", (47.7567819, 16.6210290)),
        ]:
            with self.subTest(name=name):
                pos = poim.get_pos(name)
                self.assertAlmostEqual(pos[0], exp_pos[0], delta=0.0001, msg=f"Wrong latitude for {name}")
                self.assertAlmostEqual(pos[1], exp_pos[1], delta=0.0001, msg=f"Wrong longitude for {name}")

    def test_non_existing_poi_positions(self):
        poim = POI_Manager("poi_test.json")
        for name in ["none", "of", "these", "are", "pois"]:
            with self.subTest(name=name):
                self.assertIsNone(poim.get_pos(name), msg=f"Position for {name} should be None.")

if __name__ == '__main__':
    unittest.main()

