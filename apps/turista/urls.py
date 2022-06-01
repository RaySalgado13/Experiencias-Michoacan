# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.turista import views

urlpatterns = [

    # The home page
    path("", views.index, name='index_t'),
    path("catalogo/", views.catalogo, name='catalogo'),
    path("detalles/<int:id_producto>/", views.detalle, name='detalles'),
    path("compra_inmediata/", views.compra_inmediata, name='compra_inmediata'),
    path("carrito/", views.carro_detalle, name='carro'),
    path('add/<int:producto_id>/', views.carro_add, name='carro_add'),
    path('eliminar/<int:producto_id>/', views.carro_remover, name='carro_remover'),
    path("checkout/", views.reser_create, name='checkout'),
    

    
    
    
]
