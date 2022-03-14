# from django.shortcuts import render
from typing import Callable

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response

from myapi.renderers import LatexRenderer, PlainTextRenderer
from myapi.serializers import FilmSerializer
from myapi.models import Film
import myapi.services.com_service as com


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all().order_by("projection_date")
    serializer_class = FilmSerializer

    def general_com_view(self, com_function: Callable[[Film], str]):
        film: Film = self.get_object()
        preview_text = com_function(film)
        return Response(preview_text)

    # TODO confirm that latex renderer is not a problem
    @action(detail=True, renderer_classes=[LatexRenderer], methods=["GET"])
    def bocal(self, request, pk=None):
        return self.general_com_view(com.bocal)

    @action(detail=True, renderer_classes=[PlainTextRenderer], methods=["GET"])
    def facebook(self, request, pk=None):
        return self.general_com_view(com.facebook)
