import unittest


class TaxTest(unittest.TestCase):

    def normal_tax(self):
        return NotImplemented

    def exempt_tax(self):
        return NotImplemented

    def imported_tax(self):
        return NotImplemented


def main():
    unittest.main()

if __name__ == '__main__':
    main()