from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_name>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<movie_name>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<movie_name>[0-9]+)/show/$', views.show, name='show'),
    ]
