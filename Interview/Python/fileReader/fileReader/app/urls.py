# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('fileReader.app.views',
                       url(r'^home/$', 'home', name='home'),
                       url(r'^result/$', 'result', name='result'),
                       )