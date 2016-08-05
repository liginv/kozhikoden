from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import RestaurentAtGlance, RestaurentDetail

urlpatterns = [
    url(r'^general/$', RestaurentAtGlance.as_view(), name='restglance'),
    url(r'^(?P<restaurent_id>[0-9]+)/detail/$', RestaurentDetail.as_view(),
        name='restaurentdetail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
