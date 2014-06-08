import unittest
import os
import MarsLanding
import Plateau
from InputErrors import *
from io import StringIO


class MarsLandingTest(unittest.TestCase):

    suffix = '' if os.getcwd().split('/')[-1] == 'MarsRoverTests' else 'MarsRoverTests/'
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
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 1)
        self.assertEqual(rover.orientation, 'N')
        self.assertEqual(rover.commands, 'LRM')
        self.assertEqual(rover.plateau, self.plateau)

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
        self.__marsLandingOutputHelper(self.suffix + 'TestInput/emptyInput', PlateauInputError().msg)

    def testMalformedPlateauInput(self):
        self.__marsLandingOutputHelper(self.suffix + 'TestInput/badPlateauInput', PlateauInputError().msg)

    def testMalformedRoverPositionInput(self):
        self.__marsLandingOutputHelper(self.suffix + 'TestInput/badRoverPositionInput',
                                       "WARNING: Could not create rover for input '1 6 N'; "
                                       "rover is not on the plateau.")

    def testMalformedRoverOrientationInput(self):
        self.__marsLandingOutputHelper(self.suffix + 'TestInput/badRoverOrientationInput',
                                       "WARNING: Could not create rover for initial position '1 2 A' with "
                                       "commands 'LMLMLMLMM'; did not meet required formatting standards.")

    def testMalformedRoverCommandInput(self):
        self.__marsLandingOutputHelper(self.suffix + 'TestInput/badRoverCommandInput',
                                       "WARNING: Could not create rover for initial position '1 2 N' with commands "
                                       "'LMLMLMLMMA'; did not meet required formatting standards.")

    def testNoRoversInput(self):
        self.__marsLandingOutputHelper(self.suffix + 'TestInput/noRoverInput', '')

    def testSingleRoverSquad(self):
        self.__marsLandingOutputHelper(self.suffix + 'TestInput/singleRoverInput',
                                       "1 3 N")

    def testTwoRoverSquad(self):
        self.__marsLandingOutputHelper(self.suffix + 'TestInput/twoRoverInput',
                                       "1 3 N\n5 1 E")

    def testMultiRoverSquad(self):
        self.__marsLandingOutputHelper(self.suffix + 'TestInput/multiRoverInput',
                                       "1 3 N\n5 1 E\n4 0 S")

    def __marsLandingOutputHelper(self, filename, output_message):
        out = StringIO()
        print(out.getvalue())
        self.mars_landing.process_input(filename, out)
        output = out.getvalue().strip()
        self.assertEqual(output, output_message)



def main():
    unittest.main()

if __name__ == '__main__':
    main()