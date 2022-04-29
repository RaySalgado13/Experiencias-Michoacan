# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Producto, Empresa, Direccion, Tipo_producto,Imagen,Reservacion,Tipo_Reporte,Reporte

# Register your models here.
admin.site.register(Producto)
admin.site.register(Empresa)
admin.site.register(Tipo_producto)
admin.site.register(Imagen)
admin.site.register(Reservacion)
admin.site.register(Tipo_Reporte)
admin.site.register(Reporte)
admin.site.register(Direccion)
