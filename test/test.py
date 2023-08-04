import unittest

from app.chandrayan3_lunar_craft_app import Coordinates


class CoordinatesTestCase(unittest.TestCase):

    def test_coordinates(self):
        coordinate = Coordinates()
        result = coordinate.add_coordinates()
        self.assertEqual([0, 0, 0, 'N'], result)


if __name__ == '--main__':
    unittest.main()
