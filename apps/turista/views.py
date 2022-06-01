from django.http import HttpResponse
from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator

from apps.home.models import Producto, Tipo_producto




# Create your views here.
def index(request):
    return render(request, 'turista/index.html', {})
def catalogo(request):
    experiencias = Producto.objects.all().order_by('?')
    page = request.GET.get('page')
    paginator = Paginator(experiencias, 8)
    experiencias = paginator.get_page(page)

    categorias = Tipo_producto.objects.all()
    context = {
        "experiencias" : experiencias
    }
    return render(request,'turista/catalogo.html',context)
def detalles(request,id_producto):
    return HttpResponse(f"detalles {id_producto}")
def compra_inmediata(request):
    return HttpResponse("compra inmediata")
def carrito(request):
    return HttpResponse("carrito")
def checkout(request):
    return HttpResponse("checkout")

