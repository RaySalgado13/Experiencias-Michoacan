# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from distutils.archive_util import make_zipfile
from django.db import models
from django.contrib.auth.models import User
from itsdangerous import json

# Create your models here.

class Productos(models.Model):

    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    stock = models.IntegerField()
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    tipo = models.ForeignKey('Tipo_producto' , on_delete=models.CASCADE)

class Empresa(models.Model):

    id = models.IntegerField(primary_key=True)
    nombre_legal = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    rfc = models.CharField(max_length=15)
    telefono = models.CharField(max_length=10)
    representante = models.CharField(max_length=200)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE) 

class Direccion(models.Model):

    id = models.IntegerField(primary_key=True)
    calle = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=10)
    numero_interior = models.CharField(max_length=10)
    colonia = models.CharField(max_length=100)
    cp = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)


class Tipo_producto(models.Model):

    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)

class Imagenes(models.Model):

    id = models.IntegerField(primary_key=True)
    enlace = models.TextField()
    producto = models.ForeignKey('Producto' , on_delete=models.CASCADE) 

class Reservacion_has_productos(models.Model):

    id_reservacion = models.ForeignKey('Reservacion', on_delete=models.CASCADE)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)

class Reservacion(models.Model):

    id = models.IntegerField(primary_key=True)
    folio = models.CharField(max_length=250)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    telefono = models.CharField(max_length=10)
    fecha = models.DateField()
    status = models.CharField(max_length=50)

class Reporte(models.Model):

    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=250)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_total = models.IntegerField()
    items = models.JSONField()
    tipo = models.ForeignKey('Tipo_reporte', on_delete=models.CASCADE)

class Tipo_Reporte(models.Model):

    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)


