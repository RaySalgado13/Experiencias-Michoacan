# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.empresas import views

urlpatterns = [

    # The home page
    path("", views.index, name='empresas'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("experiencias/", views.experiencias, name='experiencias'),
    path("experiencias/create/", views.experienciasC, name='create'),
    path("experiencias/edit/", views.experienciasE, name='experienciasE'),
    path("experiencias/delete/", views.experienciasD, name='experienciasD'),
    path("reservaciones/", views.reservaciones, name='reservaciones'),
    path("reservaciones/edit/", views.reservacionesE, name='reservacionesE'),
    path("reservaciones/eliminar/", views.reservacionesD, name='reservacionesD'),
    path("reportes/", views.reportes, name='reportes'),
    path("correo/", views.correo, name='correo'),
     
     
]
