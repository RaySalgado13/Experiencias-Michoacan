# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.asociacion import views

urlpatterns = [

    # The home page
    path("", views.index, name='index'),
    path("dashboard/", views.dashboard, name='dashboard_asociacion'),
    path("empresas/", views.empresas, name='asociacion_empresas'),
    path("empresas/create/", views.empresasC, name='asociacion_empresas_create'),
    path("empresas/edit/<int:id>/", views.empresasE, name='asociacion_empresas_edit'),
    path("empresas/eliminar/<int:id>/", views.empresasD, name='asociacion_empresas_delete'),
    path("reportes/", views.reportes, name='asociacion_reportes'),
    
    
]   
