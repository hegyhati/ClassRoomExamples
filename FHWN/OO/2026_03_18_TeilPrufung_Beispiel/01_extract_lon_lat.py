"""

Write two functions that receive a string like this example:

<trkpt lat="47.68013306893408298492431640625" lon="16.57821382395923137664794921875">

... and return the longitude/latitude as `float`.

"""

def parse_latitude(trkpt_str:str) -> float:
    pass

def parse_longitude(trkpt_str:str) -> float:
    pass


# Tests 

import unittest
class Test_GPX_Pos_Parse(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()

