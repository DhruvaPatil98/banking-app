
from rest_framework import serializers
from userapp.models import User, Account
from rest_framework.response import Response
from datetime import date


class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'
 
