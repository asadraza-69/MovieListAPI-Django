from rest_framework import serializers
from .models import *


class MovieSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50) 
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField(default=True)
    
    # class Meta:
    #     model = Movie
    #     fields = ('id', 'name', 'description' ,'active')