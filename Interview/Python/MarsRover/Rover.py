class Rover:

    def __init__(self, start_position, commands, plateau):
        self.x = int(start_position[0])
        self.y = int(start_position[1])
        self.orientation = start_position[2]
        self.commands = commands
        self.plateau = plateau

    def explore(self):
        for char in self.commands:
            self.command(char)

    def command(self, instruction):
        instruction = instruction.upper()
        if instruction == 'L' or instruction == 'R':
            self.spin(instruction)
        elif instruction == 'M':
            self.move()
        else:
            # We shouldn't be here because of regex, but just in case
            print("WARNING: Unrecognized rover instruction")

    def spin(self, direction):
        directions = 'NESW'
        if direction == 'L':
            new_direction = directions.find(self.orientation) - 1
            if new_direction == -1:
                # Wrap-around; if spinning left from N, new direction should be W
                new_direction = 3

            self.set_orientation(direction, new_direction)
        elif direction == 'R':
            new_direction = directions.find(self.orientation) + 1
            if new_direction == 4:
                # Wrap-around; if spinning right from W, new direction should be N
                new_direction = 0

            self.set_orientation(direction, new_direction)
        else:
            # We shouldn't be here because of regex, but just in case
            print("WARNING: Unrecognized rover spin direction")

    def set_orientation(self, direction, new_direction):
        directions = 'NESW'
        if new_direction >= 0:
            self.orientation = directions[new_direction]
        else:
            print("WARNING: Invalid orientation. Ignoring instruction to spin %s from %s." % (direction, self.orientation))

    def move(self):
        if self.orientation == 'N':
            if self.plateau.is_valid_position(self.x, self.y + 1):
                self.y += 1
        elif self.orientation == 'S':
            if self.plateau.is_valid_position(self.x, self.y - 1):
                self.y -= 1
        elif self.orientation == 'E':
            if self.plateau.is_valid_position(self.x + 1, self.y):
                self.x += 1
        elif self.orientation == 'W':
            if self.plateau.is_valid_position(self.x - 1, self.y):
                self.x -= 1
        else:
            # We shouldn't be here because of regex, but just in case
            print("WARNING: Unrecognized rover orientation")

if __name__ == '__main__':
    import Plateau
    rover = Rover(['1', '2', 'N'], 'LMLMLMLMM', Plateau.Plateau([5, 5]))
    rover.explore()