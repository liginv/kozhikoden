from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Cultural

class CulturalSr(ModelSerializer):

    class Meta:
        model = Cultural
        fields = ('name', 'pic', 'event_type',)
