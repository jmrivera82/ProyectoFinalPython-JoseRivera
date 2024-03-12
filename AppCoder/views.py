from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import *

from AppCoder.forms import *

# Create your views here.

def inicio (request):
    return render (request, "AppCoder/inicio.html")


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

def profesores(request):

    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            profesor = Profesor (nombre = informacion ["nombre"], apellido = informacion ['apellido'], email = informacion ['email'], profesion = informacion ['profesion'])

            profesor.save()

            return render (request, "AppCoder/inicio.html")
    
    else:
        
        miFormulario = ProfesorFormulario()

    return render (request, "AppCoder/profesores.html", {"miFormulario":miFormulario })


#entregable

def entregables(request):

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

    return render (request, "AppCoder/entregables.html", {"miFormulario":miFormulario })


#estudiante

def estudiantes(request):

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

    return render (request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario })

def busquedaCamada (request):
    return render(request,"AppCoder/busquedaCamada.html")


def buscar (request):

    if request.GET["camada"]:

        camada = request.GET ["camada"]
        curso = Curso.objects.filter(camada=camada) #__icontains

        return render (request, "AppCoder/resultadoBusqueda.html",{"cursos":curso ,"camada":camada})

    else:

        #respuesta = "No enviaste datos"
    
        return HttpResponse("No enviaste datos")
        #return render (request, "AppCoder/inicio.html",{"respuesta" : respuesta})



def leerProfesores(request):

    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores}
    return render (request, "AppCoder/leerProfesores.html", contexto)



def eliminarProfesor(request, profesor_nombre):

    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()

    contexto={"profesores": profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)


def editarProfesor(request, profesor_nombre):

    profesor = Profesor.objects.get (nombre = profesor_nombre)

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion ['apellido']
            profesor.email = informacion ['email']
            profesor.profesion = informacion ['profesion']

            profesor.save ()

            return render(request, "AppCoder/inicio.html")
        
        else:

            miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email': profesor.email,'profesion':profesor.profesion})

            return render (request,"AppCoder/EditarProfesor.html", {"miFormulario":miFormulario,"profesor_nombre":profesor_nombre})
