from django.urls import path
from . import views

urlpatterns = [
    path('validar', views.validar, name='validar'),
]