from rest_framework import serializers
from .models import *


class MovieSerializers(serializers.Serializer):
    class Meta:
        model = Movie
        fields = '__all__'