class InputError(Exception):
    def __init__(self):
        self.msg = "Generic input error."


class InitInputLengthError(InputError):
    def __init__(self):
        self.msg = "Malformed grid initialization input. Please input exactly two integers on the first line, " \
                   "in order to determine the size of the plateau."


class InitInputTypeError(InputError):
    def __init__(self):
        self.msg = "Malformed grid initialization input. Please ensure the first line contains two integers, " \
                   "to specify the size of the plateau."


class RoverSetupError(InputError):
    def __init__(self):
        self.msg = "Malformed rover setup input. Please ensure that for each rover, " \
                   "it's starting position and heading is specified on one line, " \
                   "and it's instructions on the line directly proceeding that."


class RoverInitLengthError(InputError):
    def __init__(self):
        self.msg = "Malformed rover initialization. Please ensure that the first line of each rover is " \
                   "of the format X Y Z, where X and Y are integers that indicate the starting co-ordinate, " \
                   "and Z is N E S or W to indicate it's initial heading."


class RoverInvalidPositionError(InputError):
    def __init__(self):
        self.msg = "Malformed rover initialization. Please ensure that each rover is on the plateau to start."