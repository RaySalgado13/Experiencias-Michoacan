from email import message
from itertools import product
from tkinter import EW
from django.views.decorators.csrf import csrf_exempt
import json
from multiprocessing import context
from turtle import st, update
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import View
from apps.home.models import Empresa, Paquete, Producto, Imagen, Reservacion
from django.views.decorators.http import require_POST
from django.conf import settings
from .carrito import Carro
from .forms import CarroAddProcutoForm, ReservacionCreateForm
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from datetime import datetime
from django.core.mail import send_mail

from apps.home.models import Producto, Tipo_producto









# Create your views here.
def index(request):
    now = datetime.now()
    paquetes = Paquete.objects.order_by('-fecha_inicio')[:3]
    productos = Producto.objects.order_by('-modified')[:3]
    context = {
        "paquetes":paquetes,
        "productos": productos
    }
    return render(request, 'turista/index.html', context)

def catalogo(request):
    now = datetime.now()
    categoria = request.GET.get('categoria')
    if categoria == None:
        productos = Producto.objects.order_by('-modified').exclude(fecha_fin__date__lt=datetime.today())
        
    else:
        productos = Producto.objects.filter(tipo__tipo=categoria)
        
    experiencias = []
    experiencias.extend(productos)
    page = request.GET.get('page')

    paginator = Paginator(experiencias, 8)
    experiencias = paginator.get_page(page)
    categorias = Tipo_producto.objects.all()
    context = {
       
        "experiencias":experiencias,
        "categorias": categorias
    }
    return render(request,'turista/catalogo.html',context)

def catalogo_paquetes(request):
   
    paquetes = Paquete.objects.order_by('-fecha_inicio')
    page = request.GET.get('page')

    paginator = Paginator(paquetes, 8)
    experiencias = paginator.get_page(page)

    context = {
       
        "experiencias":experiencias,
    }
    return render(request,'turista/catalogo_paquetes.html',context)


def detalle(request,id_producto):

    productos = Producto.objects.filter(id=id_producto)


    detallesObj = Producto.objects.get(id=id_producto)

    imagenes= Imagen.objects.filter(experiencia=detallesObj)
    
    carro_producto_form = CarroAddProcutoForm()


        

    context = {

        'detalles':detallesObj,
        'carro_producto_form':carro_producto_form,
        'imagenes':imagenes,
        "productos" : productos,
        
        
    }
    

    return render(request, 'turista/detalles.html', context=context)


def detalle_paquete(request,id_paquete):

    paquetes = Paquete.objects.filter(id=id_paquete)

    detallesObj = Paquete.objects.get(id=id_paquete)

    
    
    carro_producto_form = CarroAddProcutoForm()


        

    context = {

        'detalles':detallesObj,
        'carro_producto_form':carro_producto_form,
        
        "paquetes" : paquetes,
        
        
    }
    

    return render(request, 'turista/detalles_paquete.html', context=context)


class ProductDetailView(DetailView):
    model = Producto
    template_name = "payments/carrito_viejo.html"
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context   

    



   

def compra_inmediata(request, producto_id):
    producto = Producto.objects.filter(id=producto_id)
    pro = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        form = ReservacionCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            subject = "Tu pedido se ha completado"
            message="Tu orden numero" + str(order.id) + "se ha completado"
            email_from= settings.EMAIL_HOST_USER
            recipient_list= [request.POST["email"],]
            send_mail(subject,message,email_from,recipient_list)
            b = Reservacion.objects.latest('id')
            elme = b.id 
            x = pro.empresa
            pro = Producto.objects.get(id = producto_id)
            pro.stock = pro.stock - 1
            pro.save()
            r = Reservacion.objects.get(pk=elme)
            r.status="Pagado"
            r.producto.add(Producto.objects.get(id=producto_id))
            r.empresa = Empresa.objects.get(nombre_legal= str(x))
            r.save()

            return render(request,'turista/created.html',{'order':order, 'productos':producto,'form':form})
    else:
        form = ReservacionCreateForm()
    return render(request,'turista/create_i.html',{'productos':producto,'form':form})

def compra_inmediata_paquete(request, paquete_id):
    stock = request.GET.get('stock')
    paquete = Paquete.objects.filter(id=paquete_id)
    pro = Paquete.objects.get(id=paquete_id)
    if request.method == 'POST':
        form = ReservacionCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            subject = "Tu pedido se ha completado"
            message="Tu orden numero" + str(order.id) + "se ha completado"
            email_from= settings.EMAIL_HOST_USER
            recipient_list= [request.POST["email"],]
            send_mail(subject,message,email_from,recipient_list)
            b = Reservacion.objects.latest('id')
            elme = b.id 
            x = pro.empresa
            pro = Paquete.objects.get(id = paquete_id)
            pro.stock = pro.stock - 1
            pro.save()
            r = Reservacion.objects.get(pk=elme)
            r.status="Pagado"
            r.producto.add(Producto.objects.get(id=paquete_id))
            r.empresa = Empresa.objects.get(nombre_legal= str(x))
            r.save()

            return render(request,'turista/created.html',{'order':order, 'productos':paquete,'form':form})
    else:
        form = ReservacionCreateForm()
        print(stock)
    return render(request,'turista/create_i.html',{'productos':paquete,'form':form})



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
    if form.is_valid():
        cd = form.cleaned_data  
        carro.add(producto=producto,
                    cantidad=cd['cantidad'],
                    update_cantidad=cd['update'])


    return redirect('carro')

def carro_remover(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.remove(producto)
    return redirect('carro')

def carro_detalle(request):
    carro = Carro(request)
    for item in carro:
        item['update_cantidad_form'] = CarroAddProcutoForm(
            initial={'cantidad': item['cantidad'],
            'update': True})
        
    return render(request, 'turista/carrito_viejo.html', {'carro': carro})






def reser_create(request):
    carro = Carro(request)
    if request.method == 'POST':
        form = ReservacionCreateForm(request.POST)
        
        if form.is_valid():
            order = form.save()
            subject = "Tu pedido se ha completado"
            message="Tu orden numero" + str(order.id) + "se ha completado"
            email_from= settings.EMAIL_HOST_USER
            recipient_list= [request.POST["email"],]
            send_mail(subject,message,email_from,recipient_list)
            b = Reservacion.objects.latest('id')
            elme = b.id
            for item in carro:
               x = item['producto']
               pro = Producto.objects.get(id = x.id)
               x.stock = x.stock - int(item['cantidad'])
               x.save()
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

def reser_cance(request):
    if request.method == 'POST':
        b = Reservacion.objects.latest('id')
        b.status = "Cancelado"
        b.save()
        return render (request, 'turista/cancel.html')