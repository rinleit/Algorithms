import sys

class Rover:

    def __init__(self, x, y, orientation, commands, plateau):
        self.x = int(x)
        self.y = int(y)
        self.orientation = orientation
        self.commands = commands
        self.plateau = plateau

    def explore(self, out=sys.stdout):
        for char in self.commands:
            self.command(char, out)

    def command(self, instruction, out=sys.stdout):
        instruction = instruction.upper()
        if instruction == 'L' or instruction == 'R':
            self.spin(instruction, out)
        elif instruction == 'M':
            self.move(out)
        else:
            # We shouldn't be here because of regex, but just in case
            out.write("WARNING: Unrecognized rover instruction\n")

    def spin(self, direction, out=sys.stdout):
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
        directions = 'NESW'
        if new_direction >= 0:
            self.orientation = directions[new_direction]
        else:
            out.write("WARNING: Invalid orientation. Ignoring instruction to spin %s from %s.\n"
                      % (direction, self.orientation))

    def move(self, out=sys.stdout):
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
        if self.plateau.is_valid_position(x, y):
            return True
        else:
            out.write("WARNING: Illegal to move to coordinate %s %s. Move command ignored.\n" % (x, y))
            return False

if __name__ == '__main__':
    import Plateau
    rover = Rover(['1', '2', 'N'], 'LMLMLMLMM', Plateau.Plateau([5, 5]))
    rover.explore()