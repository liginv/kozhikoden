# from django.http import Http404
from django.shortcuts import render
# get_object_or_404,
# from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView

from rest_framework.views import APIView
from rest_framework.response import Response

from movies.models import Show, Movie
from movies.serializers import ShowSr, MovieSr


def home(request):
    return HttpResponse("Welcome to Kozhikodens")


class Index(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSr(movies, many=True)
        return Response(serializer.data)


class MovieAtGlance(APIView):

    def get(self, request, format=None):
        movies_run = Show.objects.filter(movie__status='RUN')
        serializer = ShowSr(movies_run, many=True)
        return Response(serializer.data)


class Movies(View):

    def get(self, request):
        latest_show_list = Show.objects.order_by('-show_name')[:5]
        context = {'latest_show_list': latest_show_list}
        return render(request, 'movies/index.html', context)

"""
def detail(request, movie_name):
    try:
        show = Show.objects.get(pk=movie_name)
    except Show.DoesNotExist:
        raise Http404("Show does not exist")
    return render(request, 'movies/detail.html', {'show': show})


def results(request, movie_name):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % movie_name)


def show(request, movie_name):
    return HttpResponse("You're seeing on movie %s." % movie_name)
"""


# def index(request):
#    latest_show_list = Show.objects.order_by('-show_name')[:5]
#    template = loader.get_template('movies/index.html')
#    context = RequestContext(request, {
#                             'latest_show_list': latest_show_list,
#                             })
#    return HttpResponse(template.render(context))


class Listview(ListView):
    model = Show


