from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CulturalAtGlance

urlpatterns = [
    url(r'^latest/$', CulturalAtGlance.as_view(), name='culturalglance'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)