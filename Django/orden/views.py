from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from cart.funciones import funcionCarrito, funcionEliminarCart
from .utils import funcionEliminarOrden, funcionOrden
from .utils import funcionbreadcrumb
from .models import Orden
from DirEnvio.models import DireccionEnvio
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

@login_required(login_url='login')
def direccion(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart,request)

    direccion_envio = orden.get_or_set_DireccionEnvio()
    contDireccionEnvio = request.user.direccionenvio_set.count() >1

    return render(request, 'orden/direccion.html',{
        'cart':cart,
        'orden':orden,
        'direccion_envio':direccion_envio,
        'contDireccionEnvio':contDireccionEnvio,
        'breadcrumb':funcionbreadcrumb(address=True)
    })

@login_required(login_url='login')
def select_direccion(request):
    direccion_envios = request.user.direccionenvio_set.all()
    return render(request,'orden/select_direccion.html',{
        'breadcrumb': funcionbreadcrumb(address=True),
        'direccion_envios': direccion_envios
        })

@login_required(login_url='login')
def check_direccion(request,pk):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart,request)
    direccion_envio = get_object_or_404(DireccionEnvio,pk=pk)

    if request.user.id != direccion_envio.user.id:
        return redirect('index')
    
    orden.update_direction_envio(direccion_envio)
    return redirect('direccion')

@login_required(login_url='login')
def confirmacion(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart,request)
    direccion_envio = orden.direccion_envio
    if direccion_envio is None:
        return redirect ('direccion')
    
    return  render(request, 'orden/confirmacion.html',{
        'cart':cart,
        'orden':orden,
        'direccion_envio':direccion_envio,
        'breadcrumb':funcionbreadcrumb(address=True,confirmation=True)
        })

@login_required(login_url='login')
def cancelar_orden(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart,request)

    if request.user.id!= orden.user.id:
        return redirect('index')

    orden.cancelar()
    funcionEliminarCart(request)
    funcionEliminarOrden(request)

    messages.error(request, 'Se ha cancelado la orden')
    return redirect('index')

