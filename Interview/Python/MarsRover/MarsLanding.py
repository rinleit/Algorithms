class MarsLanding:
    """ Main class for Mars Rover solution.
    This program will read in an input file.
    The first line of the file will be the upper-right coordinates of the plateau.
    The rest of the input will pertain to a rover and it's instructions.
        The first line will be the rover's initial coordinates and heading.
        The second line will be the instructions for that rover.
    The output will be each rover's final coordinates and heading.
    """

    def __init__(self):
        self

    def process_input(self):
        f = open('input1', 'r')
        try:
            upper_corner = f.readline().split()
            if len(upper_corner) != 2:
                return "Malformed input. First line should be of the format X Y, where X and Y are integers."
            else:
                try:
                    upper_cords = map(int, upper_corner)
                except ValueError:
                    return "Malformed input. First line should be of the format X Y, where X and Y are integers."
                for coord in upper_cords:
                    print(coord)
        finally:
            f.close()

if __name__ == '__main__':
    landing = MarsLanding()
    print(landing.process_input())