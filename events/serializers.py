# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Event
from movies.serializers import LocationField

class EventSr(ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'name', 'pic', 'organiser',)

class EventDetailSr(ModelSerializer):
    location = LocationField()
    class Meta:
        model = Event
        fields = ('name', 'pic', 'organiser', 'starting_time', 'fee',
                  'location', 'contact_no',)
