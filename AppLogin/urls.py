from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import * 

urlpatterns = [
    path('login',login_request, name="login"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('registro',registro, name="registro"),
    path('editarPerfil', editarPerfil, name="EditarPerfil"),



]