from django.contrib import admin
from django.urls.conf import include
from products.views import ProductListView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
