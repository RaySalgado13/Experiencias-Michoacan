# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls.static import static
from apps.home import views

urlpatterns = [
    path('admin/', admin.site.urls, name='administrador'),          # Django admin route
    path("", include("apps.turista.urls"), name="inicio"),
    path("", include("apps.authentication.urls"), name="auth"), # Auth routes - login / register
    path("home/", include("apps.home.urls"), name='home'),
    path("empresas/", include("apps.empresas.urls"), name="empresas"),
    path("asociacion/", include("apps.asociacion.urls")),
]

handler404 = "apps.home.views.handle_not_found"

