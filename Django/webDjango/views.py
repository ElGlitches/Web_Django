from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import Registro
from users.models import User
from products.models import Product
from django.http import HttpResponseRedirect




def index(request):
    productos = Product.objects.all()
    return render(request, 'index.html',{
        'mensaje': 'Tienda',
        'titulo': 'Inicio de tienda',
        'productos': productos,
        })

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuarios = authenticate(username = username, password = password)
        if usuarios:
            lg(request, usuarios)
            messages.success(request, f'Bienvenido {usuarios.username}')
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])
            
            return redirect('index')
        else:
            messages.error(request, 'Datos incorrectos')

    return render(request, 'users/login.html',{

    })

def salir(request):
    logout(request)
    messages.success(request,'Se ha cerrado la sesion')
    return redirect(login)

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = Registro(request.POST or None)
    if request.method=='POST' and form.is_valid():

        usuario = form.save()
        if usuario:
            lg(request, usuario)
            messages.success(request, 'Bienvenido')
            return redirect('index')


    return render(request,'users/registro.html',{
        'form':form

    })
