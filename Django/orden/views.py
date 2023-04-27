from django.shortcuts import render
from cart.funciones import funcionCarrito
from .utils import funcionOrden
from .utils import funcionbreadcrumb
from .models import Orden
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def orden(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart,request)

    return render(request, 'orden/orden.html',{
        'cart':cart,
        'orden':orden,
        'breadcrumb':funcionbreadcrumb()

    })
