from rest_framework import serializers
from .models import Film


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"  # TODO also send id
