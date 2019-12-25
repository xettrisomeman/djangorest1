from rest_framework import serializers

from .models import (
    Cast , 
    Director,
    Movie
)

class CastSerializer(serializers.ModelSerializer):
    #to display category name = 'Actor' rather 'A+'
    category = serializers.CharField(source='get_category_display')
    class Meta:
        model = Cast 
        fields = "__all__"


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"

