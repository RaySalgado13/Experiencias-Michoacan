from cmath import exp
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.authentication.decorators import allowed_users

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return HttpResponse("Empresas 🏢")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def dashboard(request):
    return HttpResponse("dashboard")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experiencias(request):
    user = request.user
    experiencias = user.empresa.producto_set.all() #Obtiene los datos del usuario autenticado
    return HttpResponse(experiencias)

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experienciasC(request):
    return HttpResponse("experiencias crear")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experienciasE(request):
    return HttpResponse("experiencias editar")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experienciasD(request):
    return HttpResponse("experiencias borrar")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def reservaciones(request):
    return HttpResponse("reservaciones")

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
    return HttpResponse("reportes")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def correo(request):
    return HttpResponse("correo")

