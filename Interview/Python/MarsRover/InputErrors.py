class InputError(Exception):
    def __init__(self):
        self.msg = "Generic input error."


class PlateauInputError(InputError):
    def __init__(self):
        self.msg = "Malformed grid initialization input. The first line be of the format X Y, " \
                   "where X and Y are two integers."


class RoverSetupError(InputError):
    def __init__(self):
        self.msg = "Malformed rover setup input. Each rover should have two corresponding lines," \
                   "the first of the format X Y Z, where X and Y are integers indicating their starting co-ordinate" \
                   "and Z is N E S or W to indiate it's initial orientation. " \
                   "The second should contain a series of characters that are either L R or M to indicate it's " \
                   "movement path on the plateau"

    def warning(self, raw_position, raw_commands):
        return "WARNING: Could not create rover for initial position '%s' with commands '%s'; " \
               "did not meet required formatting standards." % (raw_position, raw_commands)


class RoverInvalidPositionError(InputError):
    def __init__(self):
        self.msg = "Malformed rover initialization. Please ensure that each rover is on the plateau to start."

    def warning(self, raw_input):
        return "WARNING: Could not create rover for input '%s'; rover is not on the plateau." % raw_input