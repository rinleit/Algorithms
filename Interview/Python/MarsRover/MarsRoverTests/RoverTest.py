import unittest
import Plateau
import Rover


class RoverTest(unittest.TestCase):

    plateau = Plateau.Plateau(5, 5)

    def testCreateNormalRover(self):
        rover = Rover.Rover(1, 2, 'N', 'L', self.plateau)
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'N')
        self.assertEqual(rover.commands, 'L')
        self.assertEqual(rover.plateau, self.plateau)

    def testCreateRoverInvalidCoordinates(self):
        self.assertRaises(ValueError, Rover.Rover, 'a', 2, 'N', 'L', self.plateau)

    def testSetNormalOrientation(self):
        rover = Rover.Rover(1, 2, 'N', 'R', self.plateau)
        self.assertEqual(rover.orientation, 'N')
        rover.set_orientation('R', 1)
        self.assertEqual(rover.orientation, 'E')

    def testSetNegativeOrientation(self):
        rover = Rover.Rover(1, 2, 'N', 'R', self.plateau)
        self.assertEqual(rover.orientation, 'N')
        rover.set_orientation('R', -1)
        self.assertEqual(rover.orientation, 'N')

    def testNormalLeftSpin(self):
        rover = Rover.Rover(1, 2, 'E', 'L', self.plateau)
        self.assertEqual(rover.orientation, 'E')
        rover.spin('L')
        self.assertEqual(rover.orientation, 'N')

    def testNormalRightSpin(self):
        rover = Rover.Rover(1, 2, 'S', 'R', self.plateau)
        self.assertEqual(rover.orientation, 'S')
        rover.spin('R')
        self.assertEqual(rover.orientation, 'W')

    def testEdgeLeftSpin(self):
        rover = Rover.Rover(1, 2, 'N', 'L', self.plateau)
        self.assertEqual(rover.orientation, 'N')
        rover.spin('L')
        self.assertEqual(rover.orientation, 'W')

    def testEdgeRightSpin(self):
        rover = Rover.Rover(1, 2, 'W', 'R', self.plateau)
        self.assertEqual(rover.orientation, 'W')
        rover.spin('R')
        self.assertEqual(rover.orientation, 'N')

    def testNormalMove(self):
        rover = Rover.Rover(1, 2, 'E', 'M', self.plateau)
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'E')
        rover.move()
        self.assertEqual(rover.x, 2)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'E')

    def testEdgeMove(self):
        rover = Rover.Rover(4, 4, 'E', 'M', self.plateau)
        self.assertEqual(rover.x, 4)
        self.assertEqual(rover.y, 4)
        self.assertEqual(rover.orientation, 'E')
        rover.move()
        self.assertEqual(rover.x, 5)
        self.assertEqual(rover.y, 4)
        self.assertEqual(rover.orientation, 'E')

    def testIllegalMove(self):
        rover = Rover.Rover(5, 5, 'E', 'M', self.plateau)
        self.assertEqual(rover.x, 5)
        self.assertEqual(rover.y, 5)
        self.assertEqual(rover.orientation, 'E')
        rover.move()
        self.assertEqual(rover.x, 5)
        self.assertEqual(rover.y, 5)
        self.assertEqual(rover.orientation, 'E')

    def testLeftSpinCommand(self):
        rover = Rover.Rover(5, 5, 'E', 'L', self.plateau)
        self.assertEqual(rover.orientation, 'E')
        rover.command('L')
        self.assertEqual(rover.orientation, 'N')

    def testRightSpinCommand(self):
        rover = Rover.Rover(5, 5, 'E', 'R', self.plateau)
        self.assertEqual(rover.orientation, 'E')
        rover.command('R')
        self.assertEqual(rover.orientation, 'S')

    def testMoveSpinCommand(self):
        rover = Rover.Rover(1, 2, 'E', 'M', self.plateau)
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'E')
        rover.command('M')
        self.assertEqual(rover.x, 2)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'E')

    def testIllegalCommand(self):
        rover = Rover.Rover(1, 2, 'E', 'M', self.plateau)
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'E')
        rover.command('a')
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'E')

    def testEmptyCommandExplore(self):
        rover = Rover.Rover(1, 2, 'E', '', self.plateau)
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'E')
        rover.explore()
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'E')

    def testSingleCommandExplore(self):
        rover = Rover.Rover(1, 2, 'E', 'L', self.plateau)
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'E')
        rover.explore()
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'N')

    def testTwoCommandExplore(self):
        rover = Rover.Rover(1, 2, 'E', 'LM', self.plateau)
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'E')
        rover.explore()
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 3)
        self.assertEqual(rover.orientation, 'N')

    def testExample1Explore(self):
        rover = Rover.Rover(1, 2, 'N', 'LMLMLMLMM', self.plateau)
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 2)
        self.assertEqual(rover.orientation, 'N')
        rover.explore()
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 3)
        self.assertEqual(rover.orientation, 'N')

    def testExample2Explore(self):
        rover = Rover.Rover(3, 3, 'E', 'MMRMMRMRRM', self.plateau)
        self.assertEqual(rover.x, 3)
        self.assertEqual(rover.y, 3)
        self.assertEqual(rover.orientation, 'E')
        rover.explore()
        self.assertEqual(rover.x, 5)
        self.assertEqual(rover.y, 1)
        self.assertEqual(rover.orientation, 'E')


def main():
    unittest.main()

if __name__ == '__main__':
    main()