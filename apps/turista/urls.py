# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.turista import views

urlpatterns = [

    # The home page
    path("", views.index, name='index_t'),
    path("catalogo/", views.catalogo, name='catalogo-turista'),
    path("detalles/<int:id_producto>/", views.detalles, name='detalles'),
    path("compra_inmediata/", views.compra_inmediata, name='compra_inmediata'),
    path("carrito/", views.carrito, name='carrito'),
    path("checkout/", views.checkout, name='checkout'),
    
    
]
