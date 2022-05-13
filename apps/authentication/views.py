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
from .forms import LoginForm, SignUpForm
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

            print(f"""
            {user}
            {direccion}
            {empresa}
            """)

            
            
            #######################
            #Add auth backend code#
            #https://docs.djangoproject.com/es/4.0/topics/auth/default/#topic-authorization
            #######################

            msg = '¡Usuario creado satisfactoriamente!-<a href="/login">Regresar a página de inicio</a>.'
            success = True
            
            #return redirect("/manage/empresa/")

        else:
            msg = 'El formulario no es válido, inténtelo nuevamente'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def validate():
    return HttpResponse('aaaaaaaaa')

@login_required(login_url="/login/")
@allowed_users(allowed_roles=['asociacion'])
def register_empresa(request):
    if request.method == 'POST':
        return HttpResponse(f'registrar Empresa POST')
    else:
        return HttpResponse(f'registrar Empresa GET')