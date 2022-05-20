# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from lib2to3.pgen2.token import EQUAL
from operator import contains
from unittest import result
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from .forms import DireccionForm, EmpresasForm, LoginForm, SignUpForm
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from apps.home.models import Empresa, Direccion

@unauthenticated_user
def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                user_groups = user.groups.all()
                for user_group in user_groups:
                    return redirect(f"/{user_group}/dashboard")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion'])
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_form = form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")

            nombre_legal = form.cleaned_data.get("nombre_legal")
            nombre_comercial = form.cleaned_data.get("nombre_comercial")
            rfc = form.cleaned_data.get("rfc")
            telefono = form.cleaned_data.get("telefono")
            representante = form.cleaned_data.get("representante")

            calle = form.cleaned_data.get("calle")
            numero_interior = form.cleaned_data.get("numero_interior")
            numero_exterior = form.cleaned_data.get("numero_exterior")
            colonia = form.cleaned_data.get("colonia")
            cp = form.cleaned_data.get("cp")
            ciudad = form.cleaned_data.get("ciudad")

            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='empresas')
            user.groups.add(group)

            direccion = Direccion.objects.create(
                calle = calle,
                numero_exterior = numero_exterior,
                numero_interior = numero_interior,
                colonia = colonia,
                cp = cp,
                ciudad = ciudad,
                estado = 'Michoacán'
            )

            empresa = Empresa.objects.create(
                nombre_legal = nombre_legal,
                nombre_comercial = nombre_comercial,
                email = email,
                rfc = rfc,
                telefono = telefono,
                representante = representante,
                direccion = direccion,
                user = user
            )
            msg = '¡Usuario creado satisfactoriamente!-<a href="/login">Regresar a página de inicio</a>.'
            success = True
            
            #return redirect("/login")

        else:
            msg = 'El formulario no es válido, inténtelo nuevamente'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success, "action": "register"})


@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion'])
def edit_empresa(request, id_empresa):
    empresa = Empresa.objects.get(id=id_empresa)

    msg = None
    success = False


    if request.method == "POST":
        form_empresas = EmpresasForm(request.POST,  instance=empresa, prefix='empresas')
        form_direccion = DireccionForm(request.POST, instance=empresa.direccion, prefix='direccion')

        if form_empresas.is_valid() and form_direccion.is_valid():
            form_empresas.save()
            form_direccion.save()
            
            return redirect("dashboard_asociacion")

        else:
            msg="Datos incorrectos, favor de verificarlos"
    else:
        form_empresas = EmpresasForm(instance=empresa, prefix='empresas')
        form_direccion = DireccionForm(instance=empresa.direccion, prefix='direccion')

    return render(request, "accounts/edit.html", {"form": form_empresas, "form_direccion":form_direccion, "msg": msg, "success": success,"action": "edit"})

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion'])
def delete_empresa(request, id_empresa):


    try:
        empresa = Empresa.objects.get(id=id_empresa)
        user = empresa.user
        empresa.delete()
        user.delete()
    except:
        print('Ocurrió un error al intentar eliminar el usuario, existe on delete protect')

    return redirect("dashboard_asociacion")
