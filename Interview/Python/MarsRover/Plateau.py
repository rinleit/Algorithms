class Plateau:

    def __init__(self, x, y):
        self.max_x = int(x)
        self.max_y = int(y)

    def is_valid_position(self, x, y):
        return self.is_valid_coordinate(self.max_x, x) and \
               self.is_valid_coordinate(self.max_y, y)

    def is_valid_coordinate(self, max_coordinate, coordinate):
        return 0 <= coordinate <= max_coordinate