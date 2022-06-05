# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.empresas import views

urlpatterns = [

    # The home page
    path("", views.index, name='empresas'),
    path("dashboard/", views.dashboard, name='dashboard_empresas'),
    path("experiencias/", views.experiencias, name='experiencias-empresas'),
    path("experiencias/create/", views.experienciasCreate, name='experiencias-create'),
    path("experiencias/edit/<int:id_experiencia>", views.experienciasEdit, name='experiencias-edit'),    
    path("experiencias/delete_img/<int:id_img>", views.experiencias_imgDelete, name='experiencias_img-delete'),
    path("experiencias/delete/<int:id_experiencia>", views.experienciasD, name='experiencias-delete'),
    path("paquetes/", views.paquetes, name='experiencias-paquetes'),
    path("paquetes/create/", views.paquetesCreate, name='paquetes-create'),
    path("paquetes/edit/<int:id_paquete>", views.paquetesEdit, name='paquetes-edit'),
    path("paquetes/delete/<int:id_paquete>", views.paquetesD, name='paquetes-delete'),
    path("reservaciones/", views.reservaciones, name='reservaciones-empresas'),
    path("reservaciones/edit/<int:id_reservacion>", views.reservacionesE, name='reservaciones-edit'),
    path("reservaciones/eliminar/<int:id_reservacion>", views.reservacionesD, name='reservaciones-delete'),
    path("reportes/", views.reportes, name='reportes-empresas'),
    path("correo/", views.correo, name='correo'),
     
     
]
