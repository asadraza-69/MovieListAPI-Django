from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
from .serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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

@api_view(['GET','POST'])
def serial_movie_list(request): 
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializers = MovieSerializers(movies,many=True)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    if request.method == 'POST':
        serializers = MovieSerializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET','PUT','DELETE'])
def serial_movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
            serializers = MovieSerializers(movie)
            return Response(serializers.data,status=status.HTTP_200_OK)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializers = MovieSerializers(movie,data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializers.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)