import unittest
import Plateau
import Rover


class RoverTest(unittest.TestCase):

    plateau = Plateau.Plateau(5, 5)

    def testCreateNormalRover(self):
        rover = Rover.Rover(1, 2, 'N', 'L', self.plateau)
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'N')
        self.assertEquals(rover.commands, 'L')
        self.assertEquals(rover.plateau, self.plateau)

    def testCreateRoverInvalidCoordinates(self):
        self.assertRaises(ValueError, Rover.Rover, 'a', 2, 'N', 'L', self.plateau)

    def testSetNormalOrientation(self):
        rover = Rover.Rover(1, 2, 'N', 'R', self.plateau)
        self.assertEquals(rover.orientation, 'N')
        rover.set_orientation('R', 1)
        self.assertEquals(rover.orientation, 'E')

    def testSetNegativeOrientation(self):
        rover = Rover.Rover(1, 2, 'N', 'R', self.plateau)
        self.assertEquals(rover.orientation, 'N')
        rover.set_orientation('R', -1)
        self.assertEquals(rover.orientation, 'N')

    def testNormalLeftSpin(self):
        rover = Rover.Rover(1, 2, 'E', 'L', self.plateau)
        self.assertEquals(rover.orientation, 'E')
        rover.spin('L')
        self.assertEquals(rover.orientation, 'N')

    def testNormalRightSpin(self):
        rover = Rover.Rover(1, 2, 'S', 'R', self.plateau)
        self.assertEquals(rover.orientation, 'S')
        rover.spin('R')
        self.assertEquals(rover.orientation, 'W')

    def testEdgeLeftSpin(self):
        rover = Rover.Rover(1, 2, 'N', 'L', self.plateau)
        self.assertEquals(rover.orientation, 'N')
        rover.spin('L')
        self.assertEquals(rover.orientation, 'W')

    def testEdgeRightSpin(self):
        rover = Rover.Rover(1, 2, 'W', 'R', self.plateau)
        self.assertEquals(rover.orientation, 'W')
        rover.spin('R')
        self.assertEquals(rover.orientation, 'N')

    def testNormalMove(self):
        rover = Rover.Rover(1, 2, 'E', 'M', self.plateau)
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'E')
        rover.move()
        self.assertEquals(rover.x, 2)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'E')

    def testEdgeMove(self):
        rover = Rover.Rover(4, 4, 'E', 'M', self.plateau)
        self.assertEquals(rover.x, 4)
        self.assertEquals(rover.y, 4)
        self.assertEquals(rover.orientation, 'E')
        rover.move()
        self.assertEquals(rover.x, 5)
        self.assertEquals(rover.y, 4)
        self.assertEquals(rover.orientation, 'E')

    def testIllegalMove(self):
        rover = Rover.Rover(5, 5, 'E', 'M', self.plateau)
        self.assertEquals(rover.x, 5)
        self.assertEquals(rover.y, 5)
        self.assertEquals(rover.orientation, 'E')
        rover.move()
        self.assertEquals(rover.x, 5)
        self.assertEquals(rover.y, 5)
        self.assertEquals(rover.orientation, 'E')

    def testLeftSpinCommand(self):
        rover = Rover.Rover(5, 5, 'E', 'L', self.plateau)
        self.assertEquals(rover.orientation, 'E')
        rover.command('L')
        self.assertEquals(rover.orientation, 'N')

    def testRightSpinCommand(self):
        rover = Rover.Rover(5, 5, 'E', 'R', self.plateau)
        self.assertEquals(rover.orientation, 'E')
        rover.command('R')
        self.assertEquals(rover.orientation, 'S')

    def testMoveSpinCommand(self):
        rover = Rover.Rover(1, 2, 'E', 'M', self.plateau)
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'E')
        rover.command('M')
        self.assertEquals(rover.x, 2)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'E')

    def testIllegalCommand(self):
        rover = Rover.Rover(1, 2, 'E', 'M', self.plateau)
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'E')
        rover.command('a')
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'E')

    def testEmptyCommandExplore(self):
        rover = Rover.Rover(1, 2, 'E', '', self.plateau)
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'E')
        rover.explore()
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'E')

    def testSingleCommandExplore(self):
        rover = Rover.Rover(1, 2, 'E', 'L', self.plateau)
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'E')
        rover.explore()
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'N')

    def testTwoCommandExplore(self):
        rover = Rover.Rover(1, 2, 'E', 'LM', self.plateau)
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'E')
        rover.explore()
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 3)
        self.assertEquals(rover.orientation, 'N')

    def testExample1Explore(self):
        rover = Rover.Rover(1, 2, 'N', 'LMLMLMLMM', self.plateau)
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 2)
        self.assertEquals(rover.orientation, 'N')
        rover.explore()
        self.assertEquals(rover.x, 1)
        self.assertEquals(rover.y, 3)
        self.assertEquals(rover.orientation, 'N')

    def testExample2Explore(self):
        rover = Rover.Rover(3, 3, 'E', 'MMRMMRMRRM', self.plateau)
        self.assertEquals(rover.x, 3)
        self.assertEquals(rover.y, 3)
        self.assertEquals(rover.orientation, 'E')
        rover.explore()
        self.assertEquals(rover.x, 5)
        self.assertEquals(rover.y, 1)
        self.assertEquals(rover.orientation, 'E')


def main():
    unittest.main()

if __name__ == '__main__':
    main()