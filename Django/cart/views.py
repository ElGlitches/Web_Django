from django.shortcuts import render
from .models import Cart
from .funciones import funcionCarrito
from products.models import Product

# Create your views here.

def cart(request):
    cart = funcionCarrito(request) 
    
    return render(request, 'cart/cart.html',{}) 

def add(request):
    cart = funcionCarrito(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.product.add(product)

    return render(request, 'cart/add.html',{
        'product' : product
        })