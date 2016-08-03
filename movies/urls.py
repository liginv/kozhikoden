from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from movies.views import Index, MovieAtGlance

urlpatterns = [
    url(r'^all/$', Index.as_view(), name='index'),
    url(r'^latest/$', MovieAtGlance.as_view(), name='movieglance'),
    # url(r'^(?P<movie_name>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<movie_name>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<movie_name>[0-9]+)/show/$', views.show, name='show'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
