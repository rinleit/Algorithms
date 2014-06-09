import re
from Plateau import *
from Rover import *
from InputErrors import *
from Utils import *


class MarsLanding:
    """
    Main class for Mars Rover solution.
    This program will read in an input file.
    The first line of the file will be the upper-right coordinates of the plateau.
    The rest of the input will pertain to a rover and it's instructions.
        The first line will be the rover's initial coordinates and orientation.
        The second line will be the instructions for that rover.
    The output will be each rover's final coordinates and orientation.
    """
    def __init__(self):
        """
        Create a new instance of the MarsLanding class
        :return: A new instance of MarsLanding
        """
        self

    def process_input(self, input_file, out=sys.stdout):
        """
        Process a file for a Mars Landing expedition. Errors and warnings will be printed to a provided output stream,
        as well as the final position of each Rover.
        :param input_file: A String representing the filename that contains the Plateau and Rover information. The
                file should exist in the directory that the program is run from
        :param out: Output stream for messages during execution
        :return: None
        """
        try:
            f = open(input_file, 'r')
        except FileNotFoundError:
            out.write("ERROR: File '%s' does not exist\n" % input_file)
            return

        try:
            # Read the first line and create the plateau for the rovers
            plateau_input = f.readline()
            plateau = self.create_plateau(plateau_input)

            # Read the rest of the lines
            remaining_lines = f.readlines()

            # Throw an error if it's obvious the rover input is malformed
            if len(remaining_lines) % 2:
                raise RoverSetupError

            for line1, line2 in zip(remaining_lines[::2], remaining_lines[1::2]):
                line1 = line1.strip()
                line2 = line2.strip()
                rover = self.create_rover(line1, line2, plateau, out)

                # Warn about improper rovers but continue with well-formatted ones
                if rover:
                    rover.explore(out)
                    out.write("%s %s %s\n" % (rover.x, rover.y, rover.orientation))

        except InputError as e:
            out.write(e.msg + "\n")
        finally:
            # Close the file handler even if an error was thrown during execution
            f.close()

    @staticmethod
    def create_plateau(plateau_input):
        """
        Return a new Plateau, or a PlateauInputError if a problem was found with the input
        :param plateau_input: String representing a new Plateau. Valid plateau_input will be two Integers separated by
                a space
        :return: Plateau if no errors were found with the input, otherwise a PlateauInputError
        """
        raw_plateau = re.match('^(\d \d)$', plateau_input)
        if raw_plateau:
            coordinates = raw_plateau.group().split()
            return Plateau(coordinates[0], coordinates[1])
        else:
            raise PlateauInputError

    @staticmethod
    def create_rover(start_position, commands, plateau, out=sys.stdout):
        """
        Return a new Rover if it has a valid initial position and set of commands, otherwise nothing will be returned
        :param start_position: String representing a rover's initial position. Valid start_positions will have two
                Integers followed by a space and either N, E, S or W
        :param commands: String representing a rover's set of instructions. Valid characters in commands are either
                L, R or M
        :param plateau: the Plateau that the Rover will explore
        :param out: Output stream for messages during execution
        :return: Rover if no errors were found in the input, otherwise None
        """
        raw_position = re.match('^(\d \d [NESW])$', start_position)
        raw_commands = re.match('^[LRM]+$', commands)

        if raw_position and raw_commands:
            formatted_position = process_regex(raw_position)
            coordinates = convert_to_int_list(formatted_position[:2])

            if not plateau.is_valid_position(coordinates[0], coordinates[1]):
                out.write(RoverInvalidPositionError().warning(raw_position.group()))
            else:
                return Rover(coordinates[0], coordinates[1], formatted_position[2], raw_commands.group(), plateau)
        else:
            out.write(RoverSetupError().warning(start_position, commands))


if __name__ == '__main__':
    if len(sys.argv[1:]) < 1:
        print("ERROR: Please supply an input file name")
    else:
        MarsLanding().process_input(sys.argv[1])