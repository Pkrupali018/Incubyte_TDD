import unittest

from app.chandrayan3_lunar_craft_app import Coordinates


class CoordinatesTestCase(unittest.TestCase):

    # Test case for coordinated which is by default origin or user defined
    def test_coordinates(self):
        coordinate = Coordinates()
        coordinates = coordinate.add_coordinates()
        self.assertEqual([0, 0, 0, 'N'], coordinates)
        coordinates_with_ip = coordinate.add_coordinates(1, 0, 2, 'U')
        self.assertEqual([1, 0, 2, 'U'], coordinates_with_ip)

    # Test case to verify the functionality of Move like forward and backward
    def test_move(self):
        move = Move()
        after_forward = move.forward(0, 0, 0, 'N')
        self.assertEqual([0, 1, 0, 'N'], after_forward)
        after_backward = move.backword(0, 0, 0, 'N')
        self.assertEqual([0, -1, 0, 0], after_backward)


if __name__ == '--main__':
    unittest.main()
