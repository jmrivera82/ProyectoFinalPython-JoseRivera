from django.db import models
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

# Create your models here.

class camisetas(models.Model):

    nombre = models.CharField(max_length = 40)
    pais = models.CharField(max_length = 40)
    año = models.EmailField()

    def __str__ (self):

	    return f"Nombre: {self.nombre} - Pais { self.pais} - Año {self.año}"



class Equipos  (models.Model):

    nombre = models.CharField(max_length = 40)
    pais = models.CharField(max_length = 40)
    año = models.IntegerField
    campaña = models.CharField(max_length = 40)

    def __str__ (self):

	    return f"Nombre: {self.nombre} - Pais { self.pais} - Año {self.año} - Campaña {self.campaña}"
    
@login_required   
class EquiposListado (ListView):
      
      model = Equipos
      template_name = "AppProyecto/equipos_listado.html"