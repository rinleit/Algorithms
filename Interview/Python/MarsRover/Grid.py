class Grid:

    def __init__(self, upper_limit_x, upper_limit_y):
        self.upper_limit = (upper_limit_x, upper_limit_y)

    def position(self):
        return NotImplemented