# from django.shortcuts import render
from rest_framework import viewsets

from .serializers import FilmSerializer
from .models import Film

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all().order_by('projection_date')
    serializer_class = FilmSerializer

# Create your views here.
