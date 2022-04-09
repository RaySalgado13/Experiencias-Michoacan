# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from distutils.archive_util import make_zipfile
from django.db import models
from django.contrib.auth.models import User
from itsdangerous import json

# Create your models here.

class Producto(models.Model):

    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio = models.IntegerField()
    fecha_inicio = models.DateTimeField(blank = True)
    fecha_fin = models.DateTimeField(blank = True)
    stock = models.IntegerField()
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    tipo = models.ForeignKey('Tipo_producto' , on_delete=models.CASCADE)

class Empresa(models.Model):

    id = models.IntegerField(primary_key=True)
    nombre_legal = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=250, blank = True)
    email = models.EmailField(max_length=250)
    rfc = models.CharField(max_length=15)
    telefono = models.CharField(max_length=10)
    representante = models.CharField(max_length=200)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE) 

class Direccion(models.Model):

    id = models.IntegerField(primary_key=True)
    calle = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=10)
    numero_interior = models.CharField(max_length=10, blank = True)
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


class Reservacion(models.Model):

    id = models.IntegerField(primary_key=True)
    folio = models.CharField(max_length=250)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, blank = True)
    telefono = models.CharField(max_length=10, blank = True)
    fecha = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=50)
    producto = models.ManyToManyField(Producto)

class Reporte(models.Model):

    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=250)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    monto_total = models.IntegerField()
    items = models.JSONField()
    tipo = models.ForeignKey('Tipo_reporte', on_delete=models.CASCADE)

class Tipo_Reporte(models.Model):

    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)


