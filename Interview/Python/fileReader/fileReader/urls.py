from django.conf.urls import patterns, include
from django.views.generic import RedirectView

urlpatterns = patterns('',
                       (r'^app/', include('fileReader.app.urls')),
                       (r'^$', RedirectView.as_view(url='/app/home/')),  # Just for ease of use.
                       )
