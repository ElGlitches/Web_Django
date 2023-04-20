from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import Registro
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html',{
        'mensaje': 'Ingreso',
        'titulo': 'Personas',
        'personas':[
            {'titulo':'Maria','Edad':18,'adulto':True },
            {'titulo':'Jose','Edad':2,'adulto':False },
            {'titulo':'Juan','Edad':43,'adulto':True },
            {'titulo':'Rosa','Edad':8,'adulto':False }
        ]})

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
            return redirect('index')
        else:
            messages.error(request, 'Datos incorrectos')

    return render(request, 'users/login.html',{})

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
