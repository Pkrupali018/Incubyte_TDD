import unittest

class CoordinatesTestCase(unittest.TestCase):

    def test_coordinates(self):
        coordinate = Coordinates()
        result = coordinate.add_coordinates()
        self.assertEquals([0,0,0,'N'], result.split())

if __name__ == '--main__':
    unittest.main()