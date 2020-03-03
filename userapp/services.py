from userapp.models import User
from userapp.serializer import AccountSerializer, TransactionSerializer, TransferSerializer
from rest_framework.response import Response
from userapp.models import Account, User, Transactions
from userapp.utils import random_acc_no_generator, random_pin_number_generator
from datetime import datetime, date
from hashlib import sha256

def create_acc_no(pk, pin):
    user_year = User.objects.get(pk=pk).dob.year
    user_month = User.objects.get(pk=pk).dob.month
    user_day = User.objects.get(pk=pk).dob.day

    age = calculateAge(date(int(user_year), int(user_month), int(user_day)))
    print(age)
    if age > 18:
        if User.objects.get(pk=pk).accounts.count() < 3:
            json_obj = {
                        'acc_no': random_acc_no_generator(),
                        'pin': random_pin_number_generator(),
                        'balance': 2000,
                        'user': User.objects.get(pk=pk).pk,
                    }
        
            serialized = AccountSerializer(data=json_obj)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data)
            else:
                return Response(serialized.errors)

        else:
            return Response("Cannot have more than 3 acocunts")
    else:
        return Response("The user needs to be 18+ to have an account")


def withdraw(self, amount, pk):
    acc = Account.objects.get(pk=pk)
    if int(acc.balance) >= 2000:
        if int(amount) <= (int(acc.balance)) and (int(acc.balance) - int(amount) >= 2000):
            acc.balance -= int(amount)
            acc.save()
            return Response("Amount withdrawn sucessfully")
        else:
            return Response("Insufficient balance")
    

def deposit(self, amount, pk):
    acc = Account.objects.get(pk=pk)
    acc.balance += int(amount)
    acc.save()
    return Response("Amount deposited sucessfully")


def transfer(self, pk, reciver_acc, amount):
    sender = Account.objects.get(pk=pk)
    reciver = Account.objects.get(pk=reciver_acc)
    amount = int(amount)

    if sender == reciver:
        return Response("Cannot transfer money between same accounts ")
    else:
        if amount <= (int(sender.balance)) and (int(sender.balance) - amount >= 2000):
            sender.balance -= amount
            reciver.balance += amount
            sender.save()
            reciver.save() 

            transactiondata = {
                'sender': sender.pk,
                'reciver': reciver.pk,
                'amount': amount
            }        

            serialized = TransferSerializer(data=transactiondata)

            if serialized.is_valid():
                serialized.save()
                return Response('Money Sucessfully Transfered')
            else:
                return Response(serialized.errors)

        else:
            return Response("Insufficient Balance to Transfer")


def calculateAge(birthDate):
    days_in_year = 365.2425
    age = int((date.today() - birthDate).days / days_in_year)
    return age
