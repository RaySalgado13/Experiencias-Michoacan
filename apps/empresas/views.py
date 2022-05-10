from cmath import exp
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.authentication.decorators import allowed_users
from apps.home.models import Producto,Tipo_producto, Empresa
# Create your views here.

def index(request):
    return HttpResponse("Empresas 🏢")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def dashboard(request):
    context = {
        "user": request.user
    }
    return render(request,'empresas/dashboard.html', context)

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experiencias(request):
    user = request.user
    categoria = request.GET.get('categoria')
    print(categoria)
    if categoria == None:
        #experiencias = user.empresa.producto_set.all() #Obtiene los datos del usuario autenticado
        experiencias = Producto.objects.filter(empresa__user=user)
    else:
        experiencias = Producto.objects.filter(empresa__user=user, tipo__tipo=categoria)            
    categorias = Tipo_producto.objects.all()

    context = {
        "user": request.user,
        "experiencias": experiencias,
        "categorias": categorias
    }

    
    return render(request,'empresas/experiencias.html', context)

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experienciasCreate(request):
    context = {
        "user": request.user,
    }
    return render(request,'empresas/experiencias-create.html', context)

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experienciasE(request, id_experiencia):
    return HttpResponse(f"experiencias editar {id_experiencia}")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experienciasD(request, id_experiencia):
    return HttpResponse(f"experiencias borrar {id_experiencia}")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def reservaciones(request):
    context = {
        "user": request.user,
    }
    return render(request,'empresas/reservaciones.html', context)

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def reservacionesE(request):
    return HttpResponse("reservaciones editar")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def reservacionesD(request):
    return HttpResponse("reservaciones borrar")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def reportes(request):
    context = {
        "user": request.user,
    }
    return render(request,'empresas/reportes.html', context)

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def correo(request):
    context = {
        "user": request.user,
    }
    return render(request,'empresas/mailbox.html', context)

