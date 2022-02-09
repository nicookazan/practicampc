"""practicampc URL Configuration

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

from computadoras.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='index'),
    path('nueva_pc', nuevaPC),
    path('detalle_compu/<int:id>', detalle_compu),
    path('editar_compu/<int:id>', editar_compu),
    path('eliminar_compu/<int:id>', eliminar_compu),
    path('monitores', carga_mon, name='mon'),
    path('teclados', carga_tec, name='tec'),
    path('ratones', carga_rat, name='rat'),
    path('nuevo_monitor', nuevo_monitor),
    path('detalle_monitor/<int:id>', detalle_mon),
    path('editar_monitor/<int:id>', editar_mon),
    path('eliminar_monitor/<int:id>', eliminar_mon),
    path('nuevo_tec', nuevo_tec),
    path('detalle_tec/<int:id>', detalle_tec),
    path('editar_tec/<int:id>', editar_tec),
    path('eliminar_tec/<int:id>', eliminar_tec),
    path('nuevo_raton', nuevo_raton),
    path('detalle_raton/<int:id>', detalle_raton),
    path('editar_raton/<int:id>', editar_raton),
    path('eliminar_raton/<int:id>', eliminar_raton)

]
