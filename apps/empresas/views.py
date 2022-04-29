from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return HttpResponse("Empresas 🏢")

@login_required(login_url="/login/")
def dashboard(request):
    return HttpResponse("dashboard")

@login_required(login_url="/login/")
def experiencias(request):
    return HttpResponse("experiencias")

@login_required(login_url="/login/")
def experienciasC(request):
    return HttpResponse("experiencias crear")

@login_required(login_url="/login/")
def experienciasE(request):
    return HttpResponse("experiencias editar")

@login_required(login_url="/login/")
def experienciasD(request):
    return HttpResponse("experiencias borrar")

@login_required(login_url="/login/")
def reservaciones(request):
    return HttpResponse("reservaciones")

@login_required(login_url="/login/")
def reservacionesE(request):
    return HttpResponse("reservaciones editar")

@login_required(login_url="/login/")
def reservacionesD(request):
    return HttpResponse("reservaciones borrar")

@login_required(login_url="/login/")
def reportes(request):
    return HttpResponse("reportes")

@login_required(login_url="/login/")
def correo(request):
    return HttpResponse("correo")

