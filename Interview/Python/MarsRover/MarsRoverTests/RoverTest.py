import unittest
import Plateau
import Rover


class RoverTest(unittest.TestCase):

    def testNormalRover(self):
        plateau = Plateau.Plateau(5, 3)
        rover = Rover.Rover(1, 2, 'N', 'L', plateau)
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'N')
        self.assertEquals(rover.commands, 'L')
        self.assertEquals(rover.plateau, plateau)

    def testRoverInvalidCoordinates(self):
        plateau = Plateau.Plateau(5, 3)
        self.assertRaises(ValueError, Rover.Rover, 'a', 2, 'N', 'L', plateau)

    def testRoverInvalidOrientation(self):
        plateau = Plateau.Plateau(5, 3)
        self.assertRaises(ValueError, Rover.Rover, 1, 2, 3, 'L', plateau)

    def testExploreEmptyCommands(self):
        NotImplemented


def main():
    unittest.main()

if __name__ == '__main__':
    main()