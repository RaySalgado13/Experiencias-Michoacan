# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, edit_empresa, delete_empresa
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('register/edit/<int:id_empresa>', edit_empresa, name="edit_empresa"),
    path('delete/<int:id_empresa>', delete_empresa, name="delete_empresa"),
    path("logout/", LogoutView.as_view(), name="logout")
]
