
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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
    

