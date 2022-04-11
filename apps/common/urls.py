from django.urls import path
from apps.common import views

urlpatterns = [

    path('report/export/', views.export_data, name='report-export'),

]
