from django.shortcuts import render
from .productos import productos

def mostrar_principal(request):
    contexto = {
        'tiendita': productos
    }
    return render(request, 'principal.html', contexto)

def mostrar_iniciosesion(request):
    return render(request,'iniciosesion.html',{})

def mostrar_contacto(request):
    return render(request,'contacto.html',{})