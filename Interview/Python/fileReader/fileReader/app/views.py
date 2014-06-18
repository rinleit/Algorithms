# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def home(request):

    # Render list page with the documents and the form
    return render_to_response(
        'app/home.html',
        context_instance=RequestContext(request)
    )