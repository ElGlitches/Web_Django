from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from cart.funciones import funcionCarrito, funcionEliminarCart
from .utils import funcionEliminarOrden, funcionOrden
from .utils import funcionbreadcrumb
from .models import Orden
from DirEnvio.models import DireccionEnvio
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models.query import EmptyQuerySet
from .decorador import validar_cart_and_orden



# Create your views here.
class OrdenView(LoginRequiredMixin, ListView):
        login_url = 'login'
        template_name = 'orden/ordenes.html'

        def get_queryset(self):
            return self.request.user.ordenes_completadas()

@login_required(login_url='login')
@validar_cart_and_orden
def orden(request, cart, orden):

    return render(request, 'orden/orden.html',{
        'cart':cart,
        'orden':orden,
        'breadcrumb':funcionbreadcrumb()

    })

@login_required(login_url='login')
@validar_cart_and_orden
def direccion(request,cart, orden):

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
@validar_cart_and_orden
def check_direccion(request,cart, orden,pk):

    direccion_envio = get_object_or_404(DireccionEnvio,pk=pk)

    if request.user.id != direccion_envio.user.id:
        return redirect('index')
    
    orden.update_direction_envio(direccion_envio)
    return redirect('direccion')

@login_required(login_url='login')
@validar_cart_and_orden
def confirmacion(request, cart, orden):
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
@validar_cart_and_orden
def cancelar_orden(request,cart, orden):
    if request.user.id!= orden.user.id:
        return redirect('index')

    orden.cancelar()
    funcionEliminarCart(request)
    funcionEliminarOrden(request)

    messages.error(request, 'Se ha cancelado la orden')
    return redirect('index')

@login_required(login_url='login')
@validar_cart_and_orden
def completado_orden(request,cart, orden):
    if request.user.id!= orden.user.id:
        return('index')
    
    orden.completado()
    funcionEliminarCart(request)
    funcionEliminarOrden(request)

    messages.success(request, 'Se ha completado la orden')
    return redirect('index')

