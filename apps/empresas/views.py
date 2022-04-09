from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return HttpResponse("Empresas 🏢")
def dashboard(request):
    return HttpResponse("dashboard")
def experiencias(request):
    return HttpResponse("experiencias")
def experienciasC(request):
    return HttpResponse("experiencias crear")
def experienciasE(request):
    return HttpResponse("experiencias editar")
def experienciasD(request):
    return HttpResponse("experiencias borrar")
def reservaciones(request):
    return HttpResponse("reservaciones")
def reservacionesE(request):
    return HttpResponse("reservaciones editar")
def reservacionesD(request):
    return HttpResponse("reservaciones borrar")
def reportes(request):
    return HttpResponse("reportes")
def correo(request):
    return HttpResponse("correo")

