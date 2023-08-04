import unittest

from app.chandrayan3_lunar_craft_app import Coordinates


class CoordinatesTestCase(unittest.TestCase):

    def test_coordinates(self):
        coordinate = Coordinates()
        result = coordinate.add_coordinates()
        self.assertEqual([0, 0, 0, 'N'], result)
        result_with_ip = coordinate.add_coordinates(1, 0, 2, 'U')
        self.assertEqual([1, 0, 2, 'U'], result_with_ip)


if __name__ == '--main__':
    unittest.main()
