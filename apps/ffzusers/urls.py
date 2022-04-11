from django.urls import path
from apps.ffzusers import views

urlpatterns = [

    path('users/referral/', views.user_referrals, name='user-referrals'),

]
