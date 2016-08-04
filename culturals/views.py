from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cultural
from .serializers import CulturalSr


class CulturalAtGlance(APIView):

    def get(self, request, format=None):
        cultural_list = Cultural.objects.all()
        serializer = CulturalSr(cultural_list, many=True)
        return Response(serializer.data)
