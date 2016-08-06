# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Restaurent
from movies.serializers import LocationField


class RestaurentSr(ModelSerializer):

    class Meta:
        model = Restaurent
        fields = ('id', 'name', 'pic', 'ambience',)

class RestaurentDetailSr(ModelSerializer):
    location = LocationField()
    class Meta:
        model = Restaurent
        fields = '__all__'
