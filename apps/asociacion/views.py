from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.authentication.decorators import allowed_users,unauthenticated_user
from apps.home.models import Empresa


# Create your views here.
@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion',])
def index(request):
    return HttpResponse("Asociación 🤝")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion',])
def dashboard(request):
    empresas = Empresa.objects.all()
    context = {
        "empresas" : empresas
    }
    return render(request,"asociacion/dashboard.html",context)

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion',])
def empresas(request):
    return HttpResponse("empresas")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion',])
def empresasC(request):
    return HttpResponse("empresas crear")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion',])
def empresasE(request):
    return HttpResponse("empresas editar")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion',])
def empresasD(request):
    return HttpResponse("empresas eliminar")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion',])
def reportes(request):
    return HttpResponse("reportes")

