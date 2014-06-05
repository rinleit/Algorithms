from Plateau import *
from Rover import *
from InputErrors import *
import re


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
            plateau_input = f.readline()
            plateau = self.process_plateau(plateau_input)

            remaining_lines = f.readlines()
            if len(remaining_lines) % 2:
                raise RoverSetupError
            rovers = []
            for line1, line2 in zip(remaining_lines[::2], remaining_lines[1::2]):
                line1 = line1.strip()
                line2 = line2.strip()
                rover = self.create_rover(line1, line2, plateau)
                if rover:
                    rovers.append(rover)
        except InputError as e:
            print(e.msg)
        finally:
            f.close()

    def process_plateau(self, plateau_input):
        raw_plateau = re.match('^(\d \d)$', plateau_input)
        if raw_plateau:
            return Plateau(raw_plateau.group().split())
        else:
            raise PlateauInputError

    def create_rover(self, start_position, commands, plateau):
        raw_position = re.match('^(\d \d [NESW])$', start_position)
        raw_commands = re.match('^[LRM]+$', commands)
        if raw_position and raw_commands:
            formatted_position = raw_position.group().split()
            if not plateau.is_valid_position(formatted_position):
                print(RoverInvalidPositionError().warning(raw_position.group()))
            else:
                return Rover(formatted_position)


if __name__ == '__main__':
    landing = MarsLanding()
    landing.process_input('input1')