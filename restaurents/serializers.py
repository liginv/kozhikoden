# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Restaurent


class RestaurentSr(ModelSerializer):

    class Meta:
        model = Restaurent
        fields = ('id', 'name', 'pic', 'ambience',)

class RestaurentDetailSr(ModelSerializer):

    class Meta:
        model = Restaurent
        fields = '__all__'
