from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Movie, Show, Time, Theatre


class LocationField(serializers.Field):

    def to_representation(self, obj):
        location = {'lat': obj.latitude, 'long': obj.longitude}
        return location

class TheatreSr(ModelSerializer):
    location = LocationField()
    class Meta:
        model = Theatre
        fileds = ('location',)

class TimeSr(ModelSerializer):

    class Meta:
        model = Time
        fields = ('time',)
        
class ShowSr(ModelSerializer):

    class Meta:
        model = Show
        fields = ('id', 'movie', 'theatre',)
        depth = 1


class MovieSr(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ShowDetailSr(ModelSerializer):
    time = TimeSr(many=True)
    theatre = TheatreSr()
    class Meta:
        model = Show
        fields = ('movie', 'time', 'hall', 'theatre',)
        depth = 2
