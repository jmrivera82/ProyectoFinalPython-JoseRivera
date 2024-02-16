from django.shortcuts import render
from django.http import HttpResponse
from .views import *
from appcoder.models import Curso

# Create your views here.


def inicio (request):
    return render (request, "appcoder/index.html")

def cursos (request):
    
    cursos = Curso.objects.all()
    
    return render (request, "appcoder/cursos.html", {"Curso":cursos}  )  

def profesores (request):
    return render (request, "appcoder/profesores.html")

def estudiantes (request):
    return render (request, "appcoder/estudiantes.html")

def entregables (request):
    return render (request, "appcoder/entregables.html")

