from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def validar(request):
    responseData = {
        "id": 1,
        'nombre': 'Gonzalo',
        'role': ['Administrador', 'usuario']
    }

    return JsonResponse(responseData)