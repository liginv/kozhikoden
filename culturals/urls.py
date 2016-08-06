from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CulturalAtGlance, CulturalDetail

urlpatterns = [
    url(r'^latest/$', CulturalAtGlance.as_view(), name='culturalglance'),
    url(r'^(?P<cultural_id>[0-9]+)/detail/$', CulturalDetail.as_view(),
        name='culturaldetail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
