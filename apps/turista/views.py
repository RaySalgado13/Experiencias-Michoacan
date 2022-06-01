from itertools import product
from multiprocessing import context
from turtle import st
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import Producto, Imagen
from django.views.decorators.http import require_POST
from .carrito import Carro
from .forms import CarroAddProcutoForm




# Create your views here.
def index(request):
    return render(request, 'turista/index.html', {})
def catalogo(request):
    return HttpResponse("catalogo")


def detalle(request,id_producto):

    detallesObj = Producto.objects.get(id=id_producto)

    imagenObj = Imagen.objects.filter(experiencia__nombre=str(detallesObj.nombre))
    

    request.session['nombre'] = str(detallesObj.nombre)

    request.session['precio'] = int(detallesObj.precio)

    nombre = request.session['nombre']

    precio = request.session['precio']


    
    lista = [nombre]
    carro_producto_form = CarroAddProcutoForm()

    context = {

        'detalles':detallesObj,
        'carro_producto_form':carro_producto_form,
        'imagen':imagenObj,
        
    }

    


    return render(request, 'turista/detalles.html', context=context)



def compra_inmediata(request):
    return HttpResponse("compra inmediata")


def carrit(request):

    detallecok = request.session['nombre']

    context = {
        'nombre':detallecok,
        
    }
    return render(request, 'turista/carrito.html', context=context)


def checkout(request):
    return HttpResponse("checkout")


@require_POST
def carro_add(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = CarroAddProcutoForm(request.POST)
    
    carro.add(producto=producto,
                cantidad= 1,
                 )
    return redirect('turista:carro')

def carro_remover(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.remove(producto)
    return redirect('turista:carro')

def carro_detalle(request):
    carro = Carro(request)
    return render(request, 'turista/carrito.html', {'carro': carro})

