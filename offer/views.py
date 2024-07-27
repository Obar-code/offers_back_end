from django.shortcuts import render
from . import serializers
from rest_framework import viewsets
from places.views import CustomPagination
# Create your views here.

class CurrencyType(viewsets.ModelViewSet):
    queryset = serializers.CurrencyType.objects.filter(status=2)
    serializer_class = serializers.CurrencyTypeSerializer
    pagination_class = CustomPagination

class Offer(viewsets.ModelViewSet):
    queryset = serializers.Offer.objects.filter(status=2)
    serializer_class = serializers.OfferSerializer
    pagination_class = CustomPagination

class Coupon(viewsets.ModelViewSet):
    queryset = serializers.Coupon.objects.filter(status=2)
    serializer_class = serializers.CouponSerializer
    pagination_class = CustomPagination

class LocalCoupon(viewsets.ModelViewSet):
    queryset = serializers.LocalCoupon.objects.filter(status=2)
    serializer_class = serializers.LocalCouponSerializer
    pagination_class = CustomPagination

class GlobalCoupon(viewsets.ModelViewSet):
    queryset = serializers.GlobalCoupon.objects.filter(status=2)
    serializer_class = serializers.GlobalCouponSerializer
    pagination_class = CustomPagination