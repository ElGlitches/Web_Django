from .models import Orden
from django.urls import reverse


def funcionOrden(cart, request):    
    orden = cart.orden

    if orden is None and request.user.is_authenticated:
        orden = Orden.objects.create(cart=cart, user=request.user) 

    if orden:
        request.session['orden_id'] = orden.id

    return orden

def funcionbreadcrumb(products=True, address=False, payment=False, confirmation=False):
    return [
        {'title':'Productos', 'active':products, 'url':reverse('orden')},
        {'title':'Direccion', 'active':address, 'url':reverse('direccion')},
        {'title':'Pago', 'active':payment, 'url':reverse('orden')},
        {'title':'Confirmacion', 'active':confirmation, 'url':reverse('orden')},
    ]

