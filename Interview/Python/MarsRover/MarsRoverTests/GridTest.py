import unittest


class GridTest(unittest.TestCase):

    def new_grid(self):
        return NotImplemented

    def bad_grid(self):
        return NotImplemented

    def where_am_i(self):
        return NotImplemented


def main():
    unittest.main()

if __name__ == '__main__':
    main()