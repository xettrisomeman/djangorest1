from rest_framework import viewsets

from .models import (
    Cast ,
    Director,
    Movie
)
from .serializers import (
    CastSerializer,
    MovieSerializer,
    DirectorSerializer
)

class CastViewSet(viewsets.ModelViewSet):
    serializer_class = CastSerializer
    queryset = Cast.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class DirectorViewSet(viewsets.ModelViewSet):
    serializer_class= DirectorSerializer
    queryset = Director.objects.all()

