from django.urls import path
from .import views

urlpatterns = [
    path('', views.DireccionEnvioListView.as_view(), name='direccion_envio'),
    path('nueva', views.FormularioDir, name='formulariodir'),
    path('editar/<int:pk>', views.ActualizarDireccionEnvio.as_view(), name='update_direccion_envio'),
    path('eliminar/<int:pk>', views.EliminarDireccionEnvio.as_view(), name='remove_direccion_envio'),
]