from Plateau import *
from Rover import *
from InputErrors import *
from Utils import *
import re


class MarsLanding:
    """ Main class for Mars Rover solution.
    This program will read in an input file.
    The first line of the file will be the upper-right coordinates of the plateau.
    The rest of the input will pertain to a rover and it's instructions.
        The first line will be the rover's initial coordinates and orientation.
        The second line will be the instructions for that rover.
    The output will be each rover's final coordinates and orientation.
    """

    def process_input(self, input_file):
        f = open(input_file, 'r')
        try:
            # Read the first line and create the plateau for the rovers
            plateau_input = f.readline()
            plateau = self.process_plateau(plateau_input)

            # Read the rest of the lines
            remaining_lines = f.readlines()

            # Throw an error if it's obvious the rover input is malformed
            if len(remaining_lines) % 2:
                raise RoverSetupError

            for line1, line2 in zip(remaining_lines[::2], remaining_lines[1::2]):
                line1 = line1.strip()
                line2 = line2.strip()
                rover = self.create_rover(line1, line2, plateau)

                # Warn about improper rovers but continue with well-formatted ones
                if rover:
                    rover.explore()
                    print(rover.x, rover.y, rover.orientation)

        except InputError as e:
            print(e.msg)
        finally:
            # Close the file handler even if an error was thrown during execution
            f.close()

    def process_plateau(self, plateau_input):
        raw_plateau = re.match('^(\d \d)$', plateau_input)
        if raw_plateau:
            coordinates = raw_plateau.group().split()
            return Plateau(coordinates[0], coordinates[1])
        else:
            raise PlateauInputError

    def create_rover(self, start_position, commands, plateau):
        raw_position = re.match('^(\d \d [NESW])$', start_position)
        raw_commands = re.match('^[LRM]+$', commands)

        if raw_position and raw_commands:
            formatted_position = process_regex(raw_position)
            coordinates = convert_to_int_list(formatted_position[:2])

            if not plateau.is_valid_position(coordinates[0], coordinates[1]):
                print(RoverInvalidPositionError().warning(raw_position.group()))
            else:
                return Rover(formatted_position, raw_commands.group(), plateau)
        else:
            print(RoverSetupError().warning(start_position, commands))


if __name__ == '__main__':
    MarsLanding().process_input('input1')