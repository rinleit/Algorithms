class Tax:

    def __init__(self, import_tax, sales_tax):
        self.import_tax = import_tax
        self.sales_tax = sales_tax

    def get_import_duty(self):
        return NotImplemented

    def get_sales_tax(self):
        return NotImplemented