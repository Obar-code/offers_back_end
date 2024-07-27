from rest_framework import serializers
from .models import  CurrencyType , Offer , Coupon , LocalCoupon , GlobalCoupon 

class CurrencyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyType
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class LocalCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalCoupon
        fields = '__all__'

class GlobalCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalCoupon
        fields = '__all__'
