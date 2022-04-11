from django.urls import path
from apps.orders import views

urlpatterns = [

    path('dashboard/zero-billed/', views.zero_billed, name='zero-billed'),
    path('dashboard/total-order-atv/', views.total_orders_atv, name='total-order-atv'),

]
