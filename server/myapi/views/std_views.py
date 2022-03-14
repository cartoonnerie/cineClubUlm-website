# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from myapi.renderers import LatexRenderer, PlainTextRenderer
from myapi.serializers import FilmSerializer
from myapi.models import Film
import myapi.services.com_service as com


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all().order_by("projection_date")
    serializer_class = FilmSerializer

    # TODO confirm that latex renderer is not a problem
    @action(detail=True, renderer_classes=[LatexRenderer], methods=["GET"])
    def bocal(self, request, pk=None):
        film: Film = self.get_object()
        bocal_text = com.bocal(film)
        return Response(bocal_text)

    @action(detail=True, renderer_classes=[PlainTextRenderer], methods=["GET"])
    def facebook(self, request, pk=None):
        film: Film = self.get_object()
        fb_text = com.facebook(film)
        return Response(fb_text)
