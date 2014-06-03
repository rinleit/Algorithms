class InitInputLengthError(Exception):
    def __init__(self):
        self.msg = "Malformed grid initialization input. Please input exactly two integers on the first line, " \
                   "in order to determine the size of the plateau."


class InitInputTypeError(Exception):
    def __init__(self):
        self.msg = "Malformed grid initialization input. Please ensure the first line contains two integers, " \
                   "to specify the size of the plateau."


class RoverInputLengthError(Exception):
    def __init__(self):
        self.msg = "Malformed rover setup input. Please ensure that for each rover, " \
                   "it's starting position and heading is specified on one line, " \
                   "and it's instructions on the line directly proceeding that."__author__ = 'dweber'
