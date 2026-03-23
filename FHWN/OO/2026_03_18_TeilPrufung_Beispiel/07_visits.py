# Depends on 03

"""

Implement a two new methods for `POI_Manager` that lets you manage how many times a POI was visited:

def _get_visits(self, name:str) -> int|None
def _add_visit(self, name:str) -> None

The first returns, how many times a POI was visited in the past. If no such data is recorded for a POI yet, it returns 0, and initializes that data in the json file. If no POI with that name exists, the function returns None.

The second funtion increases that data by 1, or sets it to 1 if the data did not exist yet. 

"""

# Copy-paste your class defition here from 03 (or 06) and extend it with the new methods

class POI_manager:
    pass


# Tests 

import unittest
class Test_POI_Manager_4(unittest.TestCase):

    def test_get_visits(self):
        pass

    def test_add_visits(self):
        pass

if __name__ == '__main__':
    unittest.main()


