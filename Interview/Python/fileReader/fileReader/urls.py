# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
                       (r'^app/', include('fileReader.app.urls')),
                       (r'^$', RedirectView.as_view(url='/app/home/')),  # Just for ease of use.
                       )
