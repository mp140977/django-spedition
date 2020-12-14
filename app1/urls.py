from django.contrib import admin
from django.urls import include, path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('bestellung/', views.bestellung, name='bestellung'),
]
