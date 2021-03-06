# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),             # UI Kits Html files
    path("", include("apps.products.urls")),
    path("", include("apps.orders.urls")),
    path("", include("apps.ffzusers.urls")),
    path("", include("apps.common.urls")),
    path("", include("apps.reports.urls")),
    path("", include("apps.temp.urls")),
]
