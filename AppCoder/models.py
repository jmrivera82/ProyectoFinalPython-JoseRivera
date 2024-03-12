
# Create your models here.
from django.db import models

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




class Curso(models.Model):

    nombre = models.CharField(max_length = 40)
    camada = models.IntegerField()

    def __str__ (self):

	    return f"Nombre: {self.nombre} - Camada { self.camada}"


class Estudiante(models.Model):

    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField()

    def __str__ (self):

	    return f"Nombre: {self.nombre} - Apellido { self.apellido} - Email {self.email}"



class Profesor  (models.Model):

    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField()
    profesion = models.CharField(max_length = 40)

    def __str__ (self):

	    return f"Nombre: {self.nombre} - Apellido { self.apellido} - Email {self.email} - Profesión {self.profesion}"


#def __str__ (self):

#	    return f"Nombre: {self.nombre} - Apellido { self.apellido} - Email {self.email} - Profesión {self.profesion}"

class Entregable(models.Model):

    nombre = models.CharField(max_length = 40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__ (self):

	    return f"Nombre: {self.nombre} - fechaDeEntrega { self.fechaDeEntrega} - entregado {self.entregado}"


class CursoList (ListView):
      
      model = Curso
      template_name = "AppCoder/cursos_list.html"

class CursoDetalle (DetailView):
      
      model = Curso
      template_name = "AppCoder/cursos_detalle.html"


class CursoCreacion (CreateView):
      
      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre','camada']

class CursoUpdate (UpdateView):
      
      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre','camada']

class CursoDelete (DeleteView):
      
      model = Curso
      success_url = "/AppCoder/curso/list"
 