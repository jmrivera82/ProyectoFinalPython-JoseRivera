<<<<<<< HEAD
"""PreEntrega3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
=======
"""
URL configuration for PreEntrega3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
>>>>>>> 7257918ca46c72486c0fddbdc23889a987ea7523
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path



=======
from django.urls import path, include
>>>>>>> 7257918ca46c72486c0fddbdc23889a987ea7523


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('AppCoder/', include('AppCoder.urls')),
    
    ]
=======
    path('appcoder/', include ("appcoder.urls"))
]
>>>>>>> 7257918ca46c72486c0fddbdc23889a987ea7523
