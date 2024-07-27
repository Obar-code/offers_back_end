from django.shortcuts import render
from . import serializers
from rest_framework import viewsets , pagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class CustomPagination(pagination.PageNumberPagination):
    page_size = 25
    max_page_size = 100

    def get_paginated_response(self, data):
        if not data:
            return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'result': data,
            },status=200)

        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'result': data,
        })
    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return int(page_number)

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        return int(page_number)

class Country(viewsets.ModelViewSet):
    queryset = serializers.Country.objects.filter(status=2)
    serializer_class = serializers.CountrySerializer
    pagination_class = CustomPagination

class Provinec(viewsets.ModelViewSet):
    queryset = serializers.Provinec.objects.filter(status=2)
    serializer_class = serializers.ProvinecSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    pagination_class = CustomPagination

class Directorate(viewsets.ModelViewSet):
    queryset = serializers.Directorate.objects.filter(status=2)
    serializer_class = serializers.DirectorateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['provinec']
    pagination_class = CustomPagination

class AreWe(viewsets.ModelViewSet):
    queryset = serializers.AreWe.objects.filter(status=2)
    serializer_class = serializers.AreWeSerializer

class Advertising(viewsets.ModelViewSet):
    queryset = serializers.Advertising.objects.filter(status=2)
    serializer_class = serializers.AdvertisingSerializer
    