from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event
from .serializers import EventSr

class EventAtGlance(APIView):

    def get(self, request, format=None):
        event_list = Event.objects.all()
        serializer = EventSr(event_list, many=True)
        return Response(serializer.data)
