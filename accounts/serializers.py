from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from .models import Account , Website , Market , GlobalWebsite

def validate_unique_email(value):
    if Account.objects.filter(email=value).exists():
        raise serializers.ValidationError(_("هذا البريد مسجل من قبل."))
    return value

def get_unique_username(username):
    original_username = username
    counter = 1
    while Account.objects.filter(username=username).exists():
        username = original_username + str(counter)
        counter += 1
    return username

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[validate_unique_email])

    class Meta:
        model = Account
        fields = ('password', 'confirm_password', 'email', 'first_name','type_account','phone_number','image','directorate')

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError(_("كلمتا المرور غير متطابقتين."))
        return data

    def create(self, validated_data):
        email = validated_data['email']
        username = email.split('@')[0]
        username = get_unique_username(username)
        account = Account.objects.create(
            email=email,
            username=username,
            first_name=validated_data['first_name'],
            type_account=validated_data['type_account'],
            phone_number=validated_data['phone_number'],
            image=validated_data['image'],
            directorate=validated_data['directorate']
        )
        account.set_password(validated_data['password'])
        account.save()
        return account

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class GlobalWebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalWebsite
        fields = '__all__'