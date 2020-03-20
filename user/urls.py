"""user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from userapp import views
from rest_framework import routers
from userapp.views import UsersView, AccountsView, TransactionsView, TransferView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UsersView.as_view({'get': 'list'})),
    path('accounts/', views.AccountsView.as_view({'get': 'list'})),
    path('transactions/', views.TransferView.as_view({'get': 'list'})),
    path('users/create/', views.UsersView.as_view({'post': 'create_user'})),
    path('users/<uuid:pk>/', views.UsersView.as_view({'get': 'update'})),
    path('users/<uuid:pk>/delete/', views.UsersView.as_view({'get': 'delete_user'})),
    path('users/<uuid:pk>/accounts/', views.UsersView.as_view({'get': 'user_accounts'})),
    path('users/<uuid:pk>/accounts/create/', views.AccountsView.as_view({'post': 'create_acc'})),
    path('users/<uuid:pk>/accounts/<uuid:id>/', views.AccountsView.as_view({'get': 'list_acc'})),
    path('users/<uuid:pk>/accounts/<uuid:id>/action/', views.TransactionsView.as_view({'post': 'action'})),
    path('users/<uuid:pk>/accounts/<uuid:id>/transfer/', views.TransferView.as_view({'post': 'transfer_amt'})),
    path('users/<uuid:pk>/accounts/<uuid:id>/delete/', views.AccountsView.as_view({'get': 'delete_acc'})),
    path('', include('userapp.urls')),
]
