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
    path('buscar/',buscar,name='buscar'),


    path('consolas', consolas, name="consolas"),
    path('leerConsolas',leerConsolas,name='leerConsolas'),
    path('formularioConsolas',formularioConsolas,name='formularioConsolas'),
    path('eliminarConsola/<consola_nombre>/',eliminarConsola,name='eliminarConsola'),
    path('editarConsolas/<consola_nombre>/',editarConsolas,name='editarConsolas'),

    path('Acercademi', acercademi, name="acercademi"),




]
