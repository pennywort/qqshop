from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from shop.models import Post
from django.conf import settings
urlpatterns = patterns('',
					   url(r'^$', ListView.as_view(
						   queryset=Post.objects.all().order_by("-date")[:10],
						   template_name="blog.html")),
						   
					   url(r'^(?P<pk>\d+)$', DetailView.as_view(
						   model = Post,
						   template_name="post.html")),
						   
					   url(r'^order/$', ListView.as_view(	
						   queryset=Post.objects.all().order_by("-date")[:10],
						   template_name="order.html")),
					  # url(r'^accounts/', include('registration.urls')),
)
#if settings.DEBUG:
 #   from django.views.static import serve
 #   _media_url = settings.MEDIA_URL
 #   if _media_url.startswith('/'):
  #      _media_url = _media_url[1:]
 #       urlpatterns += patterns('',
  #                              (r'^%s(?P<path>.*)$' % _media_url,
   #                             serve,
   #                             {'document_root': settings.MEDIA_ROOT}))
  #  del(_media_url, serve)