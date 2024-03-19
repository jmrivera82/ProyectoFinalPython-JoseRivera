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

##### ----------- Busqueda

@login_required
def busquedaJuegos(request):
    return render(request,"AppProyecto/busquedaJuegos.html")



@login_required
def buscar(request):
        
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        juegos = Juegos.objects.filter(nombre__icontains=nombre)
        
        return render(request, "AppProyecto/juegos.html",{"juegos":juegos})

    else:
        respuesta = "No ingresaste nada"
    return render(request,"AppProyecto/inicio.html",{"respuesta":respuesta})

##### ----------- Consolas 

def consolas (request):
    return render (request, "AppProyecto/consolas.html")


@login_required
def leerConsolas(request):
    consolas = Consolas.objects.all()
    contexto = {"consolas":consolas}
    return render(request,"AppProyecto/consolas.html",contexto)



def formularioConsolas(request):
    if request.method == 'POST':
        miFormulario = consolasFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
		    
            consola = Consolas(nombre=informacion['nombre'],
            año_lanzamiento=informacion['año_lanzamiento'],empresa=informacion['empresa'])
		    
            consola.save()

            consolas = Consolas.objects.all()
    
            return render(request,"AppProyecto/consolas.html",{"consolas":consolas})

    else:
        miFormulario = consolasFormulario()
    return render(request, "AppProyecto/formularioConsolas.html",{"miFormulario":miFormulario})



def editarConsolas(request,consola_nombre):

    consolas = Consolas.objects.get(nombre = consola_nombre)

    if request.method == 'POST':
        miFormularioConsolas = consolasFormulario(request.POST)
        print(miFormularioConsolas)

        if miFormularioConsolas.is_valid:
            
            informacion = miFormularioConsolas.cleaned_data
		    
            consolas.nombre=informacion['nombre']
            consolas.año_lanzamiento=informacion['año_lanzamiento']
            consolas.empresa=informacion['empresa']
		    
            consolas.save()
            
            return render(request, "AppProyecto/inicio.html")

    else:
        miFormularioConsolas= consolasFormulario(initial={'nombre': consolas.nombre, 'año_lanzamiento': consolas.año_lanzamiento , 
            'empresa': consolas.empresa }) 
    
    return render(request, "AppProyecto/editarConsolas.html", {"miFormularioConsolas": miFormularioConsolas, "consola_nombre":consola_nombre})


def eliminarConsola(request,consola_nombre):
    consolas = Consolas.objects.get(nombre=consola_nombre)
    consolas.delete()
    consolas = Consolas.objects.all()
    contexto ={"consolas":consolas}
   # return render(request,"AppProyecto/juegos.html",{"mensaje":"EL juego ha sido eliminado"})
    return render(request,"AppProyecto/consolas.html",contexto)

def acercademi (request):
    return render (request, "AppProyecto/acercademi.html")

def logout (request):
   return render (request, "AppLogin/logout.html")