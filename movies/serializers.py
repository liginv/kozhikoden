from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Movie, Show, Time


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
    class Meta:
        model = Show
        fields = ('movie', 'time', 'hall',)
        depth = 2
