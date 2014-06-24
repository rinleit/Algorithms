from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from fileReader.app.views import home, result

urlpatterns = patterns('',
                       url(r'^home/$', home, name='home'),
                       url(r'^result/$', result, name='result')
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
