from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import csv

from fileReader.app.forms import UploadFileForm
from fileReader.app.models import CompanyData


def home(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['uploadedfile'])
            return HttpResponseRedirect(reverse('fileReader.app.views.home'))
    else:
        # A empty, unbound form
        form = UploadFileForm()

    # Render home page
    return render_to_response(
        'app/home.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


def handle_uploaded_file(f):
    dataReader = csv.reader(f, delimiter=',', quotechar='"')
    for row in dataReader:
        companyData = CompanyData
        companyData.date = row[0]
        companyData.category = row[1]
        companyData.employee_name = row[2]
        companyData.employee_address = row[3]
        companyData.expense_description = row[4]
        companyData.pre_tax_amount = row[5]
        companyData.tax_name = row[6]
        companyData.tax_amount = row[7]
        print("%s %s" % (companyData.date, companyData.category))