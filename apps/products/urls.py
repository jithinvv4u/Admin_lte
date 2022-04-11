from django.urls import path, re_path
from apps.products import views
from apps.home import views as home_views

urlpatterns = [

    path('dashboard/active-products/', views.active_products, name='active-products'),

]
