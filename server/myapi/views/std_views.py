# from django.shortcuts import render
from rest_framework import viewsets

from myapi.serializers import FilmSerializer
from myapi.models import Film


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all().order_by('projection_date')
    serializer_class = FilmSerializer

# Create your views here.
