# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuario",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Correo",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repetir contraseña",
                "class": "form-control"
            }
        ))
    nombre_legal = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre legal",
                "class": "form-control"
            }
        ))
    nombre_comercial = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre comercial",
                "class": "form-control"
            }
        ))
    rfc = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "RFC",
                "class": "form-control"
            }
        ))
    telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Teléfono",
                "class": "form-control"
            }
        ))
    representante = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del representante",
                "class": "form-control"
            }
        ))
    calle = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Calle",
                "class": "form-control"
            }
        ))
    numero_interior = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Número interior",
                "class": "form-control"
            }
        ), required=False)
    numero_exterior = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Número exterior",
                "class": "form-control"
            }
        ))
    colonia = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Colonia",
                "class": "form-control"
            }
        ))
    cp = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Código Postal",
                "class": "form-control"
            }
        ))
    ciudad = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ciudad",
                "class": "form-control"
            }
        ))
    
    

    class Meta: #Es donde se coloca informacion adicional acerca de la clase
        model = User
        fields = ('username', 'email', 'password1', 'password2')
