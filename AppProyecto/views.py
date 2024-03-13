from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.


def inicio (request):
   return render (request, "AppProyecto/inicio.html")

def login (request):
   return render (request, "AppLogin/login.html")


def equipos (request):
    return render (request, "equipos.html")

@login_required   
def agregar_equipo(request):
    if request.method == 'POST':
        miFormulario = EquiposFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            equipo = Equipos(nombre=informacion.POST['nombre'], pais=informacion.POST['pais'], año=informacion.POST['año'], campaña=informacion.POST['campaña'])
            equipo.save()
            return render(request, "inicio.html", {"mensaje": "Se agrego el equipo {{nombre}} a la lista"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        miFormulario = EquiposFormulario()
        return render(request, "agregar_equipo.html", {"miFormulario": miFormulario})



def camisetas (request):
    return render (request, "camisetas.html")


def acercademi (request):
    return render (request, "AppProyecto/acercademi.html")

def logout (request):
   return render (request, "AppLogin/logout.html")