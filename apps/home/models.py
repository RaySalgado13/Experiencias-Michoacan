# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from distutils.archive_util import make_zipfile
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Imagen(models.Model):
    image = models.FileField(null=False, blank = False)
    date_uploaded = models.DateTimeField(auto_now_add=True)


class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio = models.IntegerField()
    fecha_inicio = models.DateTimeField(blank = True, null=True)
    fecha_fin = models.DateTimeField(blank = True, null=True)
    stock = models.IntegerField()
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    tipo = models.ForeignKey('Tipo_producto' , on_delete=models.CASCADE)
    imagen = models.ManyToManyField(Imagen)

    def __str__(self):
        return f"{self.nombre}  {self.descripcion[0:50]}"

class Empresa(models.Model):
    nombre_legal = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=250, blank = True)
    email = models.EmailField(max_length=250)
    rfc = models.CharField(max_length=15)
    telefono = models.CharField(max_length=10)
    representante = models.CharField(max_length=200)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre_legal
    

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=10)
    numero_interior = models.CharField(max_length=10, blank = True)
    colonia = models.CharField(max_length=100)
    cp = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.calle[0:50]} {self.numero_exterior} {self.cp}"


class Tipo_producto(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo
    

class Reservacion(models.Model):
    folio = models.CharField(max_length=250)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, blank = True)
    telefono = models.CharField(max_length=10, blank = True)
    fecha = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=50)
    producto = models.ManyToManyField(Producto)

    def __str__(self) -> str:
        return self.folio

class Reporte(models.Model):
    titulo = models.CharField(max_length=250)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    monto_total = models.IntegerField()
    items = models.JSONField()
    tipo = models.ForeignKey('Tipo_reporte', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo}"

class Tipo_Reporte(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo
    


