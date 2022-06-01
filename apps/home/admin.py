# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Producto, Empresa, Direccion, Tipo_producto,Imagen,Reservacion,Tipo_Reporte,Reporte

# Register your models here.
class ImagenAdmin(admin.ModelAdmin):
    list_display=( "id" ,)

class ReservacionAdmin(admin.ModelAdmin):
    list_display=( "id" ,)
    

admin.site.register(Producto)
admin.site.register(Empresa)
admin.site.register(Tipo_producto)
admin.site.register(Imagen, ImagenAdmin)
admin.site.register(Reservacion, ReservacionAdmin)
admin.site.register(Tipo_Reporte)
admin.site.register(Reporte)
admin.site.register(Direccion)
