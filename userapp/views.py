from django.shortcuts import render
from rest_framework import viewsets
from userapp.models import User, Account, Transactions, Transfer
from userapp.serializer import UserSerializer, AccountSerializer, TransactionSerializer, TransferSerializer
from rest_framework.response import Response
from userapp.services import deposit, create_acc_no, withdraw, transfer
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
    
    # used to get all accounts
    def list(self, request):
        acc = Account.objects.all()
        serializer = AccountSerializer(acc, many=True)
        return Response(serializer.data)

    # used to create the accounts for the user
    def create_acc(self, request, pk):
        return create_acc_no(pk, request.data)

    # used to get a particular account of the user
    def list_acc(self, request, id, pk):
        account = Account.objects.get(id=id)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    # used to delete account
    def delete_acc(self, request, id, pk):
        acc = Account.objects.get(id=id)
        acc.delete()
        return Response("Account deleted Sucessfully")


class TransactionsView(viewsets.ViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    def action(self, request, pk, id):
        if request.data['action'] == 'deposit':
            return deposit(pk, request.data['amount'], id)
        elif request.data['action'] == 'withdraw':
            return withdraw(pk, request.data['amount'], id)
        else:
            return Response("Specify correct Action ")


class TransferView(viewsets.ViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    def list(self, request):
        queryset = Transfer.objects.all()
        serializer = TransferSerializer(queryset, many=True)
        log_file = open('log.txt', 'a+')
        log_file.write(str(serializer.data))
        log_file.write('\n')
        log_file.write(str(queryset))
        log_file.write('\n')
        log_file.close()
        return Response(serializer.data)

    def transfer_amt(self, request, pk, id):
        return transfer(pk, id, amount=request.data['amount'], reciver_acc=request.data['reciver'])