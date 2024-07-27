from rest_framework import serializers
from .models import  Country , Provinec , Directorate , AreWe , Advertising

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class ProvinecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinec
        fields = '__all__'

class DirectorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directorate
        fields = '__all__'

class AreWeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreWe
        fields = '__all__'

class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = '__all__'
