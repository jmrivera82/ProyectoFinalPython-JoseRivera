from django.db import models

from django.contrib.auth.models import User

from django.forms import ImageField

from distutils.command.upload import upload

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

# Create your models here.

class Juegos(models.Model):

    nombre = models.CharField(max_length = 40, unique=True) 
    año = models.EmailField()
    genero = models.CharField(max_length = 40)
    consola = models.CharField(max_length = 40)

    def __str__ (self):

	    return f"Nombre: {self.nombre} - Año {self.año} - Genero { self.genero}- Consola { self.consola}"



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True, blank = True)