"""prueba3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from vacunatorio import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('ingresar/',views.ingresar),
    path('ingresar_informacion/',views.ingresar_informacion),
    path('listar/',views.listar),
    path('listar_informacion/',views.listar_informacion),
    path('buscar/',views.buscador),
    path('buscador/',views.buscar),
    path('ingreso_vacuna/',views.ingreso_vacuna),
    path('vacuna_ingresada/',views.datos_vacuna),
    path('listar_vacuna/',views.listar_vacuna),
    path('listar_vacunas/',views.listar_vacunas),
    path('actualizar_vacuna/',views.actualizar_vacuna),
    path('modificar/',views.modificar),
    path('eliminar_vacuna/',views.eliminar_vacuna),
    path('eliminacion_vacuna/',views.eliminacion_vacuna),
    path('busca_vacunas/',views.buscar_vacuna),
    path('buscador_vacunas/',views.buscar_vacunas),
]

urlpatterns += staticfiles_urlpatterns()