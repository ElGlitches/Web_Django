from django.shortcuts import render
from django.http import JsonResponse
from .models import PromoCodigo
from orden.decorador import validar_cart_and_orden

# Create your views here.

@validar_cart_and_orden
def validar(request, cart, orden):
        codigo = request.GET.get('code')
        promo_codigo = PromoCodigo.objects.get_validar(codigo)

        if promo_codigo is None:
            return JsonResponse({
                'status': False,
            },   status= 404)
        
        orden.aplicarCodigo(promo_codigo)

        return JsonResponse({
            'status': True,
            'codigo': promo_codigo.codigo,
            'descuento': promo_codigo.descuento,
            'total': orden.total
            })