# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include
from django.views.generic import RedirectView

urlpatterns = patterns('',
                       (r'^/', include('fileReader.app.urls')),
                       (r'^$', RedirectView.as_view(url='/')),  # Just for ease of use.
                       )
