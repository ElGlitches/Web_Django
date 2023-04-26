from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Cart
from .funciones import funcionCarrito
from products.models import Product


# Create your views here.


def cart(request):
    cart = funcionCarrito(request) 
    
    return render(request, 'cart/cart.html', {
        'cart': cart
    }) 

def add(request):
    cart = funcionCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity = request.POST.get('quantity', 1)

    cart.products.add(product, through_defaults={
        'quantity' : quantity
    })

    return render(request, 'cart/add.html',{
        'product': product
        })

def remove(request):
    cart = funcionCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    cart.products.remove(product)

    return redirect('cart')