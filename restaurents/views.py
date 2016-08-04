from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Restaurent
from .serializers import RestaurentSr


class RestaurentAtGlance(APIView):

    def get(self, request, format=None):
        rest_list = Restaurent.objects.all()
        serializer = RestaurentSr(rest_list, many=True)
        return Response(serializer.data)
