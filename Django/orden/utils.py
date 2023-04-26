from .models import Orden


def funcionOrden(cart, request):    
    orden = cart.orden

    if orden is None and request.user.is_authenticated:
        orden = Orden.objects.create(cart=cart, user=request.user) 

    if orden:
        request.session['orden_id'] = orden.id

    return orden



