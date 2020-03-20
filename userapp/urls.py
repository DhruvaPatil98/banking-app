from django.urls import path
from userapp import views
from userapp.views import index

urlpatterns = [
    path('', views.index),
]
