from django.shortcuts import render
from rest_framework import viewsets
from userapp.models import User, Account, Transactions
from userapp.serializer import UserSerializer, AccountSerializer, TransactionSerializer
from rest_framework.response import Response
from userapp.services import deposit, create_acc_no, withdraw
# Create your views here.


def index(request):
    return render(request, 'base.html')


class UsersView(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        queryset = User.objects.get(pk=pk)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

    def create_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def user_accounts(self, request, pk):
        account = Account.objects.filter(user=pk)
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

    def delete_user(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response("Deleted User Sucessfully")



class AccountsView(viewsets.ViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def list(self, request):
        queryset = Account.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def create_acc(self, request, pk):
        return create_acc_no(pk, request.data)

    def list_acc(self, request, id, pk):
        queryset = Account.objects.get(id=id)
        serializer = AccountSerializer(queryset)
        return Response(serializer.data)

    def delete_acc(self, request, id, pk):
        acc = Account.objects.get(id=id)
        acc.delete()
        return Response("Account deleted Sucessfully")


class TransactionsView(viewsets.ViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    def deposit_amt(self, request, pk, id):
        return deposit(pk, request.data['amount'], id)

    def withdraw_amt(self, request, pk, id):
        return withdraw(pk, request.data['amount'], id)

