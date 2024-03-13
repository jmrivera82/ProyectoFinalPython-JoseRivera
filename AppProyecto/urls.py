from django.contrib import admin
from django.urls import path

from AppProyecto import views 

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('AppLogin/login.html', views.login, name="login"),
    path('AppLogin/logout.html', views.logout, name="logout"),
    path('Equipos', views.equipos, name="equipos"),
    path('Camisetas', views.camisetas, name="camisetas"),
    path('Acercademi', views.acercademi, name="acercademi"),




]
