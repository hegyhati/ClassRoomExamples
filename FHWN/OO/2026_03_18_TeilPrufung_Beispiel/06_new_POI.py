# Depends on 03,05 (and 04 for bonus)

"""

Implement a new method for `POI_Manager` that lets you add a new POI:

def add_new_poi(self, name:str, pos:tuple[float,float]) -> None:

Moreover, extend the code from 05, such that menu option 2 (adding a new POI) is already implemented using the above method: Ask for the name and position of a new poi, then register it into poi.json.

BONUS: Check if there is another POI close by, and if yes, ask an "Are you sure you want to add this?" before adding.

"""

# Copy-paste your class defition here from 03 and extend it with the new method

class POI_manager:
    pass


# Copy-paste your menu code from 05 and implement the menu option 2.


# Tests 

import unittest
class Test_POI_Manager_3(unittest.TestCase):

    def test_add_new_POI(self):
        pass

if __name__ == '__main__':
    unittest.main()


