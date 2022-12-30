from django.urls import path, include
from watchlist_app.views import *


urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('<int:pk>', movie_details, name='movie_details'),
    path('func-serializer/', serial_movie_list, name='serial_movie_list'),
    path('func-serializer/<int:pk>', serial_movie_details, name='serial_movie_details'),
    path('serializer/', MovielistApiView.as_view(), name='MovielistApiView'),
    path('serializer/<int:pk>', MovieDetailApiView.as_view(), name='MovieDetailApiView'),
]
