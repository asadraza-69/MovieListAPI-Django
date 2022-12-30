from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
from .serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
    }
    return JsonResponse(data)

@api_view(['GET'])
def serial_movie_list(request):
    movies = Movie.objects.all()
    serializers = MovieSerializers(movies,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def serial_movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializers = MovieSerializers(movie)
    return Response(serializers.data)