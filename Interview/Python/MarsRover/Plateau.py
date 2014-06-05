class Plateau:

    def __init__(self, upper_limits):
        self.upper_x_limit = upper_limits[0]
        self.upper_y_limit = upper_limits[1]

    def is_valid_position(self, coords):
        return self.upper_x_limit >= coords[0] and self.upper_y_limit >= coords[1]