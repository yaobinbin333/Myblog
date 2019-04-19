from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^', views.index, name='index'),
    # url(r'^about/$', views.about, name='about'),
    # url(r'^archive/$', views.about, name='archive'),
]