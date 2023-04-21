from django.contrib import admin
from django.urls.conf import include
from products.views import ProductListView
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name= 'index'),
    path('users/login', views.login, name= 'login'),
    path('users/registro', views.registro, name= 'registro'),
    path('users/salir', views.salir, name= 'salir'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('productos/', include('products.urls')),

]
