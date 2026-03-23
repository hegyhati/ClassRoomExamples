"""

Write two functions:
 - one to return the estimated distance of 2 points
 - one to tell, if two points are close or not (=within the distance of a provided treshold value)

For an estimation, you can assume, that lon/lat are 2D coordinates on a flat surface, and around this region:

1 latitude degree = 111 km
1 longitude degree = 75 km

Moreover the treshold value should have a default of 50 meters.


"""


def distance(pos1:tuple[float,float], pos2:tuple[float,float]) -> float:
    pass

def is_close(pos1:tuple[float,float], pos2:tuple[float,float], treshold_m:float) -> bool:
    pass


# Tests 

import unittest
class Test_Distance(unittest.TestCase):

    def test_distance(self):
        pass

    def test_is_close(self):
        pass

if __name__ == '__main__':
    unittest.main()

