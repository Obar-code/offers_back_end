from django.shortcuts import render
from . import serializers
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from places.views import CustomPagination
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated ,DjangoModelPermissionsOrAnonReadOnly ,DjangoObjectPermissions 
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class AccountCreateView(APIView):
    serializer_class = serializers.AccountSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            token, created = Token.objects.get_or_create(user=account)
            group = Group.objects.get(name=account.type_account)
            group.user_set.add(account)
            response_data = {
                    'first_name': account.first_name,
                    'email': account.email,
                    'is_superuser': account.is_superuser,
                    'is_active': account.is_active,
                    'type_account':account.type_account,
                    'authtoken':token.key 
            }
            return Response(response_data)
        else:
            # errors = {}
            # for field, field_errors in serializer.errors.items():
            #     errors[field] = field_errors[0]
            # # errors = serializer.errors
            return Response(serializer.errors)


class Website(viewsets.ModelViewSet):
    queryset = serializers.Website.objects.filter(status=2)
    serializer_class = serializers.WebsiteSerializer
    pagination_class = CustomPagination

class Market(viewsets.ModelViewSet):
    queryset = serializers.Market.objects.filter(status=2)
    serializer_class = serializers.MarketSerializer
    pagination_class = CustomPagination

class GlobalWebsite(viewsets.ModelViewSet):
    queryset = serializers.GlobalWebsite.objects.filter(status=2)
    serializer_class = serializers.GlobalWebsiteSerializer
    pagination_class = CustomPagination