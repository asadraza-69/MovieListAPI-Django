from rest_framework import serializers
from .models import *

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = '__all__'
        # fields = ['name', 'description' ,'active'] => for selected fields in MovieModel
        exclude = ['id']
        
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