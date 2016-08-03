from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import EventAtGlance

urlpatterns = [
    url(r'^latest/$', EventAtGlance.as_view(), name='eventglance'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
