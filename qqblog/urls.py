from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qqblog.views.home', name='home'),
    #(r'^$', lambda r: HttpResponseRedirect('/shop/')),
    (r'^$', 
        TemplateView.as_view(template_name='index.html')),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^shop/', include('shop.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
