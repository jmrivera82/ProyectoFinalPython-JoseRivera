from django.shortcuts import render

# Create your views here.


def inicio (request):
    return render (request, "AppProyecto/inicio.html")

def login (request):
    return render (request, "../AppLogin/login.html")


def equipos (request):
    return render (request, "AppProyecto/equipos.html")

def camisetas (request):
    return render (request, "AppProyecto/camisetas.html")


def acercademi (request):
    return render (request, "AppProyecto/Acercademi.html")

def logout (request):
    return render (request, "../AppLogin/logout.html")