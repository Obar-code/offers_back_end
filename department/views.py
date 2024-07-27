from django.shortcuts import render
from . import serializers
from rest_framework import viewsets
from places.views import CustomPagination
# Create your views here.

class Department(viewsets.ModelViewSet):
    queryset = serializers.Department.objects.filter(status=2)
    serializer_class = serializers.DepartmentSerializer
    pagination_class = CustomPagination