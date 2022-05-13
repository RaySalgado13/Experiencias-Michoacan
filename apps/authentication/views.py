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
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='empresas')
            user.groups.add(group)
            
            #######################
            #Add auth backend code#
            #https://docs.djangoproject.com/es/4.0/topics/auth/default/#topic-authorization
            #######################

            msg = '¡Usuario creado satisfactoriamente!-<a href="/login">Regresar a página de inicio</a>.'
            success = True
            
            #return redirect("/manage/empresa/")

        else:
            msg = 'Form is not valid'
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