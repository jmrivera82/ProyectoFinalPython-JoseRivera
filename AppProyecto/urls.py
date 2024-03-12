from django.urls import path

from AppProyecto import views

urlpatterns = [


    path('', views.inicio, name="inicio"),
    path('discos', views.discos, name="discos"),
    path('bandas', views.bandas, name="bandas"),



]