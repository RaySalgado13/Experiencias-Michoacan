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

import stripe

stripe.api_key = "sk_test_51KnukZEnY3WIng0Q1i3sIG8g92yuq8qB4EWFSJoCRxMIKsWazT9wjUW7p7TKr6CrFrVkHKEqO2AsGqDJH59AQeEI0079Qt9ehI"






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
    experiencias = Producto.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(experiencias, 8)
    experiencias = paginator.get_page(page)

    categorias = Tipo_producto.objects.all()
    context = {
        "experiencias" : experiencias
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



@csrf_exempt
def create_checkout_session(request, id):

        request_data = json.loads(request.body)
        producto = get_object_or_404(Producto, pk=id)
        product = get_object_or_404(Carro, pk=id)

        stripe.api_key = settings.STRIPE_SECRET_KEY

        checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': producto.nombre,
                    },
                    'unit_amount': int(product.precio_totald * 100),
                },
                'quantity': product.cantidad,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
        )

    # OrderDetail.objects.create(
    #     customer_email=email,
    #     product=product, ......
    # )

        order = Reservacion()
        order.producto = producto
        order.status = checkout_session['payment_intent']
        order.save()

    # return JsonResponse({'data': checkout_session})
        return JsonResponse({'sessionId': checkout_session.id})


def reser_create(request):
    carro = Carro(request)
    if request.method == 'POST':
        form = ReservacionCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            b = Reservacion.objects.latest('id')
            elme = b.id
            for item in carro:
               r = Reservacion.objects.get(pk=elme)
               r.status="Pagado"
               r.producto.add(item['producto'])
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