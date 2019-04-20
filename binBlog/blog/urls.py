from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^/$', views.index, name='index'),
    url(r'^index/$', views.index),
    url(r'^blogs/$', views.blogs, name='blogs'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^about/$', views.about, name='about'),
    # url(r'^archive/$', views.about, name='archive'),
]