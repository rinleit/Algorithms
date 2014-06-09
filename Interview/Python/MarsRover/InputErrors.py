class InputError(Exception):
    def __init__(self):
        """
        An Exception when encountering input that does not match the expected format
        :return: A new instance of an InputError
        """
        self.msg = "Generic input error."


class PlateauInputError(InputError):
    def __init__(self):
        """
        An InputError that is thrown when a Plateau input does not match the expected format
        :return: A new instance of PlateauInputError
        """
        self.msg = "Malformed grid initialization input. The first line be of the format X Y, " \
                   "where X and Y are two integers."


class RoverSetupError(InputError):
    def __init__(self):
        """
        An InputError that is thrown when a Rover's input does not match the expected format
        :return: A new instance of RoverSetupError
        """
        self.msg = "Malformed rover setup input. Each rover should have two corresponding lines," \
                   "the first of the format X Y Z, where X and Y are integers indicating their starting co-ordinate" \
                   "and Z is N E S or W to indiate it's initial orientation. " \
                   "The second should contain a series of characters that are either L R or M to indicate it's " \
                   "movement path on the plateau."

    def warning(self, raw_position, raw_commands):
        """
        Return a String that warns the user of an invalid rover input
        :param raw_position: Input String for a rover's initial position
        :param raw_commands: Input String for a rover's commands
        :return: A String that warns a user that the specified rover initialization and commands are invalid
        """
        return "WARNING: Could not create rover for initial position '%s' with commands '%s'; " \
               "did not meet required formatting standards.\n" % (raw_position, raw_commands)


class RoverInvalidPositionError(InputError):
    def __init__(self):
        """
        An InputError that is thrown when a Rover's initial position is invalid
        :return: A new instance of RoverInvalidPositionError
        """
        self.msg = "Malformed rover initialization. Please ensure that each rover is on the plateau to start."

    def warning(self, raw_input):
        """
        Return a String that warns a user one of their rover's is invalid due to it's initial position
        :param raw_input: Input String for a rover's inital position
        :return: A String that warns the user that a rover is invalid as it's initial position is off the Plateau
        """
        return "WARNING: Could not create rover for input '%s'; rover is not on the plateau.\n" % raw_input