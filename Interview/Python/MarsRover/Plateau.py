class Plateau:

    def __init__(self, x, y):
        self.max_x = int(x)
        self.max_y = int(y)

    def is_valid_position(self, x, y):
        return self.__is_valid_coordinate(self.max_x, x) and \
               self.__is_valid_coordinate(self.max_y, y)

    @staticmethod
    def __is_valid_coordinate(max_coordinate, coordinate):
        return 0 <= coordinate <= max_coordinate