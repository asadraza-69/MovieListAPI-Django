from django.urls import path, include
from watchlist_app.views import *


urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('<int:pk>', movie_details, name='movie_details'),
    path('func-serializer/', serial_movie_list, name='serial_movie_list'),
    path('func-serializer/<int:pk>', serial_movie_details, name='serial_movie_details'),
    path('serializer/', MovielistApiView.as_view(), name='MovielistApiView'),
    path('serializer/<int:pk>', MovieDetailApiView.as_view(), name='MovieDetailApiView'),
    path('platform/', PlatformApiView.as_view(), name='MovielistApiView'),
    path('platform/<int:pk>', PlatformDetailApiView.as_view(), name='MovieDetailApiView'),
    path('reviews/', ReviewApiView.as_view(), name='ReviewApiView'),
    path('reviews/<int:pk>', ReviewDetailApiView.as_view(), name='MovieDetailApiView'),
    path('reviews1/', ReviewApiView1.as_view(), name='ReviewApiView1'),
    path('reviews1/<int:pk>', ReviewDetailApiView1.as_view(), name='MovieDetailApiView1'),
    path('reviews2/', ReviewApiView2.as_view(), name='ReviewApiView2'),
    # path('reviews/<int:pk>', ReviewDetailApiView.as_view(), name='MovieDetailApiView'),
]
