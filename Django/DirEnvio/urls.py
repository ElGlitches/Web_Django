from django.urls import path
from .import views

urlpatterns = [
    path('', views.DireccionEnvioListView.as_view(), name='direccion_envio'),
    path('nueva', views.FormularioDir, name='formulariodir'),
]