from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import RestaurentAtGlance

urlpatterns = [
    url(r'^latest/$', RestaurentAtGlance.as_view(), name='restglance'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
