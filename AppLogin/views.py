
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from AppProyecto.models import Avatar

from .forms import *
from .models import *

# Create your views here.



def login_request(request):

    if request.method=='POST':
        miFormulario=AuthenticationFormLogin(request, data=request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            username=informacion["username"]
            password=informacion["password"]
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return render (request, "AppProyecto/inicio.html", {"mensaje":f"Bienvenido Usuario {user}"})
            else:
                return render(request,"AppProyecto/inicio.html", {"mensaje": "Datos invalidos"})
            
        else:
            return render(request,"AppProyecto/inicio.html", {"mensaje": "Formulario invalido"})
    else:
        miFormulario=AuthenticationFormLogin()
        return render (request, "AppLogin/login.html", {"miFormulario":miFormulario})
    

def registro(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UsuarioRegistroForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppProyecto/inicio.html",{"mensaje":"Se ha creado el usuario, por favor hacer ingresar"})
    else:
        form = UsuarioRegistroForm()
        #form = UserCreationForm()
    return render(request,"AppLogin/registro.html",{"form":form})


def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UsuarioEdicionForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password1']            
            usuario.save()
            

            return render(request, "AppProyecto/inicio.html")
    else:

        miFormulario = UsuarioEdicionForm(initial={'email':usuario.email})
    return render(request, "AppLogin/editarUsuario.html",{"miFormulario": miFormulario, "usuario":usuario})

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request,"AppProyecto/inicio.html", {"url":avatares[0].imagen.url})