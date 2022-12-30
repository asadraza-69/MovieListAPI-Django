from rest_framework import serializers
from .models import *
from datetime import datetime

class steamplatformSerializers(serializers.ModelSerializer):
    class Meta:
        model = Steamplatform
        # fields = '__all__' => for all fields in MovieModel
        # fields = ['name', 'description' ,'active'] => for selected fields in MovieModel
        exclude = ['id']



class MovieSerializers(serializers.ModelSerializer):
    
    len_name_movie = serializers.SerializerMethodField()
    current_datetime = serializers.SerializerMethodField()
    # this is used to add field to model through serializer
    
    class Meta:
        model = Movie
        # fields = '__all__' => for all fields in MovieModel
        # fields = ['name', 'description' ,'active'] => for selected fields in MovieModel
        exclude = ['id']

    def get_len_name_movie(self, object):
        length = len(object.name)
        return length

    def get_current_datetime(self, object):
        return datetime.now()  


    # object level validation for object
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description are required to be different")
        return data
    
    # field level validation for fields
    def validate_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Name must be at least greater than 2 characters")
        else:
            return value