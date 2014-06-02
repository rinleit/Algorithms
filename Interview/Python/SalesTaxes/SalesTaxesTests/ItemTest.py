import unittest


class ItemTest(unittest.TestCase):

    def normal_item(self):
        return NotImplemented

    def bad_item(self):
        return NotImplemented

    def exempt_item(self):
        return NotImplemented

    def imported_item(self):
        return NotImplemented


def main():
    unittest.main()

if __name__ == '__main__':
    main()