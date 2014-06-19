from django.db import models
import datetime


class CompanyData(models.Model):
    date = models.CharField(max_length=5)
    category = models.CharField(max_length=5)
    employee_name = models.CharField(max_length=5)
    employee_address = models.CharField(max_length=5)
    expense_description = models.CharField(max_length=5)
    pre_tax_amount = models.CharField(max_length=5)
    tax_name = models.CharField(max_length=5)
    tax_amount = models.CharField(max_length=5)
