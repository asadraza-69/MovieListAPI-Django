from rest_framework import serializers
from .models import *


class MovieSerializers(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=50) 
    description = serializers.CharField(required=False,max_length=200)
    active = serializers.BooleanField(required=False,default=True)
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance
    # class Meta:
    #     model = Movie
    #     fields = '__all__'
        # fields = ('id', 'name', 'description' ,'active')