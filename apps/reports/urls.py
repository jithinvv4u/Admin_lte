from django.urls import path
from .views import getfilterNotify, getfilterStock, stock_in_hand_view, veg_price_view,wallet_transaction_view,notify_report_view,getfilterWallet,getfilterVeg

urlpatterns = [

    path('reports/veg_price/',veg_price_view,name='veg_price'),
    path('reports/wallet/',wallet_transaction_view,name='wallet_transaction'),
    path('reports/notify_report/',notify_report_view,name='notify_report'),
    path('reports/stock_in_hand/',stock_in_hand_view,name='stock_in_hand'),
    
    path('filter_notify/',getfilterNotify),
    path('filter_vegitble/',getfilterVeg),
    path('filter_wallet/',getfilterWallet),
    path('filter_stock/',getfilterStock),
    

]
