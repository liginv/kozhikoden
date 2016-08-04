# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Movie, Show, Theatre


class ShowSr(ModelSerializer):

    class Meta:
        model = Show
        fields = ('movie', 'theatre',)
        depth = 1


class MovieSr(ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
