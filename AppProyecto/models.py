from django.db import models

# Create your models here.

class Discos  (models.Model):

    nombre = models.CharField(max_length = 40)
    banda = models.CharField(max_length = 40)
    año = models.IntegerField()
    genero = models.CharField(max_length = 20)

    def __str__ (self):

	    return f"Nombre: {self.nombre} - Banda { self.banda} - Año {self.año} - Genero {self.genero}"
    

class Bandas(models.Model):

    nombre = models.CharField(max_length = 40)
    genero = models.CharField(max_length = 40)

    def __str__ (self):

	    return f"Nombre: {self.nombre} - Genero { self.genero}"