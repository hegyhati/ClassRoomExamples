"""

Create a class called `POI_Manager`

The class should have a constructor, that expects a filename of a JSON file, that stores the POI data.

The class should have one public method besides the constructor for now:

`get_poi_count() -> int` : returns the number of POIs stored in that file as an `int`

Note: efficiency is not a concern, but consistency is, thus, open the file each time this function is called.

"""

class POI_Manager:
    pass


# Tests 

import unittest
class Test_POI_Manager_1(unittest.TestCase):

    def test_existing_poi_file(self):
        poim = POI_Manager("poi_test.json")
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

if __name__ == '__main__':
    unittest.main()

