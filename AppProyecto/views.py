from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

##### ----------- Login (AppLogin) 

def inicio (request):
   return render (request, "AppProyecto/inicio.html")

def login (request):
   return render (request, "AppLogin/login.html")

def registro (request):
   return render (request, "AppLogin/registro.html")

def editarUsuario (request):
   return render (request, "AppLogin/editarUsuario.html")

##### ----------- Juegos 

def juegos (request):
    return render (request, "AppProyecto/juegos.html")

@login_required
def leerJuegos(request):
    juegos = Juegos.objects.all()
    contexto = {"juegos":juegos}
    return render(request,"AppProyecto/juegos.html",contexto)



def formularioJuegos(request):
    if request.method == 'POST':
        miFormulario = juegosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
		    
            juego = Juegos(nombre=informacion['nombre'],
            año=informacion['año'],genero=informacion['genero'],
            consola=informacion['consola'])
		    
            juego.save()

            juegos = Juegos.objects.all()
    
            return render(request,"AppProyecto/juegos.html",{"juegos":juegos})

    else:
        miFormulario = juegosFormulario()
    return render(request, "AppProyecto/formularioJuegos.html",{"miFormulario":miFormulario})



def editarJuegos(request,juego_nombre):

    juegos = Juegos.objects.get(nombre = juego_nombre)

    if request.method == 'POST':
        miFormularioJuegos = juegosFormulario(request.POST)
        print(miFormularioJuegos)

        if miFormularioJuegos.is_valid:
            
            informacion = miFormularioJuegos.cleaned_data
		    
            juegos.nombre=informacion['nombre']
            juegos.año=informacion['año']
            juegos.genero=informacion['genero']
            juegos.consola=informacion['consola']
		    
            juegos.save()
            
            return render(request, "AppProyecto/inicio.html")

    else:
        miFormularioJuegos= juegosFormulario(initial={'nombre': juegos.nombre, 'año': juegos.año , 
            'genero': juegos.genero, 'consola':juegos.consola }) 
    
    return render(request, "AppProyecto/editarJuegos.html", {"miFormularioJuegos": miFormularioJuegos, "juego_nombre":juego_nombre})


def eliminarJuego(request,juego_nombre):
    juegos = Juegos.objects.get(nombre=juego_nombre)
    juegos.delete()
    juegos = Juegos.objects.all()
    contexto ={"juegos":juegos}
   # return render(request,"AppProyecto/juegos.html",{"mensaje":"EL juego ha sido eliminado"})
    return render(request,"AppProyecto/juegos.html",contexto)


@login_required
def busquedaJuegos(request):
    return render(request,"AppProyecto/busquedaJuegos.html")

def acercademi (request):
    return render (request, "AppProyecto/acercademi.html")

def logout (request):
   return render (request, "AppLogin/logout.html")