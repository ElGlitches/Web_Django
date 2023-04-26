from django.shortcuts import render
from cart.funciones import funcionCarrito
from .utils import funcionOrden
from .models import Orden

# Create your views here.

def orden(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart,request)

    return render(request, 'orden/orden.html',{
        'cart':cart,
        'orden':orden

    })
