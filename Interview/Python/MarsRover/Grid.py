class Grid:

    def __init__(self, upper_limit_x, upper_limit_y):
        self.upper_x_limit = upper_limit_x
        self.upper_y_limit = upper_limit_y

    def position(self):
        return NotImplemented

    def is_valid_position(self, x, y):
        return self.upper_x_limit >= x or self.upper_y_limit >= y