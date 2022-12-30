from rest_framework import serializers
from .models import *
from datetime import datetime

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


class steamplatformSerializers(serializers.ModelSerializer):
    # As opposed to previously discussed references to another entity,
    # the referred entity can instead also be embedded or nested in the representation of the object 
    # that refers to it. Such nested relationships can be expressed by using serializers as fields.
    # If the field is used to represent a to-many relationship, you should add the many=True flag to the serializer field.
    # model mai foregin key mai related_name jo hoga iski he field banegi    
    plateform_name = MovieSerializers(many = True , read_only = True)
    # StringRelatedField may be used to represent the target of the relationship using its __str__ method.
    # plateform_name = serializers.StringRelatedField(many=True)
    # PrimaryKeyRelatedField may be used to represent the target of the relationship using its primary key.
    # plateform_name = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    # plateform_name = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='MovieDetailApiView'
    # )
    print("plateform_name: ",plateform_name)
    class Meta:
        model = Steamplatform
        # fields = '__all__' => for all fields in MovieModel
        # fields = ['name', 'description' ,'active'] => for selected fields in MovieModel
        exclude = ['id']