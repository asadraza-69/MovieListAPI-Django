from rest_framework import serializers
from .models import *


#Individual fields on a serializer can include validators, by declaring them on the field instance, for example:
def validate_description_func(value):
    if len(value) <= 10:
        raise serializers.ValidationError("description must be at least greater than 10 characters")
    else:
        return value

class MovieSerializers(serializers.Serializer):

    name = serializers.CharField(required=False, max_length=50) 
    description = serializers.CharField(required=False,max_length=200,validators = [validate_description_func])
    active = serializers.BooleanField(required=False,default=True)
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance


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
    
    


    