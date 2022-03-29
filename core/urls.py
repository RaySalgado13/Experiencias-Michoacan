# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    #path("", include("apps.home.urls")), IGNORAR
    path("", include("apps.turista.urls")),           # UI Kits Html files
    path("empresas/", include("apps.empresas.urls")),             # UI Kits Html files
    path("asociacion/", include("apps.asociacion.urls"))             # UI Kits Html files
]
