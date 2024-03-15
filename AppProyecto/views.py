from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.


def inicio (request):
   return render (request, "AppProyecto/inicio.html")

def login (request):
   return render (request, "AppLogin/login.html")

def registro (request):
   return render (request, "AppLogin/registro.html")

def editarUsuario (request):
   return render (request, "AppLogin/editarUsuario.html")

def juegos (request):
    return render (request, "juegos.html")






def acercademi (request):
    return render (request, "AppProyecto/acercademi.html")

def logout (request):
   return render (request, "AppLogin/logout.html")