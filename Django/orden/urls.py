from django.urls import path
from. import views


urlpatterns = [
    path('', views.orden, name='orden'),
    path('direccion', views.direccion, name='direccion'),
    path('seleccionar/direccion', views.select_direccion, name='select_direccion'),
    path('establecer/direccion/<int:pk>', views.check_direccion, name='check_direccion'),
    path('confirmacion', views.confirmacion, name='confirmacion'),
    path('cancelar', views.cancelar_orden, name='cancelar'),
    path('completado', views.completado_orden, name='completado'),
    path('completados', views.OrdenView.as_view(), name='completados'),
]