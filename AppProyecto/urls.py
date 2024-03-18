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
    path('leerJuegos',leerJuegos,name='leerJuegos'),
    path('formularioJuegos',formularioJuegos,name='formularioJuegos'),
    path('eliminarJuego/<juego_nombre>/',eliminarJuego,name='eliminarJuego'),
    path('editarJuegos/<juego_nombre>/',editarJuegos,name='editarJuegos'),
    path('busquedaJuegos',busquedaJuegos,name='busquedaJuegos'),

    path('Acercademi', acercademi, name="acercademi"),




]
