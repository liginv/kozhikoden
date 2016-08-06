from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Cultural
from movies.serializers import LocationField

class CulturalSr(ModelSerializer):

    class Meta:
        model = Cultural
        fields = ('id', 'name', 'pic', 'event_type',)

class CulturalDetailSr(ModelSerializer):
    location = LocationField()
    
    class Meta:
        model = Cultural
        fields = '__all__'
