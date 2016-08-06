from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import EventAtGlance, EventDetail

urlpatterns = [
    url(r'^latest/$', EventAtGlance.as_view(), name='eventglance'),
    url(r'(?P<event_id>[0-9]+)/detail/$', EventDetail.as_view(),
        name='eventdetail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
