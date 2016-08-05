from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Restaurent
from .serializers import RestaurentSr, RestaurentDetailSr


class RestaurentAtGlance(APIView):

    def get(self, request, format=None):
        rest_list = Restaurent.objects.all()
        serializer = RestaurentSr(rest_list, many=True)
        return Response(serializer.data)

class RestaurentDetail(APIView):

    def get(self, request, restaurent_id, format=None):
        rest_list = Restaurent.objects.filter(id=restaurent_id)
        serializer = RestaurentDetailSr(rest_list, many=True)
        return Response(serializer.data)
