from django.shortcuts import render
from .models import Cart

# Create your views here.

def cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id=cart_id).first()

    if cart is None:
        cart = Cart.objects.create(user=user)
    
    if user and cart.user is None:
        cart.user = user
        cart.save()
    
    request.session['cart_id'] = cart.id
    
    return render(request, 'cart/cart.html',{}) 