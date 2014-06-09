class Plateau:
    """
    A class that represents a Plateau
    A Plateau is a grid, with it's origin at (0,0), and a specified upper right coordinate.
    """

    def __init__(self, x, y):
        """
        Return a Plateau
        :param x: Upper right x-coordinate of the Plateau
        :param y: Upper right y-coordinate of the Plateau
        :return: A new instance of a Plateau
        """
        self.max_x = int(x)
        self.max_y = int(y)

    def is_valid_position(self, x, y):
        """
        Return a Boolean that corresponds to whether the x, y pair exists on the Plateau
        :param x: Integer representing the x coordinate
        :param y: Integer representing the y coordinate
        :return: True if the coordinate lies on the Plateau, False otherwise
        """
        return self.__is_valid_coordinate(self.max_x, x) and \
               self.__is_valid_coordinate(self.max_y, y)

    @staticmethod
    def __is_valid_coordinate(max_coordinate, coordinate):
        """
        Helper method for is_valid_position(). Ensures a coordinate is between 0 and a maximum.
        :param max_coordinate: Integer upper limit of the coordinate
        :param coordinate: Integer coordinate for evaluation
        :return: True if coordinate is between 0 and max_coordinate, False otherwise
        """
        return 0 <= coordinate <= max_coordinate