class Plateau:

    def __init__(self, x, y):
        self.max_x = int(x)
        self.max_y = int(y)

    def is_valid_position(self, x, y):
        return self.max_x >= x and self.max_y >= y