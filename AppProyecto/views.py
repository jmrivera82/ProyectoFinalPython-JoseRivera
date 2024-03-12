from django.shortcuts import render
from django.http import HttpResponse

from AppProyecto.models import *

from AppProyecto.forms import *

# Create your views here.

def inicio (request):
    return render (request, "AppProyecto/inicio.html")



#profesor

def discos(request):

    if request.method == "POST":

        miFormulario = DiscosFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            discos = Discos (nombre = informacion ["nombre"], banda = informacion ['banda'], año = informacion ['año'], genero = informacion ['genero'])

            discos.save()

            return render (request, "AppProyecto/inicio.html")
    
    else:
        
        miFormulario = DiscosFormulario()

    return render (request, "AppProyecto/discos.html", {"miFormulario":miFormulario })


def bandas(request):

    if request.method == "POST":
        miFormulario = BandasFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            bandas = Bandas (nombre = informacion ["nombre"], genero = informacion ['genero'])

            bandas.save()

            return render (request, "AppProyecto/inicio.html")
    
    else:
        
        miFormulario = BandasFormulario()

    return render (request, "AppProyecto/bandas.html", {"miFormulario":miFormulario })