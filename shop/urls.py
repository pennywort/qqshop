from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from shop.models import Post
from django.conf import settings
from django.contrib.auth.decorators import login_required
urlpatterns = patterns('',
					    url(r'^$', login_required(ListView.as_view(
						   queryset=Post.objects.all().order_by("-date")[:10],
						   template_name="blog.html"))),
						   
					    url(r'^(?P<pk>\d+)$', login_required(DetailView.as_view(
						   model = Post,
						   template_name="post.html"))),

						url(r'^add/$', 'shop.views.add', name='add'),
						url(r'^del/$', 'shop.views.delete', name='delete'),
						url(r'^accept/$', 'shop.views.accept', name='accept'),
						url(r'^orders/$', 'shop.views.display', name='i'),
)
