# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('newproject.newproject.app.views',
                       url(r'^list/$', 'list', name='list'),
                       )

