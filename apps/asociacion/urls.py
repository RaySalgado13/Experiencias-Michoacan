# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.asociacion import views

urlpatterns = [

    # The home page
    path("", views.index, name='index'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("empresas/", views.empresas, name='empresas'),
    path("empresas/create/", views.empresasC, name='empresasC'),
    path("empresas/edit/", views.empresasE, name='empresasE'),
    path("empresas/eliminar/", views.empresasD, name='empresasD'),
    path("reportes/", views.reportes, name='reportes'),
    
    
]
