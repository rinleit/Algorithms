from django.db import models


class CompanyData(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=5)
    employee_name = models.CharField(max_length=5)
    employee_address = models.CharField(max_length=5)
    expense_description = models.CharField(max_length=5)
    pre_tax_amount = models.DecimalField(max_digits=8, decimal_places=2)
    tax_name = models.CharField(max_length=5)
    tax_amount = models.DecimalField(max_digits=8, decimal_places=2)
