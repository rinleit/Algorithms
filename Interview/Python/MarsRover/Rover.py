class Rover:

    def __init__(self, rover_input):
        self.position = rover_input[0:2]
        self.heading = rover_input[2]

    def move(self):
        return NotImplemented