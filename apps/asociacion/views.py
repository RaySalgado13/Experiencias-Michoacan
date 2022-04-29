from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return HttpResponse("Asociación 🤝")

@login_required(login_url="/login/")
def dashboard(request):
    return HttpResponse("dashboard")

@login_required(login_url="/login/")
def empresas(request):
    return HttpResponse("empresas")

@login_required(login_url="/login/")
def empresasC(request):
    return HttpResponse("empresas crear")

@login_required(login_url="/login/")
def empresasE(request):
    return HttpResponse("empresas editar")

@login_required(login_url="/login/")
def empresasD(request):
    return HttpResponse("empresas eliminar")

@login_required(login_url="/login/")
def reportes(request):
    return HttpResponse("reportes")

