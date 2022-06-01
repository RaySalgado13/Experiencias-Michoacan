from cmath import exp
from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from apps.authentication.decorators import allowed_users
from django.core.paginator import Paginator
from apps.home.models import Imagen, Producto, Reservacion,Tipo_producto, Empresa
from .forms import ImagenForm,ProductoForm
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request,"empresas/index.html")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def dashboard(request):
    experiencias = Producto.objects.filter(empresa__user = request.user).order_by('-modified')[:4]

    context = {
        "experiencias":experiencias
    }
    return render(request,'empresas/dashboard.html', context)

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experiencias(request):
    user = request.user
    categoria = request.GET.get('categoria')
    page = request.GET.get('page')
    if categoria == None:
        #experiencias = user.empresa.producto_set.all() #Obtiene los datos del usuario autenticado
        experiencias = Producto.objects.filter(empresa__user=user).order_by('-modified')
    else:
        experiencias = Producto.objects.filter(empresa__user=user, tipo__tipo=categoria)        
    
    paginator = Paginator(experiencias, 8)
    experiencias = paginator.get_page(page)

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
    msg = None
    success = False

    if request.method == 'POST':

        producto_form = ProductoForm(request.POST)
        empresa = Empresa.objects.get(user = request.user)
        images = request.FILES.getlist('imagenes')

        if producto_form.is_valid():
            producto = producto_form.save()
            producto.empresa = empresa
            producto.save()

            for img in images:
                imagen = Imagen.objects.create(
                    experiencia = producto,
                    image = img
                )
            return redirect("experiencias-empresas")

        else:
            msg = 'El formulario no es válido, inténtelo nuevamente'
                
    else:
        
        producto_form = ProductoForm()

    return render(request, "empresas/experiencias-create.html", {"producto_form": producto_form, "msg":msg, "accion":"register" })


@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experienciasEdit(request, id_experiencia):
    experiencia = Producto.objects.get(id = id_experiencia)
    imagenes = experiencia.imagen_set.all()
    msg = None

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, instance=experiencia)
        images = request.FILES.getlist('imagenes')
        
        if producto_form.is_valid():
            producto = producto_form.save()
            for img in images:
                imagen = Imagen.objects.create(
                    experiencia = producto,
                    image = img
                )
            return redirect("experiencias-empresas")
        
        else:
            msg="Datos incorrectos, favor de verificarlos"

    else:
        producto_form = ProductoForm(instance=experiencia)

    return render(request, "empresas/experiencias-create.html", {"producto_form": producto_form, "imagenes":imagenes, "msg":msg, "accion":"edit" })

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experiencias_imgDelete(request, id_img):
    try:
        imagen = Imagen.objects.get(id=id_img)
        id_experiencia = imagen.experiencia.id
        imagen.delete()
    except:
        print('Ocurrió un error al intentar eliminar la imagen')
    #print(request)
    return redirect(f'/empresas/experiencias/edit/{id_experiencia}')

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def experienciasD(request, id_experiencia):
    return HttpResponse(f"experiencias borrar {id_experiencia}")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def reservaciones(request):
    empresa = Empresa.objects.get(user = request.user)
    reservaciones = Reservacion.objects.filter(empresa=empresa)
    context = {
        "reservaciones": reservaciones,
    }
    return render(request,'empresas/reservaciones.html', context)

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def reservacionesE(request):
    return HttpResponse("reservaciones editar")

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['empresas',])
def reservacionesD(request, id):
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

