class Tax:

    def __init__(self, import_tax, sales_tax):
        self.import_tax = import_tax
        self.sales_tax = sales_tax

    """
    Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical products
    Import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions.

    When I purchase items I receive a receipt which lists the name of all the items and their price (including tax),
    finishing with the total cost of the items, and the total amounts of sales taxes paid.
    The rounding rules for sales tax are that
        for a tax rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax.
    """

    def get_import_duty(self):
        return NotImplemented

    def get_sales_tax(self):
        return NotImplemented