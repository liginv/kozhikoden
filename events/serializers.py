# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Event


class EventSr(ModelSerializer):

    class Meta:
        model = Event
        fields = ('name', 'pic', 'organiser',)
