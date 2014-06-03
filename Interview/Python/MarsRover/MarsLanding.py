import Grid
from InputErrors import *


class MarsLanding:
    """ Main class for Mars Rover solution.
    This program will read in an input file.
    The first line of the file will be the upper-right coordinates of the plateau.
    The rest of the input will pertain to a rover and it's instructions.
        The first line will be the rover's initial coordinates and heading.
        The second line will be the instructions for that rover.
    The output will be each rover's final coordinates and heading.
    """

    def __init__(self):
        self

    def process_input(self, input_file):
        f = open(input_file, 'r')
        try:
            grid_input = f.readline().split()
            grid = self.process_grid(grid_input)

            remaining_lines = f.readlines()
            if len(remaining_lines) % 2:
                raise RoverInputLengthError
            rovers = []
            for line1, line2 in zip(remaining_lines[::2], remaining_lines[1::2]):
                line1 = line1.strip()
                line2 = line2.strip()
                self.create_rover(line1, line2)

        except (InitInputLengthError, InitInputTypeError, RoverInputLengthError) as e:
            print e.msg
        finally:
            f.close()

    def process_grid(self, grid_input):
        if len(grid_input) != 2:
            raise InitInputLengthError
        else:
            try:
                upper_cords = map(int, grid_input)
                return Grid.Grid(upper_cords[0], upper_cords[1])
            except ValueError:
                raise InitInputTypeError

    def create_rover(self, inital_position, commands):
        pass


if __name__ == '__main__':
    landing = MarsLanding()
    landing.process_input('input1')