# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Restaurent


class RestaurentSr(ModelSerializer):

    class Meta:
        model = Restaurent
        fields = ('name', 'pic', 'ambience',)
