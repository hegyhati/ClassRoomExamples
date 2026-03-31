from main import parse_latitude, parse_longitude, POI_Manager, distance, is_close

import unittest
class AllTests(unittest.TestCase):
    def test_lat(self):
        self.assertAlmostEqual(
            parse_latitude('<trkpt lat="47.68013306893408298492431640625" lon="16.57821382395923137664794921875">'),
            47.680133,
            delta=0.0001,
            msg="Parsing latitude from a normal trkpt xml tag failed."
        )
        self.assertAlmostEqual(
            parse_latitude('    <trkpt lat="-12.431640625"      lon = "36"  >   '),
            -12.431640,
            delta=0.0001,
            msg="Parsing latitude from a trkpt xml tag with added whitespaces failed."
        )
    def test_lon(self):
        self.assertAlmostEqual(
            parse_longitude('<trkpt lat="47.68013306893408298492431640625" lon="16.57821382395923137664794921875">'),
            16.578213,
            delta=0.0001,
            msg="Parsing longitude from a normal trkpt xml tag failed."
        )
        self.assertAlmostEqual(
            parse_longitude('    <trkpt lat="-12.431640625"      lon = "36"  >   '),
            36,
            delta=0.0001,
            msg="Parsing longitude from a trkpt xml tag with added whitespaces failed."
        )

    def test_existing_poi_file(self):
        poim = POI_Manager("../poi_test.json")
        self.assertEqual(poim.get_poi_count(), 3,
            msg="The number of POIs in poi_test.json is 3."
        )

    def test_no_poi_file(self):
        try:
            poim = POI_Manager("this_file_does_not.exist") 
        except FileNotFoundError:
            return

        with self.assertRaises(FileNotFoundError, msg="get_poi_count should try to open the non-existent file and fail."):
            poim.get_poi_count()
    

    def test_poi_list(self):
        poim = POI_Manager("../poi_test.json")
        self.assertEqual(
            poim.get_pois(), 
            {"Herrentisch","Drei Säulen","Umbruch - Denkmal Paneuropäisches Picknick"},
            msg = "POI names from test_poi.json not returned correctly."
        )
    def test_existing_poi_positions(self):
        poim = POI_Manager("../poi_test.json")
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
        poim = POI_Manager("../poi_test.json")
        for name in ["none", "of", "these", "are", "pois"]:
            with self.subTest(name=name):
                self.assertIsNone(poim.get_pos(name), msg=f"Position for {name} should be None.")


    

if __name__ == '__main__':
    unittest.main()