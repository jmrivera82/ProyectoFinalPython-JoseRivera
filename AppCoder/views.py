from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso, Entregable, Profesor, Estudiante

from AppCoder.forms import *

# Create your views here.

def inicio (request):
    return render (request, "AppCoder/inicio.html")


def cursos (request):
    return render (request, "AppCoder/cursos.html")


def profesores (request):
    return render (request, "AppCoder/profesores.html")


def estudiantes (request):
    return render (request, "AppCoder/estudiantes.html")


def entregables (request):
    return render (request, "AppCoder/entregables.html")


def cursos(request):

    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            curso = Curso (nombre = informacion ["curso"], camada = informacion ['camada'])

            curso.save()

            return render (request, "AppCoder/inicio.html")
    
    else:
        
        miFormulario = CursoFormulario()

    return render (request, "AppCoder/cursos.html", {"miFormulario":miFormulario })

#profesor

def profesorFormulario(request):

    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            profesor = Profesor (nombre = informacion ["nombre"], apelliido = informacion ['apellido'], email = informacion ['email'], profesion = informacion ['profesion'])

            profesor.save()

            return render (request, "AppCoder/inicio.html")
    
    else:
        
        miFormulario = ProfesorFormulario()

    return render (request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario })


#entregable

def entregableFormulario(request):

    if request.method == "POST":

        miFormulario = EntregableFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            entregable = Entregable (nombre = informacion ["nombre"], fechaDeEntrega = informacion ['fechaDeEntrega'], entregado = informacion ['entregado'])
      
            entregable.save()

            return render (request, "AppCoder/inicio.html")
    
    else:
        
        miFormulario = EntregableFormulario()

    return render (request, "AppCoder/entregableFormulario.html", {"miFormulario":miFormulario })


#estudiante

def estudianteFormulario(request):

    if request.method == "POST":

        miFormulario = EstudianteFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            estudiante = Estudiante (nombre = informacion ["nombre"], apelliido = informacion ['apellido'], email = informacion ['email'])    
            estudiante.save()

            return render (request, "AppCoder/inicio.html")
    
    else:
        
        miFormulario = EstudianteFormulario()

    return render (request, "AppCoder/estudianteFormulario.html", {"miFormulario":miFormulario })

def busquedaCamada (request):
    return render(request,"AppCoder/busquedaCamada.html")


def buscar (request):

    if request.GET("camada"):

        camada = request.GET ['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render (request, "AppCoder/resultadobusqueda.html",{"curso":cursos ,"camada":camada})

    else:

        respuesta = "No enviaste datos"
    
    #return HttpResponse(respuesta)
    return render (request, "AppCoder/inicio.html",{"respuesta" : respuesta})

