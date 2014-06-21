from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Sum, connection
from datetime import datetime
from decimal import Decimal
import csv
import codecs

from fileReader.app.forms import UploadFileForm
from fileReader.app.models import CompanyData


def home(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['uploadedfile'])
            return HttpResponseRedirect(reverse('fileReader.app.views.result'))
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
    csv_data = csv.reader(codecs.iterdecode(f, 'utf-8'), delimiter=',', quotechar='"')
    next(csv_data)
    for row in csv_data:
        #TODO try-catch for value errors
        company_data = CompanyData(date=datetime.strptime(row[0], "%m/%d/%Y").date(),
                                   category=row[1],
                                   employee_name=row[2],
                                   employee_address=row[3],
                                   expense_description=row[4],
                                   pre_tax_amount=Decimal(row[5].strip().replace(',', '')),
                                   tax_name=row[6],
                                   tax_amount=Decimal(row[7].strip().replace(',', '')))
        company_data.save()


def result(request):
    # Generate results for result page
    truncate_date = connection.ops.date_trunc_sql('month', 'date')
    qs = CompanyData.objects.extra({'month': truncate_date})
    data = qs.values('month').annotate(Sum('tax_amount'), Sum('pre_tax_amount')).order_by('month')

    #TODO make expense column part of SQL query
    for row in data:
        row['expense'] = row.get('tax_amount__sum') + row.get('pre_tax_amount__sum')

    return render_to_response(
        'app/result.html',
        {'data': data},
        context_instance=RequestContext(request)
    )
