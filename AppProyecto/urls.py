from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import *



urlpatterns = [
    path('', inicio, name="inicio"),
    path('../AppLogin/login.html', login, name="login"),
    path('../AppLogin/logout.html', logout, name="logout"),
    path('../AppLogin/registro.html', registro, name="registro"),
    path('../AppLogin/editarUsuario.html', editarUsuario, name="registro"),

    path('juegos', juegos, name="juegos"),
    #path('agregar_equipo', agregar_equipo, name="agregar_equipo"),
   # path('equipos/listado', views.EquiposListado.as_view(), name='List'),


    #path('Camisetas', camisetas, name="camisetas"),
    path('Acercademi', acercademi, name="acercademi"),




]
