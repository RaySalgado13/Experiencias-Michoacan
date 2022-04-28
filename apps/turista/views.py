from django.http import HttpResponse
from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse




# Create your views here.
def index(request):
    return HttpResponse(f"Turistas 🌴")
def catalogo(request):
    return HttpResponse("catalogo")
def detalles(request,id_producto):
    return HttpResponse(f"detalles {id_producto}")
def compra_inmediata(request):
    return HttpResponse("compra inmediata")
def carrito(request):
    return HttpResponse("carrito")
def checkout(request):
    return HttpResponse("checkout")

