from itertools import product
from django.views.decorators.csrf import csrf_exempt
import json
from multiprocessing import context
from turtle import st
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import View
from apps.home.models import Empresa, Producto, Imagen, Reservacion
from django.views.decorators.http import require_POST
from django.conf import settings
from .carrito import Carro
from .forms import CarroAddProcutoForm, ReservacionCreateForm
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, DetailView, TemplateView


from apps.home.models import Producto, Tipo_producto









# Create your views here.
def index(request):
    hoteles = Producto.objects.filter(tipo__tipo = "Hoteles").order_by('-modified')[:3]
    experiencias = Producto.objects.filter(tipo__tipo = "Experiencias").order_by('-modified')[:3]
    context = {
        "hoteles":hoteles,
        "experiencias": experiencias
    }
    return render(request, 'turista/index.html', context)

def catalogo(request):
    categoria = request.GET.get('categoria')
    if categoria == None:
        experiencias = Producto.objects.order_by('-modified')
    else:
        experiencias = Producto.objects.filter(tipo__tipo=categoria)
    
    page = request.GET.get('page')

    paginator = Paginator(experiencias, 8)
    experiencias = paginator.get_page(page)

    categorias = Tipo_producto.objects.all()
    context = {
        "experiencias" : experiencias,
        "categorias": categorias
    }
    return render(request,'turista/catalogo.html',context)


def detalle(request,id_producto):

    experiencias = Producto.objects.filter(id=id_producto)

    detallesObj = Producto.objects.get(id=id_producto)

    imagenes= Imagen.objects.filter(experiencia=detallesObj)
    
    carro_producto_form = CarroAddProcutoForm()


        

    context = {

        'detalles':detallesObj,
        'carro_producto_form':carro_producto_form,
        'imagenes':imagenes,
        "experiencias" : experiencias,
        
        
    }
    

    return render(request, 'turista/detalles.html', context=context)


class ProductDetailView(DetailView):
    model = Producto
    template_name = "payments/carrito_viejo.html"
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context   

    



   

def compra_inmediata(request):
    return HttpResponse("compra inmediata")


def carrit(request):

    detallecok = request.session['nombre']

    context = {
        'nombre':detallecok,
        
    }
    return render(request, 'turista/carrito_viejo.html', context=context)


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
    return redirect('carro')

def carro_remover(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.remove(producto)
    return redirect('carro')

def carro_detalle(request):
    carro = Carro(request)
    return render(request, 'turista/carrito_viejo.html', {'carro': carro})






def reser_create(request):
    carro = Carro(request)
    if request.method == 'POST':
        form = ReservacionCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            b = Reservacion.objects.latest('id')
            elme = b.id
            for item in carro:
               x = item['producto']
               r = Reservacion.objects.get(pk=elme)
               r.status="Pagado"
               r.producto.add(item['producto'])
               r.empresa = Empresa.objects.get(nombre_legal= str(x.empresa))
               r.save()
                
            # clear the cart
            carro.limpia()
            return render (request,
                            'turista/created.html',
                            {'order':order})
    else:
        form = ReservacionCreateForm()
    return render(request,
                  'turista/create.html',
                    {'cart':carro, 'form': form})