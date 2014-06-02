import unittest


class CheckoutTest(unittest.TestCase):

    def no_items(self):
        return NotImplemented

    def single_item(self):
        return NotImplemented

    def two_items(self):
        return NotImplemented

    def multi_items(self):
        return NotImplemented

    def exempt_item(self):
        return NotImplemented

    def imported_item(self):
        return NotImplemented

    def mixed_items(self):
        return NotImplemented


def main():
    unittest.main()

if __name__ == '__main__':
    main()