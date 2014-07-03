import sys


class Rover:
    """
    Class that represents a Rover
    A Rover has a Plateau that it will explore via a set of commands. It always has an x and y coordinate and
    orientation that corresponds to it's current position on the Plateau.
    A Rover is able to spin left or right, or move one unit forward based on it's orientation.
    """
    def __init__(self, x, y, orientation, commands, plateau):
        """
        Return a rover that will explore a Plateau
        :param x: Integer that represents the initial x coordinate of the new rover
        :param y: Integer that represents the initial y coordinate of the new rover
        :param orientation: Character the represents the initial orientation of the new rover. Valid orientations are
                N, E, S or W
        :param commands: String of characters that represents the instructions the rover will execute. Valid commands
                are L, R or M.
        :param plateau: Plateau that the rover will explore
        :return: A new instance of a Rover
        """
        self.x = int(x)
        self.y = int(y)
        self.orientation = orientation
        self.commands = commands
        self.plateau = plateau
        self.directions = 'NESW'

    def explore(self, out=sys.stdout):
        """
        Execute a rover's set of commands
        :param out: Output stream for messages during execution
        :return: None
        """
        for char in self.commands:
            self.command(char, out)

    def command(self, instruction, out=sys.stdout):
        """
        Execute a single command for a rover
        :param instruction: Character representing a rover's instruction. Valid instructions are L, R and M
        :param out: Output stream for messages during execution
        :return: None
        """
        instruction = instruction.upper()
        if instruction == 'L' or instruction == 'R':
            self.spin(instruction, out)
        elif instruction == 'M':
            self.move(out)
        else:
            # We shouldn't be here because of regex, but just in case
            out.write("WARNING: Unrecognized rover instruction\n")

    def spin(self, direction, out=sys.stdout):
        """
        Change the orientation of a rover by spinning either left or right
        :param direction: Character representing the direction a rover should spin. Valid directions are L or R
        :param out: Output stream for messages during execution
        :return: None
        """
        directions = 'NESW'
        if direction == 'L':
            new_direction = directions.find(self.orientation) - 1
            if new_direction == -1:
                # Wrap-around; if spinning left from N, new direction should be W
                new_direction = 3

            self.set_orientation(direction, new_direction, out)
        elif direction == 'R':
            new_direction = directions.find(self.orientation) + 1
            if new_direction == 4:
                # Wrap-around; if spinning right from W, new direction should be N
                new_direction = 0

            self.set_orientation(direction, new_direction, out)
        else:
            # We shouldn't be here because of regex, but just in case
            out.write("WARNING: Unrecognized rover spin direction\n")

    def set_orientation(self, direction, new_direction, out=sys.stdout):
        """
        Helper method for spin(). Set the rover's orientation to it's new heading
        :param direction: Character representing the direction a rover should spin. Valid directions are L or R
        :param new_direction: Integer between 0 and 3 that represents the index in 'NESW' that the rover's orientation
                should be changed to
        :param out: Output stream for messages during execution
        :return: None
        """
        directions = 'NESW'
        if new_direction >= 0:
            self.orientation = directions[new_direction]
        else:
            out.write("WARNING: Invalid orientation. Ignoring instruction to spin %s from %s.\n"
                      % (direction, self.orientation))

    def move(self, out=sys.stdout):
        """
        Change a rover's position by one unit based on it's orientation. If facing north, a rover will move up one on
        the y-axis, and move down one on the y-axis if facing south. If facing east, it will move up one on the x-axis,
        and down one if facing west
        :param out: Output stream for messages during execution
        :return: None
        """

        
        # Alternate solution avoid big if block. Change can_move to set rover position itself.
        # moves = {}
        # moves['N'] = self.x, self.y +1

        # if self.orienientation not in moves:
        #         can_move(moves[self.orientation])


        if self.orientation == 'N':
            if self.can_move(self.x, self.y + 1, out):
                self.y += 1
        elif self.orientation == 'S':
            if self.can_move(self.x, self.y - 1, out):
                self.y -= 1
        elif self.orientation == 'E':
            if self.can_move(self.x + 1, self.y, out):
                self.x += 1
        elif self.orientation == 'W':
            if self.can_move(self.x - 1, self.y, out):
                self.x -= 1
        else:
            # We shouldn't be here because of regex, but just in case
            out.write("WARNING: Unrecognized rover orientation\n")



    def can_move(self, x, y, out=sys.stdout):
        """
        Return a Boolean that corresponds to whether the x, y coordinates is a valid position on the Plateau
        :param x: Integer representing an x-coordinate
        :param y: Integer representing a y-coordinate
        :param out: Output stream for messages during execution
        :return: True if the coordinate exist on the Plateau, False otherwise
        """
        if self.plateau.is_valid_position(x, y):
            return True
        else:
            out.write("WARNING: Illegal to move to coordinate %s %s. Move command ignored.\n" % (x, y))
            return False