from django.contrib import admin
from django.urls import path

from .views import *

from AppProyecto import views


urlpatterns = [
    path('', inicio, name="inicio"),
    path('../AppLogin/login.html', login, name="login"),
    path('../AppLogin/logout.html', logout, name="logout"),
    path('equipos', equipos, name="equipos"),
    path('agregar_equipo', agregar_equipo, name="agregar_equipo"),
   # path('equipos/listado', views.EquiposListado.as_view(), name='List'),


    path('Camisetas', camisetas, name="camisetas"),
    path('Acercademi', acercademi, name="acercademi"),




]
