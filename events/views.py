from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event
from .serializers import EventSr, EventDetailSr


class EventAtGlance(APIView):

    def get(self, request, format=None):
        event_list = Event.objects.all()
        serializer = EventSr(event_list, many=True)
        return Response(serializer.data)

class EventDetail(APIView):

    def get(self, request, event_id, format=None):
        event_list = Event.objects.filter(id=event_id)
        serializer = EventDetailSr(event_list, many=True)
        return Response(serializer.data)
