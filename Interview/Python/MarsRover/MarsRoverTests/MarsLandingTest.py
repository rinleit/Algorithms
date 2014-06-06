import unittest
import MarsLanding
import Plateau
from InputErrors import *


class MarsLandingTest(unittest.TestCase):

    mars_landing = MarsLanding.MarsLanding()
    plateau = Plateau.Plateau(5, 5)

    def testCreateNormalPlateu(self):
        plateau = self.mars_landing.create_plateau('5 5')
        self.assertTrue(plateau.max_x, 5)
        self.assertTrue(plateau.max_y, 5)

    def testInvalidPlateu(self):
        self.assertRaises(PlateauInputError,
                          self.mars_landing.create_plateau,
                          'a 5')

    def testCreateNormalRover(self):
        rover = self.mars_landing.create_rover('1 1 N', 'LRM', self.plateau)
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 1)
        self.assertEquals(rover.orientation, 'N')
        self.assertEquals(rover.commands, 'LRM')
        self.assertEquals(rover.plateau, self.plateau)

    def testBadPositionRover(self):
        rover = self.mars_landing.create_rover('1 1 A', 'LRM', self.plateau)
        self.assertIsNone(rover)

    def testInvalidPositionRover(self):
        rover = self.mars_landing.create_rover('6 6 N', 'LRM', self.plateau)
        self.assertIsNone(rover)

    def testBadCommandsRover(self):
        rover = self.mars_landing.create_rover('1 1 N', 'LRMA', self.plateau)
        self.assertIsNone(rover)

    def testEmptyInput(self):
        return NotImplemented

    def testMalformedInput(self):
        return NotImplemented

    def testSingleRoverSquad(self):
        return NotImplemented

    def testTwoRoverSquad(self):
        return NotImplemented

    def testMultiRoverSquad(self):
        return NotImplemented


def main():
    unittest.main()

if __name__ == '__main__':
    main()