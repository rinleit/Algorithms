Mars Rovers
===========

Usage:
1.  Extract contents of MarsRovers.zip
2.  From the command line, 'python3 MarsLanding.py <inputFileName>'
        'python3 MarsLanding.py input1' mirrors the example input provided
3.  To run the test suite, 'python3 RunTests.py'

Design Process:
    When designing my solution, I split the problem up into three sections: the main class, to handle input and output,
    a rover class that corresponded to a rover exploring a Mars plateau, and a plateau class, that would represent the
    grid upon which a rover would explore.

    Next, I designed the test cases. I created three test classes, to properly test each of the classes to be used in
    the solution. I thought up a base amount of tests that I could foresee.

    The plateau class was the simplest and first to be developed; it would contain two properties, x and y, which would
    correspond to the upper-right coordinate of the plateau. It would have a public method that would return whether a
    supplied coordinate is valid on that specific plateau. I would eventually write a private helper method to ensure
    that each axis of the coordinate is at least zero, but still on the plateau.

    The finalized test cases for Plateau are rather simple - ensure well-formed input results in a plateau, and to check
    the output from the is_valid_position method.

    I wrote the rover class next. A rover can explore a plateau, and always has a position and orientation, which
    mirrors the parameters required to initialize a new rover, as well as the set of commands that it will follow to
    explore the plateau.

    A rover, in exploring a plateau, can either spin or move. Spinning involves either changing the
    orientation to the left or right by 90 degrees. I was able to solve this problem by considering the string 'NESW'
    and realizing that a left turn would change the current orientation one back in that string array, or one forward
    when doing a right turn (assuming the array wraps around).

    When moving, a rover changes position by one unit based on it's orientation. If that new position is valid on the
    plateau it's exploring, it's position will be updated. Otherwise, a warning is printed to the output, and no change
    is made. Instead of throwing an error, I decided it would be better to allow the rover to continue on it's
    exploration so long as a warning was left for the user, in order for them to understand why the output may not be
    as expected. They could then change their input so their rover does not try to explore uncharted territory.

    The finalized test cases are straight forward for the rover class as well, with a number of tests written to check
    the initialization of the rover, as well it's functions to explore, spin and move, as well as the helper methods
    used to facilitate those actions.

    Finally, the class to tie all of this together, MarsLanding. It will ensure the minimum number of command line
    arguments (1) are specified, that the specified file exists and can be read, and finally, read the input file and
    try to create a plateau, the rovers intended to explore it, and to actually have them explore the plateau. If the
    plateau can not be created properly, the program will quit. Regex is used to validate the input format and type, as
    seen in the methods to create a plateau or rover. Zip is used to read two lines at once, as each rover should have
    two lines of input. For each rover that was initialized properly, it's called to explore, and the resulting location
    is printed out. If a rover is not initialized, a warning is outputted, and the method will continue on with the rest
    of the input.

    Testing for this class involved a few test cases for the processing of plateau and rover input, and the end-to-end
    execution of the program. Mock input files exist in the TestInput folder, and test a variety of scenarios that could
    be encountered during execution.

    InputErrors contain a collection of errors that can be encountered during execution, related to problems with the
    input in a specified file. Utils contains a a couple of methods that are generic enough to warrant it's own class.

    The MarsLanding and Rover classes both avoid print statements and instead call out.write(). This is aid
    unit testing, where the output can be intercepted and analyzed. For some methods, especially the main method of the
    MarsLanding class, this is the only valid form of testing as there aren't any other artifacts available, that aren't
    already tested in other tests. 'out' is defaulted to stdout, so program output will be available on the command
    line by default.
