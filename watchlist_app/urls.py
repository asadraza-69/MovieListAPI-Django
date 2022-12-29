from django.urls import path, include
from watchlist_app.views import *


urlpatterns = [
    path('', movie_list, name='movie-list'),
    path('<int:pk>', movie_details, name='movie-detail'),
    path('serializer/', serial_movie_list, name='serial_movie_list'),
    path('serializer/<int:pk>', serial_movie_details, name='serial_movie_details'),
]
