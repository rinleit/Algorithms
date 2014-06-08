import unittest
import Plateau


class PlateauTest(unittest.TestCase):

    def testNormalPlateau(self):
        plateau = Plateau.Plateau(5, 3)
        self.assertEqual(plateau.max_x, 5)
        self.assertEqual(plateau.max_y, 3)

    def testBadPlateau(self):
        self.assertRaises(ValueError, Plateau.Plateau, 'a', 3)

    def testValidPosition(self):
        plateau = Plateau.Plateau(5, 3)
        self.assertTrue(plateau.is_valid_position(1, 1))

    def testValidPositionEdgeCase(self):
        plateau = Plateau.Plateau(5, 3)
        self.assertTrue(plateau.is_valid_position(5, 3))

    def testInvalidPosition(self):
        plateau = Plateau.Plateau(5, 3)
        self.assertFalse(plateau.is_valid_position(6, 1))


def main():
    unittest.main()

if __name__ == '__main__':
    main()