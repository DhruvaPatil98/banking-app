
from rest_framework import serializers
from userapp.models import User, Account, Transactions


class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ('amount',)
