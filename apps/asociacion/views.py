from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return HttpResponse("Asociación 🤝")
def dashboard(request):
    return HttpResponse("dashboard")
def empresas(request):
    return HttpResponse("empresas")
def empresasC(request):
    return HttpResponse("empresas crear")
def empresasE(request):
    return HttpResponse("empresas editar")
def empresasD(request):
    return HttpResponse("empresas eliminar")
def reportes(request):
    return HttpResponse("reportes")

